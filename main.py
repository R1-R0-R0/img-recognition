from image import Image;
import ai;

img = Image("orange.jpg");
pixel = img.get_pixel(9, 0);

colors = img.get_colors_percents();

print(colors);

ai.PercentColorsAI();
