from classes.descriptor import Descriptor
from classes.utils.imgResizer import ImageResizer

class PixelArrayResize(Descriptor):

    def __init__(self, desiredSize = 100):
        self.resizer = ImageResizer(desizedSize)
        
    def getImageInfo(self, image):
        return self.resizer.resize(image.getPath())

    def getName(self):
        return 'PixelArrayResize'
