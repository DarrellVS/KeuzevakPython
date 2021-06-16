from __car import *
from turtle import *
import time 

car1 = Car('brand1', 2, 20, 'red')
car2 = Car('brand2', 3, 25, 'blue')
deltaTime = 0.5

while True:
    car1.print()
    car2.print()
    time.sleep(deltaTime)
    car1.drive(deltaTime)
    car2.drive(deltaTime)