from classes.descriptor import Descriptor
from classes.utils.imgResizer import ImageResizer
import cv2
import numpy as np
import pixel as px
from PIL import Image
from os import path as p

class ColorContrast(Descriptor):

    def __init__(self):
        self.desiredSize = 128
        self.resizer = ImageResizer(self.desiredSize)
        
    def getImageInfo(self, image):
        path = image.getPath()

        if (path[-3:] != 'jpg' and path[-4:] != 'jpeg'):
            path = convertToJpg(path)
        
        resizedImg = self.resizer.cv2Resize(path)

        hogDescriptor = cv2.HOGDescriptor("./classes/utils/hog.xml")
        computedHog = hogDescriptor.compute(resizedImg)
        hog = []

        for i in computedHog:
            hog.append(i[0])

        return hog

    def getName(self):
        return 'ColorContrast'


# /!\ PEUT CAUSER DES SOUCIS
def convertToJpg(path):
    if (path[-3:] != 'png'):
        print("IMAGE ", path, " NON PRIS EN CHARGE")
        exit()

    image = cv2.imread(path)
    newPath = path + '.jpg'

    if not(p.exists(newPath)):
        cv2.imwrite(newPath, image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

    return newPath
        
