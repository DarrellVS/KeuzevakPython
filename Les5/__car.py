class Car:
    def __init__(self, brand, acceleration, maxSpeed, color):
        self.brand = brand
        self.acceleration = acceleration
        self.maxSpeed = maxSpeed
        self.color = color
        self.position = 0
        self.speed = 0

    def drive(self, deltaTime):
        temp = self.acceleration * deltaTime
        if(self.speed + temp <= self.maxSpeed):
            self.speed += temp
        else:
            self.speed = self.maxSpeed
        self.position += self.speed * deltaTime

    def print(self):
        print(f"Im a {self.brand} with {self.acceleration} m/s^2 acceleration and {self.maxSpeed} m/s maxSpeed. Im going {self.speed} m/s and am located at {self.position}")

    def getColor(self):
        return self.color

    def getPosition(self):
        return self.position