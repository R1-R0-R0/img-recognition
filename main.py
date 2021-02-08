from image import Image;
import ai;
import os;

from sklearn.model_selection import train_test_split;
from sklearn.naive_bayes import GaussianNB;
import file_mgr as fm


tomAI = ai.HOGAi()

exit()


X, y = fm.loadDatas("Percent_AI")
sum = 0
for i in range(1000):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10);

    classifieur = GaussianNB();
    classifieur.fit(X_train, y_train);

    y_preditected = classifieur.predict(X_test);
    print("Real classes :");
    print(y_test);
    print("Predicted classes :");
    print(y_preditected);

    print("Score: ")
    score = classifieur.score(X_test, y_test)
    sum += score
    print(score)
    print()

print("Average score :")
print(sum / 1000)

exit()

images = []
mer = []
ailleurs = []
listMer = os.listdir('./Data/Mer')
listAilleurs = os.listdir('./Data/Ailleurs')

print("Loading images...")
for file in listMer:
    mer.append(Image("./Data/Mer/" + file))

for file in listAilleurs:
    ailleurs.append(Image("./Data/Ailleurs/" + file))

images.append(mer)
images.append(ailleurs)
print("Done.")

orange = Image("./orange.jpg");
sea = Image("./sea.jpg");

percentColorsAI = ai.PercentColorsAI()
percentColorsAI.fit(1, images)

print(orange.name + ": " + str(percentColorsAI.evaluate(orange)));
print(sea.name + ": " + str(percentColorsAI.evaluate(sea)));

percentColorsAI.save_data('Percent_AI');

percentColorsAIClone = ai.PercentColorsAI()
percentColorsAIClone.fit(0, "Percent_AI")
print(orange.name + ": " + str(percentColorsAIClone.evaluate(orange)));
print(sea.name + ": " + str(percentColorsAIClone.evaluate(sea)));
