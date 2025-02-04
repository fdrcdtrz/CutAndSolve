import numpy as np
import random
from initialization import *
from optimization import *


class Service:
    def __init__(self, id, demand, min_kpi, min_kvi, kpi_service, kvi_service, weights_kpi, weights_kvi):
        self.id = id
        self.demand = demand
        self.min_kpi = min_kpi  # valore minimo globale tollerabile kpi
        self.min_kvi = min_kvi  # valore minimo globale tollerabile kvi
        self.kpi_service = np.array(kpi_service)  # 4 KPI, valore desiderato
        self.kvi_service = np.array(kvi_service)  # 3 KVI, valore desiderato
        self.weights_kpi = np.array(weights_kpi)  # per calcolo kpi globale
        self.weights_kvi = np.array(weights_kvi)  # per calcolo kvi globale

        # da aggiunere i parametri per il calcolo di KVI, tipo potenza, dimensione della richiesta, etc...
        # (FLOPS, P_s)


class Resource:
    def __init__(self, id, availability, kpi_resource):
        self.id = id
        self.availability = availability
        self.kpi_resource = np.array(kpi_resource)

    # da aggiunere i parametri per il calcolo di KVI (n_c, P_c, u_c, n_m, P_m, speed, fpc, N0, lambda)

# da aggiungere da qualche parte la definizione di questi due parametri: g_sj^{r_n}, g_sj^{r_n, e}, guadagno canale che dipende da servizi e risorse

if __name__ == '__main__':

    # inizializzo J servizi e N risorse
    services = [Service(j, demand=random.randint(1, 5), min_kpi=0.5, min_kvi=0.5, kpi_service=[random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)],
                        kvi_service=[random.randint(1, 50), random.randint(1, 5), random], weights_kpi=[0.25, 0.25, 0.25, 0.25], weights_kvi=[0.33, 0.33, 0.33]) for j in range(5)]
    resources = [Resource(n, availability=random.randint(1, 10), kpi_resource=[random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)]) for n in range(10)]


