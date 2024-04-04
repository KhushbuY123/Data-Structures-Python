class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("start")
class Toyotacar(Car):
    def __init__(self, name,type):
        self.name=name
        super().__init__(type)  # Super method : It is used to access parent class in child class
s1=Toyotacar("pirus","Deisel")
print(s1.name,s1.type)