index = 0

class Ship:
    def __init__(self, length, orientation, customIndex):
        global index

        self.length = length
        self.orientation = orientation
        self.destroyed = False

        # Ability to customly set index
        # Used for transforming shareable matrix to map matrix
        if(customIndex is None):
            self.index = index
            index += 1
        else:
            self.index = customIndex

    def getIndex(self):
        return self.index

    def getLength(self):
        return self.length

    def getOrientation(self):
        return self.orientation

    def destroy(self):
        self.destroyed = True

    def isDestroyed(self):
        return self.destroyed

class SmallShip(Ship):
    def __init__(self, orientation, index = None):
        super().__init__(1, orientation, index)
        
class MediumShip(Ship):
    def __init__(self, orientation, index = None):
        super().__init__(2, orientation, index)

class LargeShip(Ship):
    def __init__(self, orientation, index = None):
        super().__init__(3, orientation, index)
