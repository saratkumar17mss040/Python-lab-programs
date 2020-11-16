# method overriding  - 1
class Animal:
    def animalSound(self):
        print('Animal sound !!')
    
    def animalType(self):
        print('Carnivorous or Herbivorous or Omnivorous !!')


class Dog(Animal):
    def animalSound(self):
        print('Dog sound !!')


d = Dog()
d.animalSound()
d.animalType()


