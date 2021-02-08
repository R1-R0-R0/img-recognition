from classes.classifier import Classifier
from sklearn.naive_bayes import GaussianNB;
import numpy as np;

class ClassifierAxiom(Classifier):

    def __init__(self, descriptorName):
        self.descriptorName = descriptorName
        self.classifier = GaussianNB()
        
    def fit(self, all_X: np.array, y_train: np.array):
        X_train = []

        for line in all_X:
            X_train.append(line[self.descriptorName])

        self.classifier.fit(X_train, y_train)

    def predict(self, all_X: np.array):
        X = []

        for line in all_X:
            X.append(line[self.descriptorName])

        return self.classifier.predict(X)

    def reset(self):
        self.classifier = GaussianNB()
