from network.transform import transform

from functions.save_img import save_img
from functions.open_img import open_img
from functions.img_a_procesar import img_a_procesar

import os

import time




inicio = time.time()


path='inputs/'

cantidad_archivos=img_a_procesar(path)


img=os.listdir(path=path)



for i in img:


    imagen = open_img(i,path)
    
    
    img_transform=transform(imagen)
    

    save_img(i, img_transform)
    
    
    
    cantidad_archivos-=1
    
    print('Imagenes restantes', cantidad_archivos)  
        
        

fin = time.time()
print('Tiempo de ejecucion', (fin-inicio)/60 ) 