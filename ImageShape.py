import cv2
import numpy as np

class ImageShape:
    """"
        Dibuja en un cuadro una línea. rectángulo, circulo.
    """
    def img_lines(img):
        """"Dibuja la línea """
        print ( cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3))

    def img_rectangle(img):
        """"Dibuja el rectángulo """
        print (cv2.rectangle(img,(0,0),(250,350),(0,0,255),2))

    def img_filled(img):
        """"Dibuja el rectángulo relleno """
        print(cv2.rectangle(img, (0, 0), (150, 150), (0, 0, 255), cv2.FILLED))

    def img_circle(img):
        """"Dibuja un círculo """
        print(cv2.circle(img,(400,50),30,(255,255,0),5))

    def img_text(img, texto):
        """"Dibuja un texto """
        print(cv2.putText(img,texto,(150,300),cv2.FONT_HERSHEY_COMPLEX,2,(0,150,0),1))

