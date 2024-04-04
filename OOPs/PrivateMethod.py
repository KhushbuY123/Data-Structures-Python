# Private method & attributes are meant to be used only within the class and are not allowed to accessible outside the class 

class Student():
    def __init__(self,name,dob):
        self.name=name
        self.__dob=dob  # Private Attribute
    def dob(self):
        print(s1.__dob)
s1=Student("Khushbu",10)
print(s1.name)
print(s1.dob())


