from pydub import AudioSegment
import os

# Função para dividir o arquivo
def split_audio_by_size(audio_file, chunk_size_mb):
    # Carregar o arquivo de áudio
    audio = AudioSegment.from_wav(audio_file)

    # Obter o tamanho do áudio em megabytes
    audio_size = len(audio.raw_data) / (1024 * 1024)  # Tamanho em MB

    # Calcular o número de pedaços
    chunk_length_ms = len(audio) * (chunk_size_mb / audio_size)
    chunk_length_ms = int(chunk_length_ms)

    # Diretório para salvar os pedaços
    output_dir = "output_chunks"
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

# Definir o arquivo de áudio e o tamanho desejado dos pedaços (10MB)
audio_file = "Transcriptions\\audio_extraido.wav"
chunk_size_mb = 9  # 10MB por pedaço

# Chamar a função para dividir o áudio
split_audio_by_size(audio_file, chunk_size_mb)
