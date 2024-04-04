class Circle:
    def __init__(self,rad):
        self.rad=rad
    def Area(self):
        return(3.14*self.rad**2)
    def parameter(self):
        return(3.14*2*self.rad)
s1=Circle(5)
print(s1.Area())
print(s1.parameter())