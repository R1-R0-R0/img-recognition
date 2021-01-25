from image import Image;

img = Image("orange.jpg");
pixel = img.get_pixel(9, 0);

colors = img.colors_percents();

print(colors);
