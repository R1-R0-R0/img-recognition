from abc import ABC, abstractmethod

class Classifier(ABC):

    def fit(self, X_train, y_train):
        pass

    def predict(self, X):
        pass

    def reset(self):
        pass