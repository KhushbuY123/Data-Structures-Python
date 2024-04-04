# Inheritance : Inheritence means acquiring the features of parent class to the child class 
# There are three types of Inheritence : 
# 1. Single -level
# 2.Mutiple 
# 3. Multilevel

class Car():
    def start(self):
        print('Start')
class Mersidese(Car):
    def __init__(self,name):
        self.name=name
s1=Mersidese("Toyota")
print(s1.name)
print(s1.start())
        
