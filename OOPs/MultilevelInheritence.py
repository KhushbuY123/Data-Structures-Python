class Car():
    @staticmethod
    def start():
        print("Start Car")
class CarMotion(Car):
    @staticmethod
    def stop():
        print("Stop the car")
class Marcedes(CarMotion):
    def __init__(self,name):
        self.name=name
s1=Marcedes("Toyota")
print(s1.name)
print(s1.start())
print(s1.stop())