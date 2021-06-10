class Ship:
    def __init__(self, length, orientation):
        self.length = length
        self.orientation = orientation
        print('New ship initiated')

class SmallShip(Ship):
    def __init__(self, orientation):
        super().__init__(1, orientation)

    def getLength(self):
        return self.length
        
class MediumShip(Ship):
    def __init__(self, orientation):
        super().__init__(2, orientation)

    def getLength(self):
        return self.length

class LargeShip(Ship):
    def __init__(self, orientation):
        super().__init__(3, orientation)

    def getLength(self):
        return self.length