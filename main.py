from classes.classifier_combine import ClassifierCombine
import numpy as np
from classes.image import Image
import os

class Main:

    def __init__(self):
        self.classifier = ClassifierCombine()


def save(filename, X: np.array, y: np.array):
    print("Saving samples in Data file...")
    with open('./Data/' + filename + ".R0", 'wb') as file:
        np.save(file, X)
        np.save(file, y)
    print("Saved.")

def load(filename):
    print("Loading samples from Data file...")
    X, y = None, None
    with open('./Data/' + filename + ".R0", 'rb') as file :
        X = np.load(file)
        y = np.load(file)
    print("Loaded.")
    return X , y

def imageProcess(filename):
    return Image(filename)

def imagesProcess(foldername):
    images = os.listdir(foldername)
    loadedImages = []

    for image in images:
        loadedImages.append(imageProcess(image))

    return loadedImages

def getImageDescriptor(img: Image):
    return img.getDescriptor()

def loadData():
    print("Loading data...")

    X = []
    y = []
    listMer = os.listdir('./Data/Mer')
    listAilleurs = os.listdir('./Data/Ailleurs')

    print("Loading 'Mer' images...")
    for file in listMer:
        img = Image("./Data/Mer/" + file)
        X.append(getImageDescriptor(img))
        classes.append(0)

    print("Loading 'Ailleurs' images... ")
    for file in listAilleurs:
        img = Image("./Data/Ailleurs/" + file)
        X.append(getImageDescriptor(img))
        classes.append(1)

    print("Creating sample arrays...")
    X, y = np.array(X), np.array(y)

    print("Done.")

    return X, y
