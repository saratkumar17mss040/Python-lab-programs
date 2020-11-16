# inheritance - 1 - constructor method
class Person:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

class Student(Person):

    def __init__(self, firstname, lastname, total):
        super().__init__(firstname, lastname)
        self.total = total

    def printStudentDetails(self):
        print('Student details')
        print('Firstname:', self.firstname)
        print('Lastname:', self.lastname)
        print('Total:', self.total)



s = Student("Sam", "Son", 400)
s.printStudentDetails()
