import cv2
import numpy as np

class ImagePerspective:
    """"
            Se realiza un cambio contando una imagen dentro de otra.
    """
    def image_persp():
        width, height = 250, 350
        puntos1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
        puntos2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(puntos1, puntos2)
        imgOutput = cv2.warpPerspective(img, matrix, (width, height))
        return imgOutput
    