from classes.classifier import Classifier
from classes.classifier import ClassifierCombine
from sklearn.naive_bayes import GaussianNB;
from sklearn.model_selection import train_test_split;
import numpy as np;

# Dans le cas ou plusieurs descripteurs sont utilisés, leurs combinaisons se fait par "backward"

# Not working correctly
class ClassifierCombineGaussianNB(ClassifierCombine):

    def __init__(self):
        self.classifiers = []
        self.classifier = GaussianNB()
        self.default_train_size = 0.5

    def fit(self, all_X: np.array, y_train: np.array):
        assert len(self.classifiers) > 0

        all_X1, all_X2, y_train1, y_train2 = train_test_split(all_X, y_train, test_size=self.default_train_size)
        
        for classifier in self.classifiers:
            classifier.fit(all_X1, y_train1)

        predictions_train2 = []
        for classifier in self.classifiers:
            predictions_train2.append(classifier.predict(all_X2))

        lines = []
        for i in range(len(y_train2)):
            line = [None]*len(self.classifiers)
            for j in range(len(predictions_train2)):
                line[j] = predictions_train2[j][i]
            
            lines.append(line)
        
        self.classifier.fit(np.array(lines), y_train2)


    def predict(self, all_X: np.array):
        assert len(self.classifiers) > 0

        predictions_fils = []
        for classifier in self.classifiers:
            predictions_fils.append(classifier.predict(all_X))

        lines = []
        for i in range(len(all_X)):
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

class ClassifierCombineAverage(ClassifierCombine):

    def __init__(self):
        self.classifiers = []

    def fit(self, all_X: np.array, y_train: np.array):
        assert len(self.classifiers) > 0

        for classifier in self.classifiers:
            classifier.fit(all_X, y_train)


    def predict(self, all_X: np.array):
        assert len(self.classifiers) > 0

        predictions = [0]*len(all_X)
        for classifier in self.classifiers:
            predictions_fils = classifier.predict(all_X)
            for i in range(len(predictions)):
                predictions[i] += predictions_fils[i]

        for i in range(len(predictions)):
            predictions[i] = 1 if predictions[i] > 0 else -1

        return predictions
    
    def reset(self):
        for classifier in self.classifiers:
            classifier.reset()

    def addClassifier(self, classifier: Classifier):
        self.classifiers.append(classifier)

    def removeClassifier(self, classifier: Classifier):
        self.classifiers.remove(classifier)