from classes.descriptor import Descriptor

class PixelArrayAi(Descriptor):

    def __init__(self):
        pass

    def getImageInfo(self, image):
        return image.get_colors_percents()

    def getName(self):
        return 'PixelArrayAi'

