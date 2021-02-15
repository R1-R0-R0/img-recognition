from classes.descriptor import Descriptor

class ColorContrast(Descriptor):

    def __init__(self):
        #self.desiredSize = 100
        
    def getImageInfo(self, image):
        #return imgDescriptor(image.getPath(), desiredSize).getDescriptor()

    def getName(self):
        return 'ColorContrast'

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
