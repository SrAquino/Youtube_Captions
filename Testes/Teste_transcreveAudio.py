from moviepy import VideoFileClip
import speech_recognition as sr
import os
#from pydub import AudioSegment

# Função para extrair o áudio do vídeo
def extract_audio_from_video(video_path, audio_path):

    # Garante que o diretório de destino exista
    os.makedirs(os.path.dirname(audio_path), exist_ok=True)

    video = VideoFileClip(video_path)  # Carrega o vídeo
    audio = video.audio  # Extrai o áudio do vídeo
    audio.write_audiofile(audio_path)  # Salva o áudio extraído em um arquivo
    
    #audio = AudioSegment.from_wav(audio_path)
    #audio = audio.set_frame_rate(16000)
    #audio.export("arquivo_com_taxa_16k.wav", format="wav")

# Função para transcrever o áudio
def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)  # Lê o áudio do arquivo
        
        try:
            # Usando o Google Web Speech API para transcrever
            text = recognizer.recognize_google(audio)
            print("Transcrição: ", text)
            return text
        except sr.UnknownValueError:
            print("Não foi possível entender o áudio")
        except sr.RequestError as e:
            print(f"Erro ao acessar o serviço de reconhecimento: {e}")

# Caminhos dos arquivos
video_path = "Videos\\0XtoXITfDy8\\0XtoXITfDy8.mp4"  # Substitua com o caminho do seu vídeo
audio_path = "Videos\\0XtoXITfDy8\\Audio\\0XtoXITfDy8.wav"  # Caminho onde o áudio extraído será salvo

import os
print("Diretório atual:", os.getcwd())

# Extração do áudio e transcrição
extract_audio_from_video(video_path, audio_path)
#transcribe_audio(audio_path)
