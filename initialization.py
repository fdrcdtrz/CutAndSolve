from main import *
import numpy as np
import random


# funzioni per la normalizzazione attributi KPI e indicatori KVI e rispettivi Q e V

# esempio per ricordarti
# Per normalizzare 2 rispetto a 0.5, ad esempio, e ottenere z = (2 - 0.5) / (4 - 0.5):
# attributi_servizio = np.array([0.5, 35, 20, 1])  # 4 attributi, valore desiderato
# attributi_risorsa_1 = np.array([2, 30, 15, 1])  # 4 attributi, valori esposti dalla risorsa 1
# attributi_risorsa_2 = np.array([4, 28, 20, 2])  # 4 attributi, valori esposti dalla risorsa 2
#
# ris = np.array([attributi_risorsa_1, attributi_risorsa_2])
#
# def normalize(attributi_servizio, ris, indice_risorsa):
#     z_jn = np.zeros(len(attributi_servizio))
#
#     for index, attributo in enumerate(attributi_servizio):
#         valore_risorsa = ris[indice_risorsa, index]
#         max_val = np.max(ris[:, index])
#
#         if max_val == attributo:
#             z_jn[index] = 0
#         else:
#             z_jn[index] = (valore_risorsa - attributo) / (max_val - attributo)
#
#     return z_jn

# def normalized_kpi(services, resources, signs):
#     # services[i].kpi_service for i in len(services)
#     normalized_kpi = {}
#     weighted_sum_kpi = {}
#
#     def normalize_single_row(kpis_service, resources, index_res):
#         row = np.zeros(len(kpis_service))  # inizializzo vettore riga con i kpi della risorsa index_res-esima
#         # normalizzati per i parametri kpis_service
#
#         for index, attribute in enumerate(kpis_service):  # faccio stessa cosa di sopra considerando una risorsa ben
#             # precisa, un servizio ben preciso, ed il valore massimo esposto
#             exposed_kpi = resources[index_res].kpi_resource[index]
#             if signs[index] == 1:
#                 max_val = np.max([resource.kpi_resource[index] for resource in resources])
#                 # check per zero
#                 if max_val == attribute:
#                     row[index] = 1
#                 else:
#                     row[index] = 1 - (max_val - exposed_kpi) / (max_val - attribute)
#             else:
#                 max_val = np.max([resource.kpi_resource[index] for resource in resources])
#                 # check per zero
#                 if max_val == attribute:
#                     row[index] = 1
#                 else:
#                     row[index] = 1 - (exposed_kpi - max_val) / (max_val - attribute)
#
#         row = np.clip(row, 0, 1)  # Forza tutti i valori tra 0 e 1
#         return np.abs(row)
#
#     for j, service in enumerate(services):
#         for n, resource in enumerate(resources):
#             norm_kpi = normalize_single_row(service.kpi_service, resources, n)
#             normalized_kpi[(resource.id, service.id)] = norm_kpi
#
#             # kpi globale, sommatoria
#             q_x = np.dot(service.weights_kpi,
#                          norm_kpi)  # somma pesata da moltiplicare alla variabile decisionale nel problema di ottimizzazione
#
#             weighted_sum_kpi[(resource.id, service.id)] = float(q_x)
#
#     return normalized_kpi, weighted_sum_kpi

# def normalized_kvi(services, resources, signs):
#     # services[i].kpi_service for i in len(services)
#     normalized_kvi = {}
#     weighted_sum_kvi = {}
#
#     def normalize_single_row(kvis_service, resources, index_res):
#         row = np.zeros(len(kvis_service))  # inizializzo vettore riga con i kpi della risorsa index_res-esima
#         # normalizzati per i parametri kpis_service
#
#         for index, attribute in enumerate(kvis_service):  # faccio stessa cosa di sopra considerando una risorsa ben
#             # precisa, un servizio ben preciso, ed il valore massimo esposto
#             exposed_kvi = resources[index_res].kvi_resource[index]
#             if signs[index] == 1:
#                 #adjusted_attribute = attribute * signs[index]
#                 max_val = np.max([resource.kvi_resource[index] for resource in resources])
#                 # check per zero
#                 if max_val == attribute:
#                     row[index] = 0
#                 else:
#                     row[index] = 1 - (max_val - exposed_kvi) / (max_val - attribute)
#             else:
#                 max_val = np.max([resource.kvi_resource[index] for resource in resources])
#                 # check per zero
#                 if max_val == attribute:
#                     row[index] = 0
#                 else:
#                     row[index] = 1 - (exposed_kvi - max_val) / (max_val - attribute)
#
#         return np.abs(row)

