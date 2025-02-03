import os
import numpy as np

def get_Paths(folder_path):
    paths = [
        os.path.join(folder_path, file)
        for file in os.listdir(folder_path)
    ]
    
    #for path in paths:
    #    print(path)

    return paths

# Salvando cada cluster em um arquivo CSV separado
def save_clusters(df, folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for cluster_num in df['cluster'].unique():
        # Filtra o DataFrame para o cluster específico
        cluster_data = df[df['cluster'] == cluster_num]
        
        if not os.path.exists("engage_clusters"):
            os.makedirs("engage_clusters")

        # Salva em um arquivo CSV
        filename = f'{folder_name}/cluster_{cluster_num}.csv'
        cluster_data.to_csv(filename, index=False)
        print(f"Cluster {cluster_num} salvo em {filename}")


