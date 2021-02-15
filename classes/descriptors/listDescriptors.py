from classes.descriptors.percentColors import PercentColors
from classes.descriptors.pixelArrayResize import PixelArrayResize

def getAllDescriptors():
    return [
        PercentColors(),
        PixelArrayResize()
    ]