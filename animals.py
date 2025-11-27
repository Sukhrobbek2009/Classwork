class Animal:
    def __init__(self, name):
        self.name = name
        
    def is_animal(self, name):
        return isinstance(name, str)
    
class Dog(Animal):
    def bark(self):
        print("Dog say's woof")

class Cat(Animal):
    def meow(self):
        print("Cat say's meow")