import os

# Defina o caminho da pasta onde estão os frames
folder_path = "Screenshots"

def getFrames():
# Obtenha os caminhos completos de todos os arquivos na pasta
    image_paths = [
        os.path.join(folder_path, file)
        for file in os.listdir(folder_path)
        if file.lower().endswith((".jpg", ".jpeg", ".png"))  # Filtrar imagens
    ]
    # Exibir os caminhos encontrados
    for path in image_paths:
        print(path)
        
    return image_paths




