from classes.descriptor import Descriptor
from classes.utils.imgResizer import ImageResizer

class PixelArrayResize(Descriptor):

    def __init__(self, desiredSize):
        self.desiredSize = desiredSize
        self.resizer = ImageResizer(desiredSize)
        
    def getImageInfo(self, image):
        return self.resizer.resize(image.getPath())

    def getName(self):
        return 'PixelArrayResize:' + str(self.desiredSize)
