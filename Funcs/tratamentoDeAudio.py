from moviepy import VideoFileClip
import speech_recognition as sr
import os
from pydub import AudioSegment


# Função para extrair o áudio do vídeo
def extract_audio_from_video(video_path, audio_path):
    # Garante que o diretório de destino exista
    os.makedirs(os.path.dirname(audio_path), exist_ok=True)

    video = VideoFileClip(video_path)  # Carrega o vídeo
    audio = video.audio  # Extrai o áudio do vídeo
    audio.write_audiofile(audio_path)  # Salva o áudio extraído em um arquivo

# Função para dividir o arquivo
def split_audio_by_size(audio_file, chunk_size_mb, output_dir):
    # Carregar o arquivo de áudio
    audio = AudioSegment.from_wav(audio_file)

    # Obter o tamanho do áudio em megabytes
    audio_size = len(audio.raw_data) / (1024 * 1024)  # Tamanho em MB

    # Calcular o número de pedaços
    chunk_length_ms = len(audio) * (chunk_size_mb / audio_size)
    chunk_length_ms = int(chunk_length_ms)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Dividir o áudio em pedaços
    chunks = []
    start_ms = 0
    index = 1

    while start_ms < len(audio):
        end_ms = start_ms + chunk_length_ms
        chunk = audio[start_ms:end_ms]
        chunk.export(f"{output_dir}/chunk_{index}.wav", format="wav")
        chunks.append(f"{output_dir}/chunk_{index}.wav")
        start_ms = end_ms
        index += 1

    return chunks

def transcribe_audio(audio_path, video_language):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)  # Lê o áudio do arquivo
        
        try:
            # Usando o Google Web Speech API para transcrever
            text = recognizer.recognize_google(audio, language=video_language)
            print("Transcrição: ", text)
            return str(text)
        except sr.UnknownValueError:
            print("Não foi possível entender o áudio")
            return ''
        except sr.RequestError as e:
            print(f"Erro ao acessar o serviço de reconhecimento: {e}")
            return ''