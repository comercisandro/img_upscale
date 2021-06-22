from cv2 import dnn_superres
#from functions.open_img import open_img
import numpy as np
import os



def upscale(up_x, image):  
    
    
    #model='FSRCNN_'
    
    sr = dnn_superres.DnnSuperResImpl_create()

    #path = 'models/x2/FSRCNN_x2.pb'
    
    model_path = 'models/'+up_x+'/FSRCNN_'+up_x+'.pb'
    
    sr.readModel(model_path)
    
   

    if up_x=='x2':
        model_number=2
    
    elif up_x=='x3':
        model_number=3
    
    elif up_x=='x4':
        model_number=4
    
    elif up_x=='x8':
        model_number=8
        
    
    sr.setModel("fsrcnn", model_number)
    
    inputs=os.listdir(path='inputs/'+up_x+'/')
    
    cantidad_archivos=0

    for i in range(len(inputs)):
        cantidad_archivos+=1

    #print('Cantidad de imagenes a procesar:', cantidad_archivos)
    
     
    result = sr.upsample(image)
        
    return result
        
        
