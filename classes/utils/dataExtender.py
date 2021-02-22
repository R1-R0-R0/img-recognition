import os
from random import random, Random
import cv2
from math import ceil


noisy_delta = 30
mirror_extension = '_mirror/'
noise_extension = '_noise_' + str(noisy_delta) + '/'
random_generator = Random()
extensions = [mirror_extension, noise_extension]

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
    originalImage = cv2.imread(dirname + '/' + filename, cv2.IMREAD_UNCHANGED)
    try:
        createMirroredImage('./Data/Mer', filename, originalImage)
    except:
        pass
    
    try:
        createNoisyImage('./Data/Mer', filename, originalImage)
    except:
        pass

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
