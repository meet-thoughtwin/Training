## Method Overiding = child class's method replace parent class's method

## parent and child class both have same method but we call child class,so priority goes to child class's method

## parent class
class Animal:

    def sound(self):
        return "Animal Sound"

    
## child class
class Dog(Animal):

    def sound(self):
        return "Bark"


d = Dog()

print(d.sound())