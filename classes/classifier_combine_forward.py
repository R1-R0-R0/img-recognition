from classes.classifier import Classifier
from sklearn.naive_bayes import GaussianNB;
import numpy as np;

class ClassifierCombineForward(Classifier):

    def __init__(self, *descriptorsName):
        self.descriptorsName = descriptorsName
        self.classifier = GaussianNB()
        
    def fit(self, all_X: np.array, y_train: np.array):
        X_train = []

        for line in all_X:
            combinedDescriptors = []
            for descriptorName in self.descriptorsName:
                combinedDescriptors += line[descriptorName]

            X_train.append(combinedDescriptors)

        self.classifier.fit(X_train, y_train)

    def predict(self, all_X: np.array):
        X = []

        for line in all_X:
            combinedDescriptors = []
            for descriptorName in self.descriptorsName:
                combinedDescriptors += line[descriptorName]
            
            X.append(combinedDescriptors)

        return self.classifier.predict(X)

    def reset(self):
        self.classifier = GaussianNB()
