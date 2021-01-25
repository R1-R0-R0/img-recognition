from PIL import Image as Img;
import matplotlib.pyplot as plt
from pixel import Pixel;

class Image:

    def __init__(self, filename):
        print(filename);

        self.red, self.green, self.blue = [], [], [];

        img = Img.open(filename).convert('RGB');
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

    def create_histogram (self) :
        plt.hist([self.red, self.green, self.blue], color=["red", "green", "blue"])
        plt.savefig("hist.png");

    def get_colors_percents(self):
        percents = [0] * 3;

        for i in range(self.width):
            for j in range(self.height):
                pixel = self.get_pixel(i, j);
                percents[0] += pixel.red;
                percents[1] += pixel.green;
                percents[2] += pixel.blue;

        sum = percents[0] +  percents[1] + percents[2];
        percents[0] = percents[0] / sum
        percents[1] = percents[1] / sum
        percents[2] = percents[2] / sum
        return percents;
