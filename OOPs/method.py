# Method: method is just a function which we pass in our class
# here Hello is the method
class Student():
    # class attibute : is created when it is comman for all
    college="Aith"
    def __init__(self,fullname):
        self.name=fullname
    def Hello(self):
        print("Hii there this is me ", s1.name)
s1=Student("Khushbu Yadav")
s1.Hello()
print(s1.name)
print(s1.college)