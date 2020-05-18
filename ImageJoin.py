import cv2
import numpy as np
from ImageColor import ImageColor

class ImageJoin():
    """"
           Une en un mismo gráfico la misma imagen.
    """
    def img_horizontal(img):
        imgHorizontal = np.hstack((img, img))
        return imgHorizontal

    def img_vertical(img):
        imgVertical = np.vstack((img, img))
        return imgVertical
    