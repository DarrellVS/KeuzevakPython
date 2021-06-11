from math import floor
from __ship import *

class Map:
    def __init__(self, sizes):
        self.width = sizes['mapGrid']['width']
        self.height = sizes['mapGrid']['height']
        self.sizes = sizes
        self.matrix = [ [ 0 for i in range(self.width) ] for j in range(self.height) ]
        self.destroyedShips = 0

    def placeShip(self, Ship, x, y):       
        # Validate if ship base is within map boundaries
        if(x < 0 or x > self.width or y < 0 or y > self.height): return False
         
        # Validate availability of space(s)
        if(Ship.orientation == 'east'):
            return self._placeShipEast(Ship, x, y)

        if(Ship.orientation == 'south'):
            return self._placeShipSouth(Ship, x, y)

    def _placeShipEast(self, Ship, x, y):
        # Validate if ship length is within map boundaries
        if(x + (Ship.getLength() - 1) > self.width): return False
        
        # Loop over the ship's length
        # and check if a ship already exists on said coordinates
        for i in range(Ship.getLength()):
            if(self.checkShipAt(x + i, y)): return False

        # Place ship in matrix
        for i in range(Ship.getLength()):
            self.matrix[y][x + i] = Ship

        return True

    def _placeShipSouth(self, Ship, x, y):
        # Validate if ship length is within map boundaries
        if(y + (Ship.getLength() - 1) > self.height): return False
        
        # Loop over the ship's length
        # and check if a ship already exists on said coordinates
        for i in range(Ship.getLength()):
            if(self.checkShipAt(x, y + i)): return False

        # Place ship in matrix
        for i in range(Ship.getLength()):
            self.matrix[y + i][x] = Ship

        return True

    def destroyShip(self, ship):
        for x in range(self.width):
            for y in range(self.height):

                # Get the current element
                element = self.matrix[y][x]

                # If the element is a ship
                if(isinstance(element, Ship)):

                    # If the index matches with the provided ship
                    if(element.getIndex() == ship.getIndex()):
                        element.destroy()
                        self.destroyedShips += 1

    def checkShipAt(self, x, y): 
        return isinstance(self.matrix[y][x], Ship)

    def getEntry(self, x, y):
        return self.matrix[y][x]

    def getCorrespondingMatrixIndex(self, x, y):
        return (
            floor(x / self.sizes['gridEntry']['width']),
            9 - floor(y / self.sizes['gridEntry']['height'])
        )

    def getMatrix(self):
        return self.matrix

    def getShareableMatrix(self):
        shareableMatrix = [ [ {} for i in range(self.width) ] for j in range(self.height) ]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                # If the current element in the matrix is a ship
                if(isinstance(self.matrix[i][j], Ship)):

                    # Get the length of the ship
                    ship = self.matrix[i][j]
                    shareableMatrix[i][j] = {
                        'index': ship.getIndex(),
                        'length': ship.getLength(),
                        'orientation': ship.getOrientation()
                    }

        return shareableMatrix;

    def getMatrixFromOpponentMap(self, opponentMatrix):
        # Create a new map to return
        m = Map(self.sizes)

        # Keep track of which idices have already been added
        passedIndices = []

        for i in range(len(opponentMatrix)):
            for j in range(len(opponentMatrix[i])):
                element = opponentMatrix[i][j]
                
                # If dict contains data and index has not yet been passed
                if(len(element) != 0 and not element['index'] in passedIndices):
                    length = element['length']
                    index = element['index']
                    orientation = element['orientation']
                    ship = SmallShip(orientation, index) if length == 1 else MediumShip(orientation, index) if length == 2 else LargeShip(orientation, index)
                    m.placeShip(ship, j, i);
                    passedIndices.insert(0, index)

        return m

    def getAmountOfDestroyedShips(self):
        return self.destroyedShips

    def print(self):
        for i in self.matrix:
            for j in i:
                if(isinstance(j, Ship)):
                    print(j.isDestroyed(), end = ' ')

                else:
                    print('_', end = ' ')
            print()