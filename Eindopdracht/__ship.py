index = 0

class Ship:
    def __init__(self, length, orientation):
        global index

        self.length = length
        self.orientation = orientation
        self.index = index
        print(index)
        index += 1

    def getIndex(self):
        return self.index

    def getLength(self):
        return self.length

    def getOrientation(self):
        return self.orientation

class SmallShip(Ship):
    def __init__(self, orientation):
        super().__init__(1, orientation)
        
class MediumShip(Ship):
    def __init__(self, orientation):
        super().__init__(2, orientation)

class LargeShip(Ship):
    def __init__(self, orientation):
        super().__init__(3, orientation)
