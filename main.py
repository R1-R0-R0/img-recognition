from classes.classifier_combine import ClassifierCombine
from classes.classifier_axiom import ClassifierAxiom
import numpy as np
from classes.image import Image
import os
from classes.classifier import classifier_test

class Main:

    def __init__(self):
        self.classifier = ClassifierCombine()

    def test(self, numberOfTests = 100, defaultTestSize = 0.20):
        X, y = loadData()
        classifier_test(self.classifier, X, y, number_of_tests=numberOfTests, default_test_size=defaultTestSize)


def save(filename, X: np.array, y: np.array):
    print("Saving samples in Data file...")
    with open('./Data/' + filename + ".R0", 'wb') as file:
        np.savez(file, a = X, b = y)
    print("Saved.")

def load(filename):
    print("Loading samples from Data file...")
    X, y = None, None
    with open('./Data/' + filename + ".R0", 'rb') as file :
        data = np.load(file, allow_pickle=True)
        X, y = data['a'], data['b']
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

def getImageDescriptors(img: Image):
    return img.getDescriptors()

def loadData():
    print("Loading data...")

    X = []
    y = []
    listMer = os.listdir('./Data/Mer')
    listAilleurs = os.listdir('./Data/Ailleurs')

    print("Loading 'Mer' images...")
    for file in listMer:
        img = Image("./Data/Mer/" + file)
        X.append(getImageDescriptors(img))
        y.append(0)

    print("Loading 'Ailleurs' images... ")
    for file in listAilleurs:
        img = Image("./Data/Ailleurs/" + file)
        X.append(getImageDescriptors(img))
        y.append(1)

    print("Creating sample arrays...")
    X, y = np.array(X), np.array(y)

    print("Done.")

    return X, y

def loadPartialData(numbersOfImages, displayLoadingFile = False):
    print("Loading data partially...")

    X = []
    y = []
    listMer = os.listdir('./Data/Mer')
    listAilleurs = os.listdir('./Data/Ailleurs')

    print("Loading 'Mer' images...")
    for file in listMer:
        if (displayLoadingFile): print(len(X)+1, '/', numbersOfImages*2)
        img = Image("./Data/Mer/" + file)
        X.append(getImageDescriptors(img))
        y.append(0)
        if (len(X) == numbersOfImages): break

    print("Loading 'Ailleurs' images... ")
    for file in listAilleurs:
        if (displayLoadingFile): print(len(X)+1, '/', numbersOfImages*2)
        img = Image("./Data/Ailleurs/" + file)
        X.append(getImageDescriptors(img))
        y.append(1)
        if (len(X) == numbersOfImages*2): break

    print("Creating sample arrays...")
    X, y = np.array(X), np.array(y)

    print("Done.")

    return X, y

# CREATION D'UN DESCRIPTEUR :
# - Création d'une classe implémentant Descriptor (voir classes déjà implémentés)
# - Possiblité de passer certains éléments de votre descripteur dans la classe image (A EVITER SI POSSIBLE)
# - Instancier cette classe dans listDescriptors
# - Tester votre descripteur avec le code ci-dessous en l'appelant par son nom défini
if __name__ == '__main__':
    X, y = loadPartialData(20, True)
    classifier = ClassifierAxiom('ColorContrast')
    classifier_test(classifier, X, y, 100, 0.20, True)
