import numpy as np

infoSeparator = " | "

def saveDatas (X , y , fileLink) :
    with open(fileLink + ".data", 'wb') as file :
        np.save(file, X)
    with open(fileLink + '.class', 'wb') as file:
        np.save(file, y)

def loadDatas (fileLink) :
    with open(fileLink + ".data", 'rb') as file :
        X = np.load(file)
    with open(fileLink + '.class', 'rb') as file:
        y = np.load(file)

    return X , y
