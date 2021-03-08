from classes.classifier_combine import ClassifierCombineGaussianNB
from classes.classifier_combine import ClassifierCombineAverage
from classes.classifier_axiom import ClassifierGaussianNB
from classes.classifier_axiom import ClassifierKNeighbors
from classes.classifier_axiom import ClassifierMLP
from classes.classifier_axiom import ClassifierRandomForest
import numpy as np
from classes.image import Image
import os
from math import ceil
from main import loadData

trained_data_file = 'trained_data'

def createClassifier():
    classifierPercentColors = ClassifierGaussianNB('PercentColors')
    classifierPixelArray11 = ClassifierGaussianNB('PixelArrayResize:11')
    classifierPixelArray23 = ClassifierGaussianNB('PixelArrayResize:23')
    classifierPixelArray31 = ClassifierGaussianNB('PixelArrayResize:31')
    classifierPixelArray23Bis = ClassifierRandomForest('PixelArrayResize:23')
    classifierColorContrast = ClassifierGaussianNB('ColorContrast')

    classifierCombineAverage = ClassifierCombineAverage()
    classifierCombineAverage.addClassifier(classifierPercentColors)
    classifierCombineAverage.addClassifier(classifierPixelArray11)
    classifierCombineAverage.addClassifier(classifierPixelArray23)
    classifierCombineAverage.addClassifier(classifierPixelArray23Bis)

    finalClassifier = ClassifierCombineGaussianNB(0.65)
    finalClassifier.addClassifier(classifierCombineAverage)
    finalClassifier.addClassifier(classifierPixelArray31)
    finalClassifier.addClassifier(classifierColorContrast)

    return finalClassifier

def loadDir(dirname):
    print("Loading data " + dirname)
    X = []

    imagesList = os.listdir(dirname)
    numbersOfImages = len(imagesList) if (nbOfImages == None) else nbOfImages

    for file in imagesList:
        if (displayLoadingFile): print(len(X)+1, '/', nbOfImages*2)
        img = Image(dirname + file)
        X.append(getImageDescriptors(img))
        print(ceil((len(X) / numbersOfImages)*100), '%', end = '\r')

    return X

def predict_main(dirName):
    names = []

    X = loadDir(dirName)
    X_train, y_train = loadData(trained_data_file)
    classifier = createClassifier()
    classifier.fit(X_train, y_train)

    predictions = classifier.predict(X)
    for image in X:
        names.append(image.name)

    return [names, predictions]
