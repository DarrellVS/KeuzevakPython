from __map import *
from __ship import *

map = Map(20, 10)
ship = LargeShip('south')

map.placeShip(ship, 0, 0)

map.print();

map.destroyShip(ship)

print();

map.print()