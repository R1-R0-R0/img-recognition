from classes.descriptor import Descriptor

class PercentColors(Descriptor):

    def __init__(self):
        pass

    def getImageInfo(self, image):
        return image.get_colors_percents()

    def getName(self):
        return 'PercentColors'

