TODO:
1. Da aggiunere i parametri per il calcolo di KVI, tipo potenza, dimensione della richiesta, (FLOPS, P_s)
2. Da aggiunere i parametri per il calcolo di KVI (n_c, P_c, u_c, n_m, P_m, speed, fpc, N0, lambda)
3. Da aggiungere da qualche parte la definizione di questi due parametri: g_sj^{r_n}, g_sj^{r_n, e}, guadagno canale che dipende da servizi e risorse
4. calcolo kvi
5. rivedere cut and solveeee reduced cost da correggere
6. rivedere aggiornamento di epsilon!! non modifico delta, modifico la soluzione che va da QN a QI, quindi da migliore per V (VI) a peggiore per V (VN)


# Ottimizzazione Multi-Obiettivo con Metodo Epsilon-Constraint esatto e Cut-and-Solve

Questo progetto implementa una soluzione di ottimizzazione per l'assegnazione di servizi a risorse in un sistema con due obiettivi, KPI e KVI. Il modello utilizza i metodi **Epsilon-Constraint** esatto e **Cut-and-Solve** per trovare la soluzione ottima sotto vincoli multi-obiettivo. 

### Metodo Epsilon-Constraint

Il metodo epsilon-constraint è utilizzato per ottimizzare un obiettivo mentre si vincola l'altro a un valore specifico. L'algoritmo viene iterato su diverse soglie, ottenendo soluzioni efficienti rispetto alla combinazione dei due obiettivi.

### Cut-and-Solve

Il metodo cut-and-solve è impiegato per risolvere il problema di ottimizzazione riducendo il problema a sottoproblemi più piccoli, migliorando così l'efficienza della soluzione.
