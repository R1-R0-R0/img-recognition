from classes.classifier import Classifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import NearestNeighbors
from sklearn.neural_network import MLPClassifier
import numpy as np
 

def fit(descriptorsName, all_X: np.array):
    X_train = []

    for line in all_X:
        combinedDescriptors = []
        for descriptorName in descriptorsName:
            combinedDescriptors += line[descriptorName]

        X_train.append(combinedDescriptors)

    return X_train

def predict(descriptorsName, all_X: np.array):
    X = []

    for line in all_X:
        combinedDescriptors = []
        for descriptorName in descriptorsName:
            combinedDescriptors += line[descriptorName]
        
        X.append(combinedDescriptors)

    return X

class ClassifierGaussianNB(Classifier):

    def __init__(self, *descriptorsName):
        self.descriptorsName = descriptorsName
        self.reset()

    def fit(self, all_X: np.array, y_train: np.array):
        X_train = fit(self.descriptorsName, all_X)
        self.classifier.fit(X_train, y_train)

    def predict(self, all_X: np.array):
        X = predict(self.descriptorsName, all_X)
        return self.classifier.predict(X)

    def reset(self):
        self.classifier = GaussianNB()

# Not working
class ClassifierNearestNeighbors(Classifier):
    def __init__(self, nb_neighbors, *descriptorsName):
        self.descriptorsName = descriptorsName
        self.nbNeighbors = nb_neighbors
        self.reset()

    def fit(self, all_X: np.array, y_train: np.array):
        X_train = fit(self.descriptorsName, all_X)
        self.classifier.fit(X_train, y_train)

    def predict(self, all_X: np.array):
        X = predict(self.descriptorsName, all_X)
        return self.classifier.predict(X)

    def reset(self):
        self.classifier = NearestNeighbors(n_neighbors=self.nbNeighbors, algorithm='ball_tree')

# Not working
class ClassifierMLP(Classifier):

    def __init__(self, *descriptorsName):
        self.descriptorsName = descriptorsName
        self.classifier = MLPClassifier()

    def fit(self, all_X: np.array, y_train: np.array):
        X_train = fit(self.descriptorsName, all_X)
        self.classifier.fit(X_train, y_train)

    def predict(self, all_X: np.array):
        X = predict(self.descriptorsName, all_X)
        return self.classifier.predict(X)

    def reset(self):
        self.classifier = GaussianNB()
