from classes.descriptors.percentColors import PercentColors
from classes.descriptors.pixelArrayResize import PixelArrayResize
from classes.descriptors.colorContrast import ColorContrast

def getAllDescriptors():
    return [
        PercentColors()
        # PixelArrayResize(),
        # ColorContrast()
    ]