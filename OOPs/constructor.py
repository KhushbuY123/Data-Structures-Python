# All the classes have method __init__ which is called as constructor and it will be executed always .
# Syntex of constructor : def __init__(self) here self is the argument which is defualt , we can add postional arguemnts according to our preference in further

class Student():
    def __init__(self,fullname,totalmarks):
        self.name=fullname
        self.marks=totalmarks
s1=Student("khushbu yadav",90)
print(s1.name,s1.marks)