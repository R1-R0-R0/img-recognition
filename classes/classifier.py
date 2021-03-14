from abc import ABC, abstractmethod
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class Classifier(ABC):

    def fit(self, all_X: np.array, y_train: np.array):
        pass

    def predict(self, all_X: np.array):
        pass

    def reset(self):
        pass

class ClassifierCombine(Classifier):

    def addClassifier(self, classifier: Classifier):
        pass

    def removeClassifier(self, classifier: Classifier):
        pass


def classifier_test(classifier: Classifier, X: np.array, y: np.array, number_of_tests = 50, default_test_size = 0.20, display_multiple_tests = False):
    assert default_test_size > 0
    assert default_test_size < 1
    
    classifier.reset()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=default_test_size)

    classifier.fit(X_train, y_train)
    y_predicted = classifier.predict(X_test)

    print("--- Simple test ---")
    print("Real classes : ", y_test)
    print("Predicted classes : ", y_predicted)
    print("Score : ", accuracy_score(y_test,y_predicted))

    print()

    print("--- Testing ", number_of_tests, " times ---")
    sum = 0
    for i in range(number_of_tests):
        if (display_multiple_tests):
            print("Test n°", i)

        classifier.reset()
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=default_test_size);

        classifier.fit(X_train, y_train)
        y_predicted = classifier.predict(X_test)
        sum += accuracy_score(y_test, y_predicted)

    print("Total score : ", (sum / number_of_tests))