# inheritance - 2 - normal methods
class Person():

    def details(self):
        print("Can have information specific to the person")


class Student(Person):

    def details(self):
        super().details()
        print("Can have information specific to the student")


s = Student()
s.details()
