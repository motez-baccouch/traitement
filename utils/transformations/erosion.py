import cv2
import numpy as np

def OTSU_threshold(img, type_img):
    if (type_img != "pgm"):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


def morph(img, transform_type, iter_number=1):
    kernel = np.ones((5, 5), np.uint8)
    if (transform_type == "EROSION"):
        return cv2.erode(img, kernel, iterations=iter_number)
    elif (transform_type == "DILATATION"):
        return cv2.dilate(img, kernel, iterations=iter_number)
    elif (transform_type == "OUVERTURE"):
        return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    elif (transform_type == "FERMETURE"):
        return cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

