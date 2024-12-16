import os

def get_Paths(folder_path):
    paths = [
        os.path.join(folder_path, file)
        for file in os.listdir(folder_path)
    ]
    
    #for path in paths:
    #    print(path)

    return paths


