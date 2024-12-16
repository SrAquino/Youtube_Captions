from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

# Chave de API do Youtube
API_KEY = os.getenv("API_KEY1")

# Função para buscar vídeos no YouTube
def get_youtube_video_links(query, max_results):
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    # Fazer a busca no YouTube
    request = youtube.search().list(
        q=query,  # O termo de pesquisa
        part='snippet',
        maxResults=max_results,  # Quantidade máxima de resultados
        type='video'
    )
    
    # Obter a resposta da API
    response = request.execute()

    # Extrair os links dos vídeos
    video_links = {}
    for item in response['items']:
        if item["id"]["kind"] == "youtube#video":
            video_id = item['id'].get('videoId')
            video_url = f'https://www.youtube.com/watch?v={video_id}'

            video_details = youtube.videos().list(
                part='snippet,statistics',
                id=video_id
            ).execute()

            stats = video_details['items'][0].get('statistics', {})

            video_language = video_details['items'][0]['snippet'].get('defaultAudioLanguage', 'Unknown')
            if video_language == 'Unknown':
                video_language = 'en-US'  # Idioma padrão

            likes = stats.get('likeCount', '0')  
            comments = stats.get('commentCount', '0')  
            views = stats.get('viewCount', '0')

            video_links[video_id]={
                'url': video_url, 
                'id': video_id,
                'language': video_language,
                'likes': likes,
                'comments': comments,
                'views': views
            }
        else:
            return None
        
    return video_links
