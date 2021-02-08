from classes.classifier import Classifier
from sklearn.naive_bayes import GaussianNB;
import numpy as np;

class ClassifierAxiom(Classifier):

    def __init__(self, criterias):
        self.criterias = criterias
        self.classifier = GaussianNB()
        
    def fit(self, all_X: np.array, y_train: np.array):
        X_train = []

        for i in range(len(all_X)):
            X_train.append(extract_X(self.criterias, all_X[i]))

        self.classifier.fit(X_train, y_train)

    def predict(self, all_X: np.array):
        X = []

        for i in range(len(all_X)):
            X.append(extract_X(self.criterias, all_X[i]))

        return self.classifier.predict(X)

    def reset(self):
        self.classifier = GaussianNB()


def extract_X(criterias, infos):
    results = []
    
    for criteria in criterias:
        results.append(infos[criteria])

    return results
