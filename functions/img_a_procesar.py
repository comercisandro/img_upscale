import os

def img_a_procesar(path):
  

    inputs=os.listdir(path=path)

    cantidad_archivos=0
    for i in range(len(inputs)):
        cantidad_archivos+=1

    
    print('Cantidad de Imagenes:', cantidad_archivos)
    
    return cantidad_archivos
 