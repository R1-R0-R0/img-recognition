import cv2

class ImageResizer:
    
    def __init__(self, desiredSize):
        assert desiredSize >= 0 or desiredSize == -1
        self.desiredSize = desiredSize

    def cv2Resize(self, filename):
        srcImg = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
        if(self.desiredSize == -1):
            resizedImg = srcImg
        else:
            resizedImg = cv2.resize(srcImg, (self.desiredSize, self.desiredSize))

        return resizedImg

    def resize(self, filename):
        resizedImg = self.cv2Resize(filename)

        array = []
        for pixelLine in resizedImg:
            for pixel in pixelLine:
                array.append(pixel[0])
                array.append(pixel[1])
                array.append(pixel[2])

        return array