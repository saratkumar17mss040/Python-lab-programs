# method overriding  - 2
class Animal:
    def animalSound(self):
        print('Animal sound !!')

    def animalType(self):
        print('Carnivorous or Herbivorous or Omnivorous !!')


class Dog(Animal):
    def animalSound(self):
        super().animalSound()
        print('Dog sound !!')


d = Dog()
d.animalSound()
d.animalType()
