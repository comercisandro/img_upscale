import numpy as np
import os

from functions.open_img import open_img
from functions.save_img import save_img
from functions.img_a_procesar import img_a_procesar

from network.upscale import upscale

import time
inicio = time.time()

folders='inputs/'



folder=os.listdir(path=folders)



for i in folder:

    
    inputs, img_path, times, cantidad_archivos=img_a_procesar(i)

    
    for i in inputs:
    
        img = open_img(i,img_path)
        
        lr_img = np.array(img)

        result=upscale(times, lr_img)
        
        save_img(result,i,times)
        
        
        
        cantidad_archivos-=1
        
        print('Imagenes restantes', cantidad_archivos)  
        
        
        
        
        
fin = time.time()
print('Tiempo de ejecucion', (fin-inicio)/60 ) 