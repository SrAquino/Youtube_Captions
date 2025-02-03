import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Exemplo de dataset (substitua pelo seu)
data = {
    'video_id': ['A', 'B', 'C', 'D', 'E', 'F'],
    'views': [1000, 5000, 2000, 8000, 1500, 10000],
    'likes': [100, 300, 150, 500, 130, 900]
}

# Criar DataFrame
df = pd.DataFrame(data)

# Calcular Engajamento (likes/views)
df['engajamento'] = df['likes'] / df['views']

# Converter para formato numérico para clustering
X = df[['engajamento']].values

# Aplicar K-Means com 3 clusters (ajuste conforme necessário)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(X)

# Visualizar os resultados
plt.scatter(df['views'], df['engajamento'], c=df['cluster'], cmap='viridis', edgecolors='k')
plt.xlabel('Número de Views')
plt.ylabel('Engajamento (Likes/Views)')
plt.title('Clusterização de Vídeos por Engajamento')
plt.colorbar(label='Cluster')
plt.show()

# Exibir os clusters
print(df[['video_id', 'views', 'likes', 'engajamento', 'cluster']])
