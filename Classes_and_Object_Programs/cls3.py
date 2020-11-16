class Student:

  # object as argument - 1
  def student_details(self,obj):
    print("Name:", obj.name)
    print("Age:", obj.age)


class StudentDetail:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def printStudentDetails(self):
    print('Student details')
    print("Name:", self.name)
    print("Age:", self.age)
    s1 = Student()
    s1.student_details(self)


sd = StudentDetail('Sam', 21)
sd.printStudentDetails()
