# Polymorphism : many forms
#Here we use dunder function for addtion and other operation

class Num:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def print_num(self):
        print(self.real,"i +" ,self.img,"j ")
    def __add__(self,num2):  # this is dunder function
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Num(newReal,newImg)
s1=Num(5,6)
s2=Num(3,4)
s1.print_num()
s2.print_num()
# num3=s1.add(s2)
num3=s1+s2
num3.print_num()