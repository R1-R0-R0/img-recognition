from classes.classifier_combine import ClassifierCombineGaussianNB
from classes.classifier_combine import ClassifierCombineAverage
from classes.classifier_axiom import ClassifierGaussianNB
from classes.classifier_axiom import ClassifierNearestNeighbors
import numpy as np
from classes.image import Image
import os
from classes.classifier import classifier_test
from math import ceil
import classes.utils.dataExtender as DataExtender

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

def loadDirectory(dirname, classType, nbOfImages = None, displayLoadingFile = False):
    print("Loading data " + dirname)
    X = []
    y = []

    liste = os.listdir(dirname)
    numbersOfImages = len(liste) if (nbOfImages == None) else nbOfImages

    for file in liste:
        if (displayLoadingFile): print(len(X)+1, '/', nbOfImages*2)
        img = Image(dirname + file)
        X.append(getImageDescriptors(img))
        y.append(classType)
        print(ceil((len(X) / numbersOfImages)*100), '%', end = '\r')
        if ((nbOfImages != None) and (nbOfImages <= len(X))): break

    return X, y

def loadData(numbersOfImages = None, displayLoadingFile = False):
    if (numbersOfImages != None): print("Loading " + str(numbersOfImages) + " images...")
    else: print("Loading all data (this might take a while)...")

    X = []
    y = []
    dirData = './Data/{}'
    dirsData = [dirData + '/'] + [dirData + extension for extension in DataExtender.extensions]
    for temp in [['Mer', 1], ['Ailleurs', -1]]:
        name = temp[0]
        classType = temp[1]
        print("Loading '" + name + "' images...")

        for directory in dirsData:
            directoryName = directory.format(name)
            tempX, tempY = loadDirectory(directoryName, classType, numbersOfImages, displayLoadingFile)
            X += tempX
            y += tempY

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
    # X, y = load('data_save')
    X, y = loadData(10)
    # save('data_save', X, y)
    # classifier = ClassifierAxiom('PixelArrayResize')
    # classifier = ClassifierGaussianNB('PercentColors')
    classifier = ClassifierGaussianNB('PixelArrayResize:32')
    # classifier = ClassifierGaussianNB('ColorContrast:128')
    # classifier = ClassifierCombineGaussianNB()
    # classifier = ClassifierCombine()
    # classifier.addClassifier(ClassifierGaussianNB('PercentColors'))
    # classifier.addClassifier(ClassifierGaussianNB('PixelArrayResize'))
    # classifier.addClassifier(ClassifierGaussianNB('ColorContrast'))
    classifier_test(classifier, X, y, 100, 0.20, False)
    # DataExtender.createExtendedImage('./Data/Mer', '838s.jpg')
    # DataExtender.createExtendedImages()
    
    # Si possible, renommer classifier combine en classifier combine tardif
