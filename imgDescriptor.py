import cv2
import image
import numpy as np
import pixel as px

class imgDescriptor:
    def __init__(self,filename, desiredSize):
        self.array = []
        srcImg = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
        resizedImg = cv2.resize(srcImg,(desiredSize,desiredSize))
        for pixelLine in resizedImg:
            for pixel in pixelLine:
                #print(pixel,'tamere')
                colors = [pixel[0],pixel[1],pixel[2]]
                self.array.append(pixel[0])
                self.array.append(pixel[1])
                self.array.append(pixel[2])
        self.descriptor = np.array(self.array)
        print(self.descriptor)

    def getDescriptor(self):
        return self.descriptor

#example
#img = imgDescriptor('./orange.jpg',10)