# for j, service in enumerate(services):
#     for n, resource in enumerate(resources):
#         norm_kvi = normalize_single_row(service.kvi_service, resources, n)
#         normalized_kvi[(resource.id, service.id)] = norm_kvi
#
#         # kpi globale, sommatoria
#         v_x = np.dot(service.weights_kvi,
#                      norm_kvi)  # somma pesata da moltiplicare alla variabile decisionale nel problema di ottimizzazione
#
#         weighted_sum_kvi[(resource.id, service.id)] = float(v_x)
#
# return normalized_kvi, weighted_sum_kvi


def normalize_single_row(kvi_service, resources, index_res, signs, kvi_values):
    # kvis_service sono i tre kvi del servizio i-esimo richiesti, cioè le soglie output di LLM
    row = np.zeros(len(kvi_service))  # creo riga per i tre kvi del servizio i-esimo offerti da risorsa index_res-esima
    maximum = np.max(kvi_values, axis=0)
    # idea è normalizzarli in riferimento a quelli offerti dalla risorsa index_res-esima

    for index, attribute in enumerate(kvi_service):
        exposed_kvi = resources[index_res].kvi_resource[index] # questo deve essere il vettore offerto dalla risorsa
        # index_res-esima
        max_val = maximum[index] # questo deve essere il valore
        # massimo per quell'attributo valutato su tutte le risorse per quel servizio

        if max_val == attribute:
            row[index] = 1 # cioè è esattamente quanto chiesto
        else:
            row[index] = 1 - (max_val - exposed_kvi) / (max_val - attribute) if signs[index] == 1 else \
                1 - (exposed_kvi - max_val) / (max_val - attribute)
        #row = np.clip(row, 0, 1)  # Forza tutti i valori tra 0 e 1

    return np.abs(row)


# funzione calcolo channel gain
def compute_channel_gain_matrix(services, resources):
    gains = np.zeros((len(services), len(resources)))
    for i, service in enumerate(services):
        for j, resource in enumerate(resources):
            gains[i, j] = random.uniform(0.1, 1.0) # non so i valori precisi, da cambiare
    return gains


def compute_eavesdropper_gain(services, resources):
    gains_eavesdropper = np.zeros((len(services), len(resources)))
    for i, service in enumerate(services):
        for j, resource in enumerate(resources):
            gains_eavesdropper[i, j] = random.uniform(0.05, 0.5) # same
    return gains_eavesdropper


# funzione calcolo computation time
def compute_computation_time(service, resource):
    return service.flops / (resource.n_c * resource.speed * resource.fpc)


# funzione calcolo KVI sostenibilità ambientale
def compute_energy_sustainability(resource, computation_time, CI=475, PUE=1.67):
    return computation_time * (
            resource.n_c * resource.P_c * resource.u_c + resource.n_m * resource.P_m) * PUE * CI * 0.001


# funzione calcolo KVI trustworthiness
def compute_secrecy_capacity(service, channel_gain, eavesdropper_gain, resource):
    return max(0, np.log2(1 + (service.p_s * channel_gain / resource.N0)) -
               np.log2(1 + (service.p_s * eavesdropper_gain / resource.N0)))


# funzione calcolo KVI inclusiveness
def compute_failure_probability(computation_time, resource):
    return 1 - np.exp(-computation_time / resource.lmbd)


def compute_normalized_kvi(services, resources, CI, signs):
    # calcolo indicatori per ogni coppia (servizio, risorsa), normalizzo e faccio somma pesata per V(X) finale

    normalized_kvi = {}
    weighted_sum_kvi = {}
    gains = compute_channel_gain_matrix(services, resources)
    gains_eavesdroppers = compute_eavesdropper_gain(services, resources)

    for j, service in enumerate(services):
        kvi_values = [] # lista di future liste di lunghezza 3, vanno tutti i kvi garantiti per il servizio s

        # Calcolo degli indicatori per tutte le risorse
        for n, resource in enumerate(resources):
            secrecy_capacity = compute_secrecy_capacity(service, gains[j,n], gains_eavesdroppers[j,n],
                                                        resource)
            energy_sustainability = compute_energy_sustainability(resource, compute_computation_time(service, resource), CI)
            failure_probability = compute_failure_probability(compute_computation_time(service, resource), resource)

            kvi_values.append([secrecy_capacity, failure_probability, energy_sustainability])
            resource.kvi_resource = [secrecy_capacity, failure_probability, energy_sustainability]

        # Normalizzazione
        for n, resource in enumerate(resources):
            norm_kvi = normalize_single_row(service.kvi_service, resources, n, signs, kvi_values)
            normalized_kvi[(resource.id, service.id)] = norm_kvi

            # Somma pesata con i pesi del servizio
            v_x = np.dot(service.weights_kvi, norm_kvi)
            weighted_sum_kvi[(resource.id, service.id)] = float(v_x)

    return normalized_kvi, weighted_sum_kvi

def normalize_single_row_kpi(kpi_service, resources, index_res, signs, kpi_values):
    # kvis_service sono i tre kvi del servizio i-esimo richiesti, cioè le soglie output di LLM
    row = np.zeros(len(kpi_service))  # creo riga per i tre kvi del servizio i-esimo offerti da risorsa index_res-esima
    maximum = np.max(kpi_values, axis=0)
    # idea è normalizzarli in riferimento a quelli offerti dalla risorsa index_res-esima

    for index, attribute in enumerate(kpi_service):
        exposed_kpi = resources[index_res].kpi_resource[index] # questo deve essere il vettore offerto dalla risorsa
        # index_res-esima
        max_val = maximum[index] # questo deve essere il valore
        # massimo per quell'attributo valutato su tutte le risorse per quel servizio

        if max_val == attribute:
            row[index] = 1 # cioè è esattamente quanto chiesto
        else:
            row[index] = 1 - (max_val - exposed_kpi) / (max_val - attribute) if signs[index] == 1 else \
                1 - (exposed_kpi - max_val) / (max_val - attribute)
        row = np.clip(row, 0, 1)  # Forza tutti i valori tra 0 e 1
    return np.abs(row)

def compute_normalized_kpi(services, resources, signs):
    # calcolo indicatori per ogni coppia (servizio, risorsa), normalizzo e faccio somma pesata per Q(X) finale

    normalized_kpi = {}
    weighted_sum_kpi = {}

    for j, service in enumerate(services):
        kpi_values = [] # lista di future liste di lunghezza 4, vanno tutti i kpi garantiti per il servizio s

        # Calcolo degli indicatori per tutte le risorse
        for n, resource in enumerate(resources):
            kpi_values.append(resource.kpi_resource)
        # Normalizzazione
        for n, resource in enumerate(resources):
            norm_kpi = normalize_single_row_kpi(service.kpi_service, resources, n, signs, kpi_values)
            normalized_kpi[(resource.id, service.id)] = norm_kpi

            # Somma pesata con i pesi del servizio
            q_x = np.dot(service.weights_kpi, norm_kpi)
            weighted_sum_kpi[(resource.id, service.id)] = float(q_x)

    return normalized_kpi, weighted_sum_kpi


# esempio per ricordarsi come chiamarle
# computation_time = compute_computation_time(service, resource) -> una coppia specifica
# gains_matrix = compute_channel_gain_matrix([service], [resource])
# gains_eavesdropper = compute_eavesdropper_gain([service], [resource])
# secrecy_capacity = compute_secrecy_capacity(service, gains_matrix[0, 0], gains_eavesdropper[0, 0], resource)
# failure_prob = compute_failure_probability(computation_time, resource)
# energy_sustainability = compute_energy_sustainability(resource, computation_time, CI=400)
