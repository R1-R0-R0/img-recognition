from image import Image;

img = Image("./Data/Mer/838s.jpg");
pixel = img.get_pixel(9, 0);

print(pixel.red);
print(img.width);
print(img.height);
