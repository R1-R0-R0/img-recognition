from abc import ABC, abstractmethod

class Descriptor(ABC):
    
    # Retourne le tableau X
    def getImageInfo(self, image):
        pass

    def getName(self):
        pass