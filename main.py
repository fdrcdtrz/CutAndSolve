import os
import time

import numpy as np

from benchmark import *
from initialization import *
from knapsacks import *


class Service:

    def __init__(self, id, demand, min_kpi, min_kvi, kpi_service_req, kvi_service_req, kpi_service, kvi_service,
                 weights_kpi, weights_kvi, size, p_s):
        self.id = id
        self.demand = demand
        self.min_kpi = 0  # valore minimo globale tollerabile kpi
        self.min_kvi = 0  # valore minimo globale tollerabile kvi
        self.kpi_service_req = np.array(kpi_service_req)  # requested minimum
        self.kvi_service_req = np.array(kvi_service_req)  # requested minimum
        self.kpi_service = np.array(kpi_service)  # 4 KPI, valore desiderato
        self.kvi_service = np.array(kvi_service)  # 3 KVI, valore desiderato
        self.weights_kpi = np.array(weights_kpi)  # per calcolo kpi globale
        self.weights_kvi = np.array(weights_kvi)  # per calcolo kvi globale
        self.size = size
        self.p_s = p_s

    # property            # first decorate the getter method
    def get_id(self):  # This getter method name is *the* name
        return self.id

    def get_demand(self):  # This getter method name is *the* name
        return self.demand

    def get_min_kpi(self):  # This getter method name is *the* name
        return self.min_kpi

    def get_min_kvi(self):  # This getter method name is *the* name
        return self.min_kvi

    def get_kpi_service_req(self):  # This getter method name is *the* name
        return self.kpi_service_req

    def get_kvi_service_req(self):  # This getter method name is *the* name
        return self.kvi_service_req

    def get_kpi_service(self):  # This getter method name is *the* name
        return self.kpi_service

    def get_kvi_service(self):  # This getter method name is *the* name
        return self.kvi_service

    def get_weights_kpi(self):  # This getter method name is *the* name
        return self.weights_kpi

    def get_weights_kvi(self):  # This getter method name is *the* name
        return self.weights_kvi

    def get_size(self):  # This getter method name is *the* name
        return self.size

    def get_p_s(self):  # This getter method name is *the* name
        return self.p_s

    def set_id(self, value):  # This getter method name is *the* name
        self.id = value

    def set_demand(self, value):  # This setter method name is *the* name
        self.demand = value

    def set_min_kpi(self, value):  # This setter method name is *the* name
        self.min_kpi = value

    def set_min_kvi(self, value):  # This setter method name is *the* name
        self.min_kvi = value

    def set_kpi_service_req(self, value):  # This setter method name is *the* name
        self.kpi_service_req = value

    def set_kvi_service_req(self, value):  # This setter method name is *the* name
        self.kvi_service_req = value

    def set_kpi_service(self, value):  # This setter method name is *the* name
        self.kpi_service = value

    def set_kvi_service(self, value):  # This setter method name is *the* name
        self.kvi_service = value

    def set_weights_kpi(self, value):  # This setter method name is *the* name
        self.weights_kpi = value

    def set_weights_kvi(self, value):  # This setter method name is *the* name
        self.weights_kvi = value

    def set_size(self, value):  # This setter method name is *the* name
        self.size = value

    def set_p_s(self, value):  # This setter method name is *the* name
        self.p_s = value


class Resource:
    def __init__(self, id, availability, kpi_resource, kvi_resource, carbon_offset, P_c, u_c, n_m, P_m, speed, fcp, N0,
                 lambda_failure, lambda_services_per_hour):
        self.id = id
        self.availability = availability
        self.kpi_resource = np.array(kpi_resource)
        self.kvi_resource = np.array(kvi_resource)
        self.carbon_offset = carbon_offset
        self.P_c = P_c
        self.u_c = u_c
        self.n_m = n_m  # memory available GBytes
        self.P_m = P_m
        self.speed = speed
        self.fpc = fcp
        self.N0 = N0
        self.lambda_failure = lambda_failure
        self.lambda_services_per_hour = lambda_services_per_hour

    def get_availability(self):  # This setter method name is *the* name
        return self.availability

    def get_kpi_resource(self):  # This setter method name is *the* name
        return self.kpi_resource

    def get_kvi_resource(self):  # This setter method name is *the* name
        return self.kvi_resource

    def get_carbon_offset(self):  # This setter method name is *the* name
        return self.carbon_offset

    def get_P_c(self):  # This setter method name is *the* name
        return self.P_c

    def get_u_c(self):  # This setter method name is *the* name
        return self.u_c

    def get_n_m(self):  # This setter method name is *the* name
        return self.n_m

    def get_P_m(self):  # This setter method name is *the* name
        return self.P_m

    def get_speed(self):  # This setter method name is *the* name
        return self.speed

    def get_fpc(self):  # This setter method name is *the* name
        return self.fpc

    def get_N0(self):  # This setter method name is *the* name
        return self.N0

    def get_lambda_failure(self):  # This setter method name is *the* name
        return self.lambda_failure

    def get_lambda_services_per_hour(self):  # This setter method name is *the* name
        return self.lambda_services_per_hour

    def set_availability(self, value):  # This setter method name is *the* name
        self.availability = value

    def set_kpi_resource(self, value):  # This setter method name is *the* name
        self.kpi_resource = value

    def set_kvi_resource(self, value):  # This setter method name is *the* name
        self.kvi_resource = value

    def set_carbon_offset(self, value):  # This setter method name is *the* name
        self.carbon_offset = value

    def set_P_c(self, value):  # This setter method name is *the* name
        self.P_c = value

    def set_u_c(self, value):  # This setter method name is *the* name
        self.u_c = value

    def set_n_m(self, value):  # This setter method name is *the* name
        self.n_m = value

    def set_P_m(self, value):  # This setter method name is *the* name
        self.P_m = value

    def set_speed(self, value):  # This setter method name is *the* name
        self.speed = value

    def set_fpc(self, value):  # This setter method name is *the* name
        self.fpc = value

    def set_N0(self, value):  # This setter method name is *the* name
        self.N0 = value

    def set_lambda_failure(self, value):  # This setter method name is *the* name
        self.lambda_failure = value

    def set_lambda_services_per_hour(self, value):  # This setter method name is *the* name
        self.lambda_services_per_hour = value


if __name__ == '__main__':

    num_services_list = [5]
    num_services_type = 8
    delta = 0.1
    num_resources = 5
    weights_kpi = [1 / 3, 1 / 3, 1 / 3]
    weights_kvi = [1 / 3, 1 / 3, 1 / 3]

    deadlines = [0.002, 0.5, 1, 150]
    deadlines_req = [0.02, 0.6, 1.2, 250]
    plrs = [20.0, 20.0, 30.0, 40.0]
    plrs_req = [35.0, 45.0, 45.0, 50.0]
    data_rates = [70.0, 100.0, 100.0, 250.0]
    data_rates_req = [60.0, 45.0, 90.0, 95.0]
    sizes = [250e6, 300e6, 600e6, 600e6]  # Mb
    p_s_values = [2, 2, 3, 4]
    demand_values = [2, 4, 10, 20]


    services = []
    for i in range(num_services_type):
        chosen_index = i % len(demand_values)

        service = Service(i, 0, 0, 0, 0, 0, 0,
                          0, weights_kpi, weights_kvi, 0, 0)

        deadline = deadlines[chosen_index]
        plr = plrs[chosen_index]
        plr_req = plrs_req[chosen_index]
        data_rate = data_rates[chosen_index]

        if deadline == 150:
            deadline_req = 250
        else:
            deadline_req = deadlines_req[chosen_index]

        if data_rate == 70:
            data_rate_req = 60
        else:
            data_rate_req = data_rates_req[chosen_index]

        service.set_kpi_service([deadline, data_rate, plr])
        service.set_kpi_service_req([deadline_req, data_rate_req, plr_req])
        service.set_demand(demand_values[chosen_index])
        service.set_p_s(p_s_values[chosen_index])
        service.set_size(sizes[chosen_index])

        services.append(service)

        print(f"Service id: {services[i].id}, {services[i].demand}, {services[i].min_kpi}, {services[i].min_kvi}, "
              f"{services[i].kpi_service}, {services[i].kpi_service_req}, {services[i].kvi_service}, {services[i].kvi_service_req}, "
              f"{services[i].size}, {services[i].p_s}")


    for num_services in num_services_list:
        results_dir = f"test_benchmark_{num_services}_200_{delta}_1"
        # path_onedrive = r"C:\Users\Federica\OneDrive - Politecnico di Bari\phd\works\comnet\Simulazioni"
        path_locale = r"C:\Users\Federica de Trizio\PycharmProjects\CutAndSolve"
        full_path = os.path.join(path_locale, results_dir)
        os.makedirs(full_path, exist_ok=True)

        # Probabilità assegnate ai servizi
        probabilities = [1, 1, 1, 3, 4, 5, 6, 7, 8, 8]
        service_requests = []

        # Generazione delle richieste basate sulla distribuzione
        for i in range(num_services):
            chosen_index = i % len(probabilities)
            service_requests.append(probabilities[chosen_index])
        print("Distribuzione delle richieste di servizio:", service_requests)

        start = time.time()

        availability_values = [10, 20, 20, 50]
        carbon_offset_values = [500000, 700000, 800000, 900000]
        P_c_values = [0.01, 0.02, 0.04, 0.04]
        u_c_values = [0.1, 0.4, 0.8, 1]
        n_m_values = [2000000, 2000000, 3000000, 6000000]
        P_m_values = [0.01, 0.01, 0.015, 0.2]
        speed_values = [20e6, 30e6, 40e6, 60e6]  # Hz
        fcp_values = [3e9, 5e9, 15e9, 15e9]  # 2 - 5 Giga cicli
        N0 = 10e-10
        lambda_failure_values = [8760, 8760, 8760, 100740]
        lambda_services_per_hour_values = [2e3, 2e3, 2e3, 3e3]

        # congiunti

        gain_values_eavesdropper = np.random.uniform(0.05, 0.5, num_resources * num_services)
        gain_values = np.random.uniform(1, 6, num_resources * num_services)

        # Indicators offered by the resources

        deadlines_off = [0.001, 0.4, 0.8, 100]
        data_rates_off = [85.0, 110.0, 110.0, 250.0]
        plr_off = [10.0, 20.0, 20.0, 40.0]

        resources = []

        for i in range(num_resources):
            chosen_index = i % len(availability_values)
            resource = Resource(i, 0, 0, [0, 0, 0], 0, 0, 0, 0, 0, 0, 0, N0, 0, 0)

            availability_value = availability_values[chosen_index]
            carbon_offset_value = carbon_offset_values[chosen_index]
            P_c_value = P_c_values[chosen_index]
            u_c_value = u_c_values[chosen_index]
            n_m_value = n_m_values[chosen_index]
            P_m_value = P_m_values[chosen_index]
            speed_value = speed_values[chosen_index]
            fcp_value = fcp_values[chosen_index]
            lambda_failure_value = lambda_failure_values[chosen_index]
            lambda_services_per_hour_value = lambda_services_per_hour_values[chosen_index]

            deadline_off = deadlines_off[chosen_index]
            data_rate_off = data_rates_off[chosen_index]
            plr_off_res = plr_off[chosen_index]

            resource.set_availability(availability_value)
            resource.set_kpi_resource([deadline_off, data_rate_off, plr_off_res])
            resource.set_carbon_offset(carbon_offset_value)
            resource.set_P_c(P_c_value)
            resource.set_u_c(u_c_value)
            resource.set_n_m(n_m_value)
            resource.set_P_m(P_m_value)
            resource.set_speed(speed_value)
            resource.set_fpc(fcp_value)
            resource.set_lambda_failure(lambda_failure_value)
            resource.set_lambda_services_per_hour(lambda_services_per_hour_value)

            resources.append(resource)


        for resource in resources:
            print(resource.id, resource.availability, resource.kpi_resource, resource.n_m, resource.fpc,
                  resource.P_m, resource.P_c, resource.speed, resource.lambda_services_per_hour)

        # Calcolo Q_MIN e computation time

        q_v_big_req(services, [-1, 1, -1], [1, -1, -1])  # qui dentro set
        # for s in services:
        #     print(f"min q rec total {s.min_kpi}, min v rec total {s.min_kvi}")

        for service in services:
            for resource in resources:
                computation_time = compute_computation_time(service, resource)
                print(computation_time)

        # TIS:  trustworthiness inclusiveness sustainability
        normalized_kvi, weighted_sum_kvi = compute_normalized_kvi(services, gain_values, gain_values_eavesdropper,
                                                                  resources, CI=475, signs=[1, -1,
                                                                                            -1])  #

        normalized_kpi, weighted_sum_kpi = compute_normalized_kpi(services, resources, signs=[-1, 1, -1])  # latenza, data rate e plr

        ############## METODO EPSILON-CONSTRAINT: CALCOLO IDEAL E NADIR POINTS E IMPLEMENTAZIONE DEL METODO ESATTO

        # V_I = optimize_kvi(service_requests, services, resources, normalized_kpi, normalized_kvi, weighted_sum_kpi, weighted_sum_kvi,
        #                    results_dir)
        #
        # Q_I = optimize_kpi(service_requests, services, resources, normalized_kpi, normalized_kvi, weighted_sum_kpi,
        #                    weighted_sum_kvi, results_dir)
        #
        # V_N = v_nadir(service_requests, services, resources, normalized_kpi, normalized_kvi,
        #               weighted_sum_kpi, weighted_sum_kvi, Q_I, results_dir)
        #
        # Q_N = q_nadir(service_requests, services, resources, normalized_kpi,
        #               normalized_kvi, weighted_sum_kpi, weighted_sum_kvi, V_I, results_dir)
        #
        #
        #
        # pareto_solutions_exact = epsilon_constraint_exact(service_requests, services, resources, normalized_kpi, normalized_kvi,
        # weighted_sum_kpi, weighted_sum_kvi, Q_N, Q_I, delta=delta, results_dir=results_dir)

        # plot_pareto_front(pareto_solutions_exact)


        ############ APPROCCI BENCHMARK: GREEDY ASSIGNMENT KPI E RANDOM ASSIGNMENT

        assignment, total_kpi, total_kvi = greedy_assignment_kpi(service_requests, services, resources,
                                                                 weighted_sum_kpi,
                                                                 weighted_sum_kvi, max_assignments=10)

        save_assignment_results(service_requests, assignment, services, resources,
                                weighted_sum_kpi, weighted_sum_kvi, normalized_kpi, normalized_kvi, total_kpi,
                                total_kvi,
                                results_dir=results_dir, filename="greedy_kpi_results.csv")

        assignment, total_kpi, total_kvi = random_assignment(service_requests, services, resources, weighted_sum_kpi,
                                                             weighted_sum_kvi)

        print(f"Assignment: {assignment}, Total KPI: {total_kpi}, Total KVI: {total_kvi}, service_requests: {service_requests}")

        save_assignment_results(service_requests, assignment, services, resources, weighted_sum_kpi,
                                weighted_sum_kvi, normalized_kpi, normalized_kvi, total_kpi, total_kvi,
                                results_dir=results_dir,
                                filename="random_results.csv")

        ############ APPROCCIO LAGRANGIAN-HEURISTIC BASED

        # Parametri del metodo subgradiente
        max_iterations = 20  # Numero massimo di iterazioni
        tolerance = 1e-3  # Soglia di convergenza
        z = 0.5  # Parametro per lo step size

        # Loop iterativo per il metodo subgradiente
        for alpha in [i / 10 for i in range(11)]:
            lambda_ = np.ones(len(service_requests)) * 0.1
            UB = float("inf")  # Upper Bound iniziale
            LB = float("-inf")  # Lower Bound iniziale

            for k in range(max_iterations):
                # Zaini
                total_value_not_lagrangian, item_assignment = multi_knapsack_dp(
                    service_requests, services, resources, weighted_sum_kpi, weighted_sum_kvi, lambda_, alpha
                )

                #  Total value lagrangian
                total_value_lagrangian = compute_total_value_lagrangian(services, resources,
                                                                        item_assignment,
                                                                        weighted_sum_kpi, weighted_sum_kvi,
                                                                        lambda_, total_value_not_lagrangian, alpha)

                print("Valore totale lagrangiano:", total_value_not_lagrangian)
                print("Valore totale lagrangiano corretto:", total_value_lagrangian)
                print("Assegnazione lagrangiana:", item_assignment)

                if is_feasible_solution(service_requests, services, resources, item_assignment, weighted_sum_kpi,
                                        weighted_sum_kvi):
                    print(f"Soluzione feasible trovata all'iterazione {k + 1}, interrompo l'ottimizzazione.")
                    save_results_csv_lagrangian(service_requests,
                                                services, resources, item_assignment, weighted_sum_kpi,
                                                weighted_sum_kvi,
                                                results_dir=results_dir, filename=f"iteration_{k + 1}.csv"
                                                )
                    break

                # Riparazione
                item_assignment_repaired = repair_solution(service_requests,
                                                           services, resources, item_assignment, weighted_sum_kpi,
                                                           weighted_sum_kvi, lambda_, alpha
                                                           )

                # Valore f. obiettivo con soluzione feasible (riparata)
                total_value_feasible = compute_total_value(service_requests,
                                                           services, resources, item_assignment_repaired,
                                                           weighted_sum_kpi,
                                                           weighted_sum_kvi, alpha
                                                           )

                print("Valore totale riparato:", total_value_feasible)
                print("Assegnazione riparata:", item_assignment_repaired)

                # Aggiorna i moltiplicatori di Lagrange, lo step size, UB e LB
                lambda_, UB, LB = update_lagrangian_multipliers(service_requests,
                                                                services, resources, item_assignment_repaired,
                                                                weighted_sum_kpi, weighted_sum_kvi,
                                                                lambda_, UB, LB, total_value_lagrangian,
                                                                total_value_feasible, z
                                                                )

                save_results_csv_lagrangian(service_requests,
                                            services, resources, item_assignment_repaired, weighted_sum_kpi,
                                            weighted_sum_kvi,
                                            results_dir=results_dir, filename=f"alpha_{alpha}_iteration_{k + 1}.csv"
                                            )

                # Convergenza
                gap = (UB - LB) / max(1, abs(LB))
                print(f"Iterazione {k + 1}: UB = {UB:.4f}, LB = {LB:.4f}, Gap = {gap:.6f}")

                if gap < tolerance:
                    print("The covergence was reached.")
                    break

                print(f"Valore finale UB: {UB}, LB: {LB}")

        # Tempo di esecuzione
        end_time = time.time()
        time_elapsed = end_time - start

        print(f"Completato per {num_services} servizi. Tempo: {time_elapsed:.6f} sec")
