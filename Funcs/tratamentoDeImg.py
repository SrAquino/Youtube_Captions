import cv2
import os
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

def make_ScreenShots(video_path, output_folder,intervalo):
    # Criar pasta para armazenar screenshots
    os.makedirs(output_folder, exist_ok=True)

    # Abrir o vídeo
    cap = cv2.VideoCapture(video_path)

    # Taxa de frames por segundo (FPS) do vídeo
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_interval = fps * intervalo

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

def generate_caption(image_path):
    # Carregar modelo e processador BLIP
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    # Lista de imagens (screenshots geradas anteriormente)

    # Gerar captions automaticamente
    #captions = {}
    #for image_path in image_paths:
    image = Image.open(image_path).convert("RGB")
        
    # Pré-processar a imagem
    inputs = processor(images=image, return_tensors="pt")
        
    # Inferência no modelo para gerar caption
    outputs = model.generate(**inputs)
    caption = processor.decode(outputs[0], skip_special_tokens=True)
        
    # Armazenar resultado
    #captions[image_path] = caption
    print(caption)
        
    return caption

    # Exibir resultados
    #for img, caption in captions.items():
    #    print(f"Imagem: {img}, Caption: {caption}")

if __name__ == '__main__':
    print('ok')
    #generate_caption(get_Paths('Videos\\C48oHf1TOcg\\Screenshots'))