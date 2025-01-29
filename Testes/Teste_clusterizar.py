from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

# Dados de entrada
data = pd.DataFrame({
    'id': [1, 2, 3],
    'captions_vector': [np.random.rand(3) for _ in range(3)],
    'transcriptions_vector': [np.random.rand(3) for _ in range(3)],
    'likes': [100, 200, 300],
    'views': [100, 200, 300]
})

# 1. Clusterizar Captions
captions_vectors = np.array(data['captions_vector'].tolist())
kmeans_captions = KMeans(n_clusters=3, random_state=42)
data['caption_cluster'] = kmeans_captions.fit_predict(captions_vectors)

# 2. Clusterizar Transcrições
transcriptions_vectors = np.array(data['transcriptions_vector'].tolist())
kmeans_transcriptions = KMeans(n_clusters=3, random_state=42)
data['transcription_cluster'] = kmeans_transcriptions.fit_predict(transcriptions_vectors)

# 3. Clusterizar Engajamento
data['engagement'] = data['likes'] / data['views']
scaler = MinMaxScaler()
engagement_scaled = scaler.fit_transform(data[['engagement']])
kmeans_engagement = KMeans(n_clusters=3, random_state=42)
data['engagement_cluster'] = kmeans_engagement.fit_predict(engagement_scaled)

# 4. Combinação dos clusters
data['combined_cluster'] = data[['caption_cluster', 'transcription_cluster', 'engagement_cluster']].apply(tuple, axis=1)

print(data)
