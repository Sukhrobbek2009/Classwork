class Car:
    def __init__(self, brand, color, speed):
        self.brand = brand
        self.color = color
        self.speed = 0

    def acclerate(self):
        self.speed += 10
        print(f"The speed is {self.speed}")

    def brake(self):
        self.speed -= 10
        self.speed = 0
        print(f"The speed is {self.speed}")


car = Car()
            