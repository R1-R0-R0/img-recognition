from PIL import Image as Img;
import matplotlib.pyplot as plt
from pixel import Pixel;

class Image:

    def __init__(self, filename):
        self.red, self.green, self.blue = [], [], [];

        img = Img.open(filename);
        pix = img.load();
        size = img.size;
        self.width = size[0];
        self.height = size[1];

        for i in range(self.width):
            for j in range(self.height):
                pixel = pix[i, j]

                self.red.append(pixel[0]);
                self.green.append(pixel[1]);
                self.blue.append(pixel[2]);

    def get_pixel(self, x, y):
        i = (y * self.width + x);
        return Pixel(self.red[i], self.green[i], self.blue[i]);

    def createHistogram (self) :
        plt.hist([self.red, self.green, self.blue], color=["red", "green", "blue"])
        plt.title("orange.jpg");
        plt.savefig("hist.png");
