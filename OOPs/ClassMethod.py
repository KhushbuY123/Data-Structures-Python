# Class Method : It is bound to the class & recieves the class as an implicit first argument
# Note: Static method can't access or modify class state & generally for utility

class Person:
    name="Khushbu"
    def changename(self,name):
        # self.name=name       #but i want to access global name 
        # Person.name=name    # One option is this
        self.__class__.name="rahul"  # Second Method
s1=Person()
s1.changename("Ram")
print(s1.name)
print(Person.name)

