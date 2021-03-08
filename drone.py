import numpy as np
from classes.image import Image
import os
from math import ceil
from main import Main

trained_data_file = 'trained_data'

def createClassifier():
    return Main().classifier

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
