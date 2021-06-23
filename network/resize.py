import cv2
from PIL import Image


def resize(img,dim):

    inter= cv2.INTER_AREA
    
    resized = cv2.resize(img, dim, interpolation = inter)

    #lr_img = np.array(resized)
    
    
    print('RESIZE')   
    #print("Tamaño original: ", img.shape)
    print("Nuevo tamaño:", resized.shape)
    
    resized=Image.fromarray(resized)
    
    return resized