import subprocess

#  Da runnare per epsilon constraint non commentato, approcci benchmark non commentati, approccio Lagrangian-Based
#  Heuristic non commentato e cambiando opportunamente i nomi delle cartelle

# --- CASO 1: variano solo num_services_list e num_resources ---
num_services_list_options = [[50], [100], [250], [500], [1000]]
num_resources_options = [50, 100, 250, 500, 1000]

for num_services_list in num_services_list_options:
    for num_resources in num_resources_options:
        print(f"Caso 1 -> num_services_list={num_services_list}, num_resources={num_resources}")
        subprocess.run([
            "python", "main.py",
            "--num_services_list", str(num_services_list),
            "--num_resources", str(num_resources)
        ])

# --- CASO 2: variano delta, num_services_list e num_resources ---
delta_options = [0.01, 1, 0.001]  # valutare se togliere 0.001
num_services_list_options = [[250]]
num_resources_options = [250]

for delta in delta_options:
    for num_services_list in num_services_list_options:
        for num_resources in num_resources_options:
            print(f"Caso 2 -> delta={delta}, num_services_list={num_services_list}, num_resources={num_resources}")
            subprocess.run([
                "python", "main.py",
                "--delta", str(delta),
                "--num_services_list", str(num_services_list),
                "--num_resources", str(num_resources)
            ])

# --- CASO 3: variano weights_kvi ---
weights_kvi_options = [
    [0.6, 0.2, 0.2],
    [0.2, 0.6, 0.2],
    [0.2, 0.2, 0.6]
]
num_services_list_options = [[250]]
num_resources_options = [250]

for weights_kvi in weights_kvi_options:
    for num_services_list in num_services_list_options:
        for num_resources in num_resources_options:
            print(f"Caso 3 -> weights_kvi={weights_kvi}")
            subprocess.run([
                "python", "main.py",
                "--weights_kvi", ",".join(map(str, weights_kvi)),
                "--num_services_list", str(num_services_list),
                "--num_resources", str(num_resources)
            ])

# --- CASO 4: varia J, fisso N ---
num_services_list_options = [[150, 160, 170, 180, 190]]
num_resources_options = [250]

for num_services_list in num_services_list_options:
    for num_resources in num_resources_options:
        print(f"Caso 4 -> num_services_list={num_services_list}, num_resources={num_resources}")
        subprocess.run([
            "python", "main.py",
            "--num_services_list", str(num_services_list),
            "--num_resources", str(num_resources)
        ])

# --- CASO 5: varia N, fisso J ---
num_services_list_options = [[150]]
num_resources_options = [[200], [210], [220], [230], [240]]

for num_services_list in num_services_list_options:
    for num_resources in num_resources_options:
        print(f"Caso 5 -> num_services_list={num_services_list}, num_resources={num_resources}")
        subprocess.run([
            "python", "main.py",
            "--num_services_list", str(num_services_list),
            "--num_resources", str(num_resources)
        ])
