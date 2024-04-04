# @static method : @static method is used where we want that the method must be private and ic couldn't accessible by parent other class .
# It is used where method doesn't use the instances and paramenters of the class
class Car():
    @staticmethod
    def start():
        return("start")
    @staticmethod
    def stop():
        return("stop")
s1=Car()
print(s1.start())
