import os
from enum import Enum
from random import random, Random
from functools import partial


import cv2
import numpy as np
from PIL import Image
from os import path as p





def mirror(cv2Image):
    flipHorizontal = cv2.flip(cv2Image, 1)
    transformedName = '_mirrored'
    return flipHorizontal


def noise(cv2Image):
    transformedName = '_noised'
    ra = Random()
    size = 30
    r, g, b = cv2.split(cv2Image)
    colors = [r, g, b]
    for col in colors:
        for p in col:
            for i in range(len(p)):
                # print(a[i])
                v = ra.randint(-size, size)
                if (p[i] < 255 - size) & (p[i] > 0 + size):
                    p[i] += v
    img4 = cv2.merge([r, g, b])
    return img4

class Transformation(Enum):
    _mirrored = partial(mirror)
    _noised = partial(noise)


def createNewImage(imagePath):
    print(imagePath)
    originalImage = cv2.imread(imagePath, cv2.IMREAD_UNCHANGED)
    temp = imagePath.split('/')
    fullname = temp[len(temp) - 1]
    dirPath = ''
    dirName = temp[len(temp) - 2]
    for i in range(len(temp) - 2):
        dirPath += temp[i] + '/'
    newDirPath = dirPath + dirName + '_extended/'
    spitedfullname = fullname.split('.')
    extension = '.'+spitedfullname[len(spitedfullname) - 1]
    name = fullname[0: -(len(extension))]
    for t in Transformation:
        newName = name + t.name + extension
        newPath = newDirPath + newName
        if not p.exists(newPath):
            cv2.imwrite(newPath, t.value(originalImage))
            print(newPath)


def creatAll():
    listMer = os.listdir('./Data/Mer')
    listAilleurs = os.listdir('./Data/Ailleurs')
    for file in listMer:
        path = 'Data/Mer/' + file
        createNewImage(path)

    for file in listAilleurs:
        path = 'Data/Ailleurs/' + file
        if not (p.exists(path)):
            createNewImage(path)


# mirror('Data/Mer/838s.jpg')
# noise('Data/Mer/838s.jpg')
# createNewImage('Data/Mer/838s.jpg')
creatAll()
