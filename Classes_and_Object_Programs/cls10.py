# encapsulation - private members - 2
class Person:
  def __init__(self):
    self.name = 'Sam'
    self.__lastname = 'son'

  def printName(self):
    return self.name + self.__lastname


p = Person()
print(p.name)
print(p.printName())
print(dir(p))
# name mangling
print(p._Person__lastname)
# error
print(p.__lastname)