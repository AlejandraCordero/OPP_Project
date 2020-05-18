import cv2
import numpy as np
from ImageColor import ImageColor
from ImageJoin import ImageJoin
from ImagePerspective import ImagePerspective
from ImageShape import ImageShape
from ImageSize import ImageSize

def Picture1(img):
    a=2

    for i in range(a):
        img = ImageJoin.img_horizontal(img)
        img = ImageJoin.img_vertical(img)

    ImageShape.img_lines(img)
    ImageShape.img_circle(img)
    ImageShape.img_text(img,"Espacio gigante")
    return img


def Picture2(img):
    a = 3

    for i in range(a):
        img = ImageJoin.img_horizontal(img)
        img = ImageJoin.img_vertical(img)

    ImageShape.img_text(img,"Alejandra")
    ImageShape.img_filled(img)
    return img

imagen =cv2.imread("Images/img1.jpg")
imagen2 =cv2.imread("Images/img2.jpg")
imagen2=ImageColor.img_to_gray_scale(imagen2)
imagen=ImageSize.img_to_small(imagen)
# Picture(img)cv2.imshow("Picture 1", Picture1(imagen))
cv2.imshow("Picture 1", Picture1(imagen))
cv2.waitKey(5000)
cv2.imshow("Picture 1", Picture2(imagen2))
cv2.waitKey(5000)
