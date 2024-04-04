# Define a Employee class with parameters role , departments , & salary .This class also have showdetails() method. 
# Crate an Engineer class that inherits properties from employee & has additional attributes : name & age
class Employee:
    def __init__(self,role,dep,sal):
        self.role=role
        self.dep=dep
        self.sal=sal
    def show_details(self):
        return(self.role,self.dep,self.sal)
class Engineer(Employee):
    def __init__(self, role, dep, sal,name,age):
        self.name=name
        self.age=age
        super().__init__(role, dep, sal)

s1=Engineer("Web Developer", "CSE",70000,"khushbu",24)
print(s1.show_details())
print(s1.name)
