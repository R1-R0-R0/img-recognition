from classes.descriptor import Descriptor

class PixelArrayAi(Descriptor):

    def __init__(self):
        self.desiredSize = 100
        
    def getImageInfo(self, image):
        return imgDescriptor(image, desiredSize).getDescriptor()

    def getName(self):
        return 'PixelArrayAi'

class imgDescriptor:

    def __init__(self,filename, desiredSize):
        self.desiredSize = desiredSize
        self.f = filename
        self.array = []
        self.srcImg = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
        if(desiredSize == -1):
            self.resizedImg = self.srcImg
        else:
            self.resizedImg = cv2.resize(self.srcImg, (desiredSize, desiredSize))
        for pixelLine in self.resizedImg:
            for pixel in pixelLine:
                self.array.append(pixel[0])
                self.array.append(pixel[1])
                self.array.append(pixel[2])
        self.descriptor = np.array(self.array)
        #print(self.descriptor)

    def getDescriptor(self):
        return self.descriptor

    def convertToJpg(self, path):
        image = cv2.imread(path)
        newPath = path[0:-3]+'jpg'
        if not(p.exists(newPath)):
            cv2.imwrite(newPath, image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
        return newPath

    def getHOG(self):
        path = self.f
        if (path[len(path) - 3:] == 'png'):
            path = self.convertToJpg(path)
            self.resizedImg = imgDescriptor(path,self.desiredSize).resizedImg
        print(path , len(self.resizedImg))
        img = self.resizedImg
        hog = cv2.HOGDescriptor("hog.xml")
        h = hog.compute(img)
        hog = []
        for i in h:
            hog.append(i[0])
        return np.array(hog)