import os

def img_a_procesar(i):
    times=i

    img_path='inputs/'+times+'/'

    inputs=os.listdir(path=img_path)

    cantidad_archivos=0
    for i in range(len(inputs)):
        cantidad_archivos+=1

    print(times+'\n')
    
    print('Cantidad de imagenes a procesar:', cantidad_archivos)
    
    return inputs, img_path, times, cantidad_archivos