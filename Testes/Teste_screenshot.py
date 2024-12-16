import cv2
import os

# Caminho do vídeo baixado
video_path = "C:\\Users\\dougl\\Documents\\Meus_Projetos\\Por_Disciplina\\Mestrado_AED\\Atv_Pesquisa\\Videos\\1.mp4"
output_folder = "Screenshots"

# Criar pasta para armazenar screenshots
os.makedirs(output_folder, exist_ok=True)

# Abrir o vídeo
cap = cv2.VideoCapture(video_path)

# Taxa de frames por segundo (FPS) do vídeo
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_interval = fps * 10  # A cada 10 segundos

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:  # Se não houver mais frames, saia do loop
        break
    
    # Salvar o frame no intervalo desejado
    if frame_count % frame_interval == 0:
        screenshot_path = os.path.join(output_folder, f"frame_{frame_count // fps}.jpg")
        cv2.imwrite(screenshot_path, frame)

    frame_count += 1

cap.release()
print(f"Screenshots salvas em: {output_folder}")
