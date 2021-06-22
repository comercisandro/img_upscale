from skimage import io
from pathlib import Path

def save_img(img_upscaled,img_name, times):
    
    path=('outputs/')
    
    Path(path).mkdir(parents=True, exist_ok=True)
    
    io.imsave(path+times+img_name, img_upscaled)
    
    print('Procesada con exito'+'\n')
    