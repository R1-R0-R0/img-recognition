import os;
import numpy as np;
from sklearn.model_selection import train_test_split;
from sklearn.naive_bayes import GaussianNB;
from image import Image;

class PercentColorsAI:

    def __init__(self):
        print("Init PercentColorsAI");

        averagePercentColors = [];
        classes = [];
        listMer = os.listdir('./Data/Mer');
        listAilleurs = os.listdir('./Data/Ailleurs');

        for file in listMer:
            img = Image("./Data/Mer/" + file);
            percentColors = img.get_colors_percents();
            averagePercentColors.append(percentColors);
            classes.append(0);

        for file in listAilleurs:
            img = Image("./Data/Ailleurs/" + file);
            percentColors = img.get_colors_percents();
            averagePercentColors.append(percentColors);
            classes.append(1);

        X = np.array(averagePercentColors);
        y = np.array(classes);

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20);

        self.classifieur = GaussianNB();
        self.classifieur.fit(X_train, y_train);

        y_preditected = self.classifieur.predict(X_test);
        print("Real classes :");
        print(y_test);
        print("Predicted classes :");
        print(y_preditected);

        print("Score: ")
        print(self.classifieur.score(X_test, y_test))

    def evaluate(self, img: Image):
        percentColors = img.get_colors_percents();

        X = np.array([percentColors]);

        y_preditected = self.classifieur.predict(X);

        return 1 if y_preditected == 0 else -1;
