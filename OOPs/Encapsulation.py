# Encapsulation : It means wrapping up of the functions and methods , All the thing which we have done in OOPs is also encapsulation 


class Student():
    def __init__(self,fullname,rollno , subj):
        self.name=fullname
        self.roll_no=rollno 
        self.subj=subj
s1=Student("Khushbu Yadav",75,"DAA")
print(s1.name,s1.roll_no,s1.subj)