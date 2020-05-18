import cv2
import numpy as np


class ImageSize:
    """"
        Realiza cambios de tamaño en la imagen.
    """
    def img_to_small(img):
        """"Recibe el objeto imagen y lo devuelve más pequeño"""
        imgResize = cv2.resize(img,(150,100))
        return imgResize

    def img_to_crop(img):
        """"Recibe el objeto imagen y lo devuelve una parte cortada de  la imagen"""
        imgCrop = img[0:200,200:500]
        return imgCrop

    
   