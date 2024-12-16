from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from Teste_verificaPath import getFrames

def generate_caption():
    # Carregar modelo e processador BLIP
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    # Lista de imagens (screenshots geradas anteriormente)

    image_paths = getFrames()

    # Gerar captions automaticamente
    captions = {}
    for image_path in image_paths:
        image = Image.open(image_path).convert("RGB")
        
        # Pré-processar a imagem
        inputs = processor(images=image, return_tensors="pt")
        
        # Inferência no modelo para gerar caption
        outputs = model.generate(**inputs)
        caption = processor.decode(outputs[0], skip_special_tokens=True)
        
        # Armazenar resultado
        captions[image_path] = caption

    # Exibir resultados
    for img, caption in captions.items():
        print(f"Imagem: {img}, Caption: {caption}")

if __name__ == '__main__':
    generate_caption()
