from classes.classifier_axiom import ClassifierAxiom
from classes.classifier import classifier_test as ct
import os
from image import Image
import numpy as np

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

classifier = ClassifierAxiom(['averageRedPercent', 'averageGreenPercent', 'averageBluePercent'])
ct(classifier, X, y, number_of_tests=1000)
