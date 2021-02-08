from classes.classifier_axiom import ClassifierAxiom
from sklearn.model_selection import train_test_split
import os
from image import Image
import numpy as np
from sklearn.metrics import accuracy_score

averagePercentColors = [];
classes = [];
listMer = os.listdir('./Data/Mer');
listAilleurs = os.listdir('./Data/Ailleurs');

for file in listMer:
    print("Mer: " + file)
    img = Image("./Data/Mer/" + file)
    percentColors = img.get_colors_percents()
    dico = dict()
    dico['averageRedPercent'] = percentColors[0]
    dico['averageGreenPercent'] = percentColors[1]
    dico['averageBluePercent'] = percentColors[2]
    averagePercentColors.append(dico)
    classes.append(0)

for file in listAilleurs:
    print("Aileurs: " + file)
    img = Image("./Data/Ailleurs/" + file);
    percentColors = img.get_colors_percents();
    dico = dict()
    dico['averageRedPercent'] = percentColors[0]
    dico['averageGreenPercent'] = percentColors[1]
    dico['averageBluePercent'] = percentColors[2]
    averagePercentColors.append(dico);
    classes.append(1);

print("Fin traitement")

X = np.array(averagePercentColors);
y = np.array(classes);

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20);

classifier = ClassifierAxiom(['averageRedPercent', 'averageGreenPercent', 'averageBluePercent'])
classifier.fit(X_train, y_train)

y_predicted = classifier.predict(X_test);
print("Real classes :");
print(y_test);
print("Predicted classes :");
print(y_predicted);

print("Taux de réussite : ", accuracy_score(y_test,y_predicted))

sum = 0
for i in range(1000):
    classifier = ClassifierAxiom(['averageRedPercent', 'averageGreenPercent', 'averageBluePercent'])
    classifier.fit(X_train, y_train)

    y_predicted = classifier.predict(X_test)
    sum += accuracy_score(y_test, y_predicted)

print("Score:")
print(sum / 1000)