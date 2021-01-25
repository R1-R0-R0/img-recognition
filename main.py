from image import Image;

img = Image("orange.jpg");
pixel = img.get_pixel(9, 0);

print(pixel.red);
print(img.width);
print(img.height);

img.createHistogram();
