from __ship import *

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = [ [ 0 for i in range(width) ] for j in range(height) ]

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

        return True;

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

        return True;

    def destroyShip(self, Ship):
        for x in range(self.width):
            for y in range(self.height):
                if(self.matrix[y][x] is not 0): self.matrix[y][x] = 0 

    def checkShipAt(self, x, y): 
        return isinstance(self.matrix[y][x], Ship)

    def print(self):
        for i in self.matrix:
            for j in i:
                if(isinstance(j, Ship)):
                    print(j.getLength(), end = ' ')

                else:
                    print(j, end = ' ')

            print()