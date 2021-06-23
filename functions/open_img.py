from PIL import Image

def open_img(file, path):
    
    
    
    print('Nombre de la imagen:', file)
    
    img = Image.open(path+file)
    
    return img