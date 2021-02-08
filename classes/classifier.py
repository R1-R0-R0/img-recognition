from abc import ABC, abstractmethod
import numpy as np;

class Classifier(ABC):

    def fit(self, X_train: np.array, y_train: np.array):
        pass

    def predict(self, X: np.array):
        pass

    def reset(self):
        pass

    def score(self, y_test: np.array, y_predicted: np.array):
        pass