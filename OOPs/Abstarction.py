# Abstraction : It means hiding of un-relevent inforamtion and showing up the only relevent one to the user 

class Car():
    def __init__(self,clutch,brk,rik):
        self.cluth="false"
        self.brk="false"
        self.rik="false"
    def start(self):  # Here this information hides by the user 
        self.clutch="true"
        self.rik="true"
        print("Car Starts")
s1=Car(True,False,True)
s1.start()