import numpy as np
from classes.image import Image
import os
from math import ceil
from main import Main
from main import loadAll

trained_data_file = 'trained_data'

def createClassifier():
    return Main().classifier

def loadDir(dirname):
    print("Loading data " + dirname)
    names = []
    X = []

    imagesList = os.listdir(dirname)
    numbersOfImages = len(imagesList)

    for file in imagesList:
        names.append(file)
        print(len(X)+1, '/', numbersOfImages, end = '\r')
        img = Image(dirname + file)
        X.append(img.getDescriptors())
        print(ceil((len(X) / numbersOfImages)*100), '%', end = '\r')

    return X, names

def predict_main(dirName):
    X, names = loadDir(dirName)
    X_train, y_train = loadAll() # loadData(trained_data_file)
    classifier = createClassifier()
    classifier.fit(X_train, y_train)

    predictions = classifier.predict(X)
    return [names, predictions]
