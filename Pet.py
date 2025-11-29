class Pet:
    def __init__(self, name, animal_type, hunger, energy):
        self.name = name
        self.animal_type = animal_type
        self.hunger = hunger
        self.energy = energy

    def feed(self, amount):
        self.hunger -= amount
        if self.hunger < 0:
            self.hunger = 0
            print(f"You need fed {self.name}. You're hunger is {self.hunger}")

    def play(self, minutes):
        self.energy = self.energy - minutes * 2
        if self.energy < 0:
            self.energy = 0
            print(f"{self.name} you played for {minutes} minutes. Energy: {self.energy}. Hunger: {self.hunger} ")


    def rest(self, minutes):
        self.energy = self.energy + minutes + 5
        if self.energy > 100:
            print("Warning it can't be more than 100")
            self.energy = 100