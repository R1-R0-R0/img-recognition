from classes.descriptors.percentColors import PercentColors
from classes.descriptors.pixelArrayAi import PixelArrayAi

def getAllDescriptors():
    return [
        PercentColors(),
        PixelArrayAi()
    ]