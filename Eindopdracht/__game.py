from __map import *
from __ship import *

class Game:
    def __init__(self, mapWidth, mapHeight, amountOfShips):
        self.mapWidth = mapWidth
        self.mapHeight = mapHeight
        self.amountOfShip = amountOfShips
        self.map = Map(mapWidth, mapHeight)