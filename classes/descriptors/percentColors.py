from classes.descriptor import Descriptor

class PercentColors(Descriptor):

    def __init__(self):
        pass

    def getImageInfo(self, image):
        percents = [0] * 3

        for i in range(image.width):
            for j in range(image.height):
                pixel = image.get_pixel(i, j)
                percents[0] += pixel.red
                percents[1] += pixel.green
                percents[2] += pixel.blue

        sum = percents[0] +  percents[1] + percents[2]
        percents[0] = percents[0] / sum
        percents[1] = percents[1] / sum
        percents[2] = percents[2] / sum

        return percents

    def getName(self):
        return 'PercentColors'
