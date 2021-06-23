from pathlib import Path


def save_img(img_name, img_upscaled):
    
    path=('outputs/')
    
    Path(path).mkdir(parents=True, exist_ok=True)
    
    img_upscaled.save(path+img_name)

    
    print('Procesada con exito'+'\n')
    