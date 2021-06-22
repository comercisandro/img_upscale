from PIL import Image

def open_img(file, image_path):
    
    
    print('Nombre de la imagen:', file)
    
    img = Image.open(image_path+file)
    
    return img