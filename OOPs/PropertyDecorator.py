# property Decorator : We use this decorator pn any method in the class to use the method as a property 
class Student:
    def __init__(self,phy,hindi,math):
        self.phy=phy
        self.math=math 
        self.hindi=hindi
        # self.avg=str((self.phy+self.math+self.hindi)/3)+"%"
    @property
    def percentage(self):
        return str((self.phy+self.math+self.hindi)/3)+"%"

s1=Student(100,100,100)
print(s1.percentage)
s1.phy=70
print(s1.percentage)
