class StudentDetails:

    # self can be anything - general class - 2
    def __init__(self,name, age, total):
        self.name = name
        self.age = age
        self.total = total
    
    def passOrFail(self):
        if self.total >= 35:
            return 'pass !'
        else:
            return 'Fail !'

    def printStudentDetails(self):
        print('Student details')
        print('Name:', self.name)
        print('Age:', self.age)
        print('Total:', self.total)
        print('Result:', self.passOrFail())
    

s1 = StudentDetails('Sam', 21, 45)
s2 = StudentDetails('Ram', 18, 25)
s1.printStudentDetails()
s2.printStudentDetails()


