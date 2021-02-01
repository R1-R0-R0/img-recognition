import os;
import numpy as np;
import file_mgr as fm
import imgDescriptor as id
from sklearn.model_selection import train_test_split;
from sklearn.naive_bayes import GaussianNB;
from image import Image;

class PercentColorsAI:

    def __init__(self):
        pass

    def fit(self, mode, arg):
        if (mode == 0):
            self.fit_from_file(arg)
        elif (mode == 1):
            self.fit_from_images(arg)
        else:
            print("Unknown mode. Please select 0 or 1 for fitting from saved file or images.")

    # arg = Array with 2 indexes : first is data array, second is classes array
    def fit_from_file(self, arg):
        print("Fit from file...")

        self.X, self.y = fm.loadDatas(arg)

        averagePercentColors = []
        classes = []

        self.classifier = GaussianNB()
        self.classifier.fit(self.X, self.y)
        print("Done.")

    # arg = Array with 2 indexes : first is images of "Mer" array, second is "Ailleurs"
    def fit_from_images(self, arg):
        print("Fit from images...")

        averagePercentColors = []
        classes = []

        mer = arg[0]
        ailleurs = arg[1]

        for img in mer:
            averagePercentColors.append(img.get_colors_percents())
            classes.append(0)

        for img in ailleurs:
            averagePercentColors.append(img.get_colors_percents())
            classes.append(1)

        self.X = np.array(averagePercentColors)
        self.y = np.array(classes)

        self.classifier = GaussianNB()
        self.classifier.fit(self.X, self.y)
        print("Done.")

    def evaluate(self, img: Image):
        percentColors = img.get_colors_percents()
        X = np.array([percentColors])
        y_preditected = self.classifier.predict(X)

        return 1 if y_preditected == 0 else -1

    def save_data(self, filename):
        fm.saveDatas(self.X, self.y, filename)
        print("File saved")

    def classifier_test(self):
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

class PixelArrayAi:
    def __init__(self):
        print("init PixelArrayAi")
        desiredSize = 10
        descriptors = [];
        classes = [];
        listMer = os.listdir('./Data/Mer');
        listAilleurs = os.listdir('./Data/Ailleurs');

        for file in listMer:
            descriptor = id.imgDescriptor("./Data/Mer/" + file,desiredSize)
            descriptors.append(descriptor)
            classes.append(0);

        for file in listAilleurs:
            descriptor = id.imgDescriptor("./Data/Ailleurs/" + file, desiredSize)
            descriptors.append(descriptor)
            classes.append(1);

        X = np.array(descriptors);
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
