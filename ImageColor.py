import cv2
import numpy as np

kernel=np.ones((5,5),np.uint8)

class ImageColor:
    """"
    Realiza cambios de color en la imagen.
    """

    def img_to_gray_scale(img):
        """"Recibe el objeto imagen y lo devuelve en blanco y negro"""
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return gray_img

    def img_to_blur(img):
        """Recive el objeto imagen y lo devuelve con opacacidad"""
        blur_img = cv2.GaussianBlur(img, (7, 7), 0)
        return blur_img

    def img_to_canny(img):
        """Recive el objeto imagen y lo devuelve con la deteccion de bordes y contornos"""
        canny_img = cv2.Canny(img, 100, 100)
        return canny_img

    def img_to_dialation(img):
        """Recive el objeto imagen y lo devuelve con la expansión de colores claros"""
        dialation_img = cv2.dilate(img, kernel, iterations=1)
        return dialation_img

    def img_to_erosion(img):
        """Recive el objeto imagen y lo devuelve con la expansión de colores oscuros"""
        eroded_img = cv2.erode(img, kernel, iterations=1)
        return eroded_img

