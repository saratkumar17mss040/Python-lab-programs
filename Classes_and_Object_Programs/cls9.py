# encapsulation - protected members - 1
class Person:

	def __init__(self):
		self._name = 'sam'


class Student(Person):

	def __init__(self):
		Person.__init__(self)
		print(self._name)


s = Student()
p = Person()



print(p._name)
print(s._name)

