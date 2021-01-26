from image import Image;
import ai;


percentColorsAI = ai.PercentColorsAI();

orange = Image("./orange.jpg");
sea = Image("./sea.jpg");

print(orange.name + ": " + str(percentColorsAI.evaluate(orange)));
print(sea.name + ": " + str(percentColorsAI.evaluate(sea)));
