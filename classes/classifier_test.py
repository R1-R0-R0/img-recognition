from classes.classifier import Classifier


class ClassifierTest(Classifier):

    def __init__(self,name, classifier, param1, param2):
        self.descriptorName = name
        self.classifier = classifier
        self.param1 = param1
        self.param2 = param2

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
        self.classifier.reset()