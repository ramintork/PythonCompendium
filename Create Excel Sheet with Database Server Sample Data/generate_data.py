
import pandas as pd
import numpy as np
import random

def generate_sample_data(num_servers=100):
    server_types = {
        "Oracle database server": "ORA",
        "Oracle RAC": "ORA_RAC",
        "Ms SQL server": "SQL",
        "Sybase ASE": "SYB",
        "Sybase repserver": "SYB_REP",
        "Sybase IQ": "SYB_IQ",
        "Postgresql": "PG",
        "MongoDB": "MONGO"
    }
    regions = ["AMER", "APAC", "EMEA", "CH"]

    data = []
    for i in range(num_servers):
        server_type_name = random.choice(list(server_types.keys()))
        server_type_prefix = server_types[server_type_name]
        region = random.choice(regions)
        server_id = i + 1
        server_name = f"{server_type_prefix}_{region}_{server_id}"

        cpu = round(random.uniform(10, 90), 2)
        io = round(random.uniform(5, 80), 2)
        storage = round(random.uniform(20, 95), 2)
        memory = round(random.uniform(15, 85), 2)

        cpu_base = round(cpu * random.uniform(0.7, 0.9), 2)
        io_base = round(io * random.uniform(0.7, 0.9), 2)
        storage_base = round(storage * random.uniform(0.7, 0.9), 2)
        memory_base = round(memory * random.uniform(0.7, 0.9), 2)

        cpu_thresh = round(cpu * random.uniform(1.1, 1.3), 2)
        io_thresh = round(io * random.uniform(1.1, 1.3), 2)
        storage_thresh = round(storage * random.uniform(1.1, 1.3), 2)
        memory_thresh = round(memory * random.uniform(1.1, 1.3), 2)

        criticality = random.choice(["High", "Medium", "Low"])
        timestamp = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")

        data.append({
            "Servername": server_name,
            "type": server_type_name,
            "CPU": cpu,
            "IO": io,
            "Storage": storage,
            "Memory": memory,
            "CPU_base": cpu_base,
            "IO_base": io_base,
            "Storage_base": storage_base,
            "Memory_base": memory_base,
            "CPU_thresh": cpu_thresh,
            "IO_thresh": io_thresh,
            "Storage_thresh": storage_thresh,
            "Memory_thresh": memory_thresh,
            "criticality": criticality,
            "region": region,
            "timestamp": timestamp
        })

    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = generate_sample_data()
    df.to_csv("server_data.csv", index=False)
    print("Sample data generated and saved to server_data.csv")


