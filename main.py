from classes.classifier_combine import ClassifierCombineGaussianNB
from classes.classifier_combine import ClassifierCombineAverage
from classes.classifier_axiom import ClassifierGaussianNB
from classes.classifier_axiom import ClassifierKNeighbors
from classes.classifier_axiom import ClassifierMLP
from classes.classifier_axiom import ClassifierRandomForest
from classes.classifier_combine import ClassifierCombineRandomForest
import numpy as np
from classes.image import Image
import os
from classes.classifier import classifier_test
from math import ceil
import classes.utils.dataExtender as DataExtender
from joblib import dump, load as loadJB

class Main:

    def __init__(self):
        classifierPercentColors = ClassifierGaussianNB('PercentColors')
        classifierPixelArray11 = ClassifierGaussianNB('PixelArrayResize:11')
        classifierPixelArray23 = ClassifierGaussianNB('PixelArrayResize:23')
        classifierPixelArray31 = ClassifierGaussianNB('PixelArrayResize:31')
        classifierPixelArray23Bis = ClassifierRandomForest('PixelArrayResize:23')
        classifierColorContrast = ClassifierGaussianNB('ColorContrast')

        classifierCombineAverage = ClassifierCombineGaussianNB()
        classifierCombineAverage.addClassifier(classifierPercentColors)
        classifierCombineAverage.addClassifier(classifierPixelArray11)
        classifierCombineAverage.addClassifier(classifierPixelArray23)
        classifierCombineAverage.addClassifier(classifierPixelArray23Bis)

        finalClassifier = ClassifierCombineRandomForest()
        finalClassifier.addClassifier(classifierCombineAverage)
        finalClassifier.addClassifier(classifierPixelArray31)
        finalClassifier.addClassifier(classifierColorContrast)

        self.classifier = finalClassifier

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

def loadDirectory(dirname, classType, startIndex, nbOfImages = None, displayLoadingFile = False):
    print("Loading data " + dirname)
    X = []
    y = []

    liste = os.listdir(dirname)
    numbersOfImages = (len(liste) - startIndex) if (nbOfImages == None) else nbOfImages

    counter = 0

    for file in liste:
        counter += 1
        if (counter < startIndex): continue

        if (displayLoadingFile): print(len(X)+1, '/', nbOfImages*2)
        img = Image(dirname + file)
        X.append(getImageDescriptors(img))
        y.append(classType)
        print(ceil((len(X) / numbersOfImages)*100), '%', end = '\r')
        if ((nbOfImages != None) and (nbOfImages <= len(X))): break

    return X, y

def loadData(numbersOfImages = None, startIndex = 0, displayLoadingFile = False):
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
            tempX, tempY = loadDirectory(directoryName, classType, startIndex, numbersOfImages, displayLoadingFile)
            X += tempX
            y += tempY

    print("Creating sample arrays...")
    X, y = np.array(X), np.array(y)

    print("Done.")

    return X, y

def saveAll():
    print("SAVING ALL")
    X, y = loadData(120, 0)
    save('data_0-120', X, y)

    X, y = loadData(120, 120)
    save('data_120-240', X, y)

    X, y = loadData(120, 240)
    save('data_240-360', X, y)

    X, y = loadData(120, 360)
    save('data_360-480', X, y)

    print("SAVE COMPLETE")

def loadAll():
    print("LOADING ALL")
    X1, y1 = load('data_0-120')
    X2, y2 = load('data_120-240')
    X3, y3 = load('data_240-360')
    X4, y4 = load ('data_360-480')

    X3 = np.concatenate((X3, X4))
    y3 = np.concatenate((y3, y4))

    X2 = np.concatenate((X2, X3))
    y2 = np.concatenate((y2, y3))

    X1 = np.concatenate((X1, X2))
    y1 = np.concatenate((y1, y2))

    print("LOAD COMPLETE")
    return X1, y1


# CREATION D'UN DESCRIPTEUR :
# - Création d'une classe implémentant Descriptor (voir classes déjà implémentés)
# - Possiblité de passer certains éléments de votre descripteur dans la classe image (A EVITER SI POSSIBLE)
# - Instancier cette classe dans listDescriptors
# - Tester votre descripteur avec le code ci-dessous en l'appelant par son nom défini
if __name__ == '__main__':
    # X, y = load('data_save')
    # DataExtender.createExtendedImages()
    # saveAll()

    X, y = loadAll()

    classifier = Main().classifier
    classifier_test(classifier, X, y, 50, 0.20, True)

    # save('bijour', X, y)
    # classifier = ClassifierGaussianNB('PercentColors')
    # classifier = ClassifierGaussianNB('PixelArrayResize:32')
    # classifier = ClassifierGaussianNB('ColorContrast:128')
    # classifier = ClassifierCombineGaussianNB()
    # classifier.addClassifier(ClassifierGaussianNB('PercentColors'))
    # classifier.addClassifier(ClassifierGaussianNB('PixelArrayResize:32'))
    # classifier.addClassifier(ClassifierGaussianNB('ColorContrast'))
    # classifier_test(classifier, X, y, 10, 0.20, True)
    # DataExtender.createExtendedImage('./Data/Mer', '838s.jpg')
    
    # Si possible, renommer classifier combine en classifier combine tardif
