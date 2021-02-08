from abc import ABC, abstractmethod

class Classifier(ABC):

    def fit(self, X_train: np.array, y_train: np.array):
        pass

    def predict(self, X: np.array):
        pass

    def reset(self):
        pass