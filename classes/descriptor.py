from abc import ABC, abstractmethod

class Descriptor(ABC):
    
    def getImageInfo(self, image):
        pass

    def getName(self):
        pass