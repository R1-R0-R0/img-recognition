from PIL import Image as Img;
import matplotlib.pyplot as plt
from pixel import Pixel;
from math import ceil
import classes.descriptors.listDescriptors as listDescriptors

class Image:

    def __init__(self, arg, mode = 0):
        if (mode == 0):
            self.init_with_filename(arg)
        elif(mode == 1):
            self.init_from_rgb(arg)
        else:
            print("Unknown mode")

    def init_with_filename(self, filename):
        self.name = filename;
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

    def init_from_rgb(self, rgbArray):
        self.red = rgbArray[0]
        self.green = rgbArray[1]
        self.blue = rgbArray[2]
        self.width = rgbArray[3]
        self.height = rgbArray[4]

    def get_pixel(self, x, y):
        i = (y * self.width + x);
        return Pixel(self.red[i], self.green[i], self.blue[i]);

    def create_histogram (self) :
        plt.hist([self.red, self.green, self.blue], color=["red", "green", "blue"])
        plt.savefig("hist.png");

    def getDescriptors(self):
        X = []
        descriptors = listDescriptors.getAllDescriptors()

        dico = dict()
        for descriptor in descriptors:
            dico[descriptor.getName()] = descriptor.getImageInfo(self)

        return dico

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

    def partition(self, minX, minY, maxX, maxY):
        assert minX <= maxX and minY <= maxY
        assert minX >= 0 and minY >= 0
        assert maxX <= self.width and maxY <= self.height

        r, g, b = [], [], []

        for i in range(minX, maxX+1):
            for j in range(minY, maxY+1):
                pixel = self.get_pixel(i, j)
                r.append(pixel.red)
                g.append(pixel.green)
                b.append(pixel.blue)

        return Image([r, g, b, maxX - minX +1, maxY - minY +1], 1)

    def fragmentation (self , horizontal , vertical) :
        assert 0 < horizontal and horizontal <= self.width and 0 < vertical and vertical <= self.height

        result = [None] * horizontal
        for i in range(horizontal) :
            result[i] = [None] * vertical

        deltaX = ceil(self.width / horizontal)
        deltaY = ceil(self.height / vertical)

        for x in range(horizontal) :
            for y in range(vertical) :

                minX = x * deltaX
                maxX = minX + deltaX - 1
                maxX = maxX if maxX < self.width else (self.width - 1)

                minY = y * deltaY
                maxY = minY + deltaY - 1
                maxY = maxY if maxY < self.height else (self.height - 1)

                result[x][y] = self.partition(minX,minY,maxX,maxY)

        return result

    def getPath(self):
        return self.name
