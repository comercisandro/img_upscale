from network.upscale import upscale

from network.resize import resize






def transform(image):
 
#·······························································#
#                                                               #
#                       960x540                                 #
#                                                               #
#·······························································#
    
    if image.size==(1300, 731):
        
        
        up_x='x2'
        
        img_upscale=upscale(up_x, image)
        
        dim=(1920,1080)
        
        img_resize=resize(img_upscale, dim)
        
        
        return img_resize
        
        
        
        
    if image.size==(800,450) or image.size==(640,360):
        
        up_x='x3'
        
        img_upscale=upscale(up_x, image)
        
        dim=(1920,1080)
        
        img_resize=resize(img_upscale, dim)
        
        
        return img_resize