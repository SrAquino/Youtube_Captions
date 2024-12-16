import yt_dlp

def download_video(url):
    # Configurar para baixar o vídeo
    ydl_opts = {
        'quiet': True,  # Suprimir mensagens no console
        'format': 'best',  # Formato do vídeo a ser baixado
        'outtmpl': 'Videos/%(id)s/%(id)s.%(ext)s',  # Pasta de saída e nome do arquivo
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])