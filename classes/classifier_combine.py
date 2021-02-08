from classes.classifier import Classifier
from sklearn.naive_bayes import GaussianNB;
from sklearn.model_selection import train_test_split;
import numpy as np;


class ClassifierCombine(Classifier):
    default_train_size = 0.5
    
    def __init__(self):
        self.classifiers = []
        self.classifier = GaussianNB()

    def fit(self, X_train: np.array, y_train: np.array):
        assert len(self.classifiers) > 0

        X_train1, X_train2, y_train1, y_train2 = train_test_split(X, y, test_size=default_train_size)
        
        for classifier in self.classifiers:
            classifier.fit(X_train1, y_train1)

        predictions_train2 = []
        for classifier in self.classifiers:
            predictions_train2.append(classifier.predict(X_train2))

        lines = []
        for i in range(len(y_train2)):
            line = [None]*len(self.classifiers)
            for j in range(len(predictions_train2)):
                line[j] = predictions_train2[j][i]
            
            lines.append(line)
        
        self.classifier.fit(np.array(lines), y_train2)


    def predict(self, X: np.array):
        assert len(self.classifiers) > 0

        predictions_fils = []
        for classifier in self.classifiers:
            predictions_fils.append(classifier.predict(X))

        lines = []
        for i in range(len(X)):
            line = [None]*len(self.classifiers)
            for j in range(len(predictions_fils)):
                line[j] = predictions_fils[j][i]
            
            lines.append(line)

        return self.classifier.predict(np.array(lines))
    
    def reset(self):
        self.classifier = GaussianNB()
        for classifier in self.classifiers:
            classifier.reset()

    def addClassifier(self, classifier: Classifier):
        self.classifiers.append(classifier)

    def removeClassifier(self, classifier: Classifier):
        self.classifiers.remove(classifier)
