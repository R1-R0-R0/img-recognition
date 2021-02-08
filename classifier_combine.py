from classifier import Classifier

class ClassifierCombine(Classifier):
    
    def __init__(self):
        self.classifiers = []

    def fit(self, X_train, y_train):
        pass

    def predict(self, X):
        pass
    
    def reset(self):
        pass

    def addClassifier(self, classifier: Classifier):
        pass

    def removeClassifier(self, classifier: Classifier):
        pass
