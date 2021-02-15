from random import random, Random

import cv2
import numpy as np
from PIL import Image

def mirror(cv2Image):
    flipHorizontal = cv2.flip(cv2Image, 1)
    transformedName = '_mirrored'
    return flipHorizontal,transformedName

def noise(cv2Image):
    transformedName = '_noised'
    r = Random()
    size = 10

    for i in range(cv2Image.height):
        for j in range(cv2Image.width):

            r = int(r.randint(-size,size))
            print(cv2Image[i, j])
            cv2Image[i, j] += r
            print(cv2Image[i, j])
    return cv2Image,transformedName

def createNewImage(imagePath):
    originalImage = cv2.imread(imagePath)
    temp = imagePath.split('/')
    fullname = temp[len(temp)-1]
    dirPath=''
    dirName = temp[len(temp)-2]
    for i in range(len(temp)-2):
        dirPath += temp[i]+'/'
    newDirPath = dirPath+dirName+'_extended/'
    fullname = fullname.split('.')
    name = fullname[0]
    extension = fullname[1]

    transformedImg = [mirror(originalImage),noise(originalImage)]
    for result in transformedImg:
        newName = name + result[1]+'.'+ extension
        newPath = newDirPath + newName
        cv2.imwrite(newPath, result[0])
        print(newPath)





#mirror('Data/Mer/838s.jpg')
noise('Data/Mer/838s.jpg')