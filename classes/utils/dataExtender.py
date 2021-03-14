import os
from random import random, Random
import cv2
from math import ceil
from os import path as p


noisy_delta = 15
mirror_extension = '_mirror/'
noise_extension = '_noise_' + str(noisy_delta) + '/'
random_generator = Random()
extensions = [mirror_extension, noise_extension]

# ---

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

# ---

def createMirroredImage(dirname, filename, originalImage):
    newPath = dirname + mirror_extension + filename
    if os.path.exists(newPath):
        return

    mirroredImage = cv2.flip(originalImage, 1)
    cv2.imwrite(newPath, mirroredImage)

# ---

def createNoisyImage(dirname, filename, originalImage):
    newPath = dirname + noise_extension + filename
    if os.path.exists(newPath):
        return
    
    red, green, blue = cv2.split(originalImage)
    colors = [red, green, blue]
    for color in colors:
        for pixel in color:
            for i in range(len(pixel)):
                randomDelta = random_generator.randint(-noisy_delta, noisy_delta)
                tempPixelColor = pixel[i] + randomDelta
                tempPixelColor = 0 if tempPixelColor < 0 else tempPixelColor
                tempPixelColor = tempPixelColor if tempPixelColor < 256 else 255
                pixel[i] = tempPixelColor
                    
    noisyImage = cv2.merge(colors)
    cv2.imwrite(newPath, noisyImage)

# ---

def createExtendedDirectories():
    if not os.path.exists('./Data/Mer' + mirror_extension):
        os.makedirs('./Data/Mer' + mirror_extension)
    if not os.path.exists('./Data/Ailleurs' + mirror_extension):
        os.makedirs('./Data/Ailleurs' + mirror_extension)

    if not os.path.exists('./Data/Mer' + noise_extension):
        os.makedirs('./Data/Mer' + noise_extension)
    if not os.path.exists('./Data/Ailleurs' + noise_extension):
        os.makedirs('./Data/Ailleurs' + noise_extension)

def createExtendedImage(dirname, filename):
    path = dirname + '/' + filename
    if (path[-3:] != 'jpg' and path[-4:] != 'jpeg'):
        path = convertToJpg(path)
        filename += '.jpg'
        
    originalImage = cv2.imread(path, cv2.IMREAD_UNCHANGED)

    try:
        createMirroredImage(dirname, filename, originalImage)
    except:
        print("ERR MIRROR: " + path)
    
    try:
        createNoisyImage(dirname, filename, originalImage)
    except:
        print("ERR NOISY: " + path)

def createExtendedImages():
    createExtendedDirectories()

    listMer = os.listdir('./Data/Mer')
    listAilleurs = os.listdir('./Data/Ailleurs')
    numberOfImages = len(listMer) + len(listAilleurs)
    counter = 0

    print("Creating extended 'Mer' images...")
    for file in listMer:
        createExtendedImage('./Data/Mer', file)
        counter += 1
        print(ceil((counter / numberOfImages)*100), '%', end = '\r')

    print("Creating extended 'Ailleurs' images... ")
    for file in listAilleurs:
        createExtendedImage('./Data/Ailleurs', file)
        counter += 1
        print(ceil((counter / numberOfImages)*100), '%', end = '\r')