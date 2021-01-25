from PIL import Image as Img;
from pixel import Pixel;

class Image:
    def __init__(self, filename):
        self.r, self.g, self.b = [], [], [];

        img = Img.open(filename);
        pix = img.load();
        size = img.size;

        for i in range(size[0]):
            for j in range(size[1]):
                pixel = pix[i, j]

                self.r.append(pixel[0]);
                self.g.append(pixel[1]);
                self.b.append(pixel[2]);

    def get_pixel(self, x, y):
        return;

    def get_pixel(self, i):
        return Pixel(self.r[i], self.g[i], self.b[i]);
