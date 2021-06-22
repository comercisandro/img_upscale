from functions.open_img import open_img
import numpy as np
from PIL import Image
from skimage import io
from pathlib import Path
import os

from functions.save_img import save_img
from network.upscale import upscale

import time
inicio = time.time()

folders='inputs/'



folder=os.listdir(path=folders)

print(folder)

for i in folder:

    times=i

    img_path='inputs/'+times+'/'

    inputs=os.listdir(path=img_path)

    cantidad_archivos=0
    for i in range(len(inputs)):
        cantidad_archivos+=1

    print(times+'\n')
    
    print('Cantidad de imagenes a procesar:', cantidad_archivos+'\n')
        

    
    for i in inputs:
    
        img = open_img(i,img_path)
        
        lr_img = np.array(img)

        result=upscale(times, lr_img)
        
        save_img(result,i,times)
        
        
        
        cantidad_archivos-=1
        
        print('Imagenes restantes', cantidad_archivos)  
        
        
        
        
        
fin = time.time()
print('Tiempo de ejecucion', (fin-inicio)/60 ) 