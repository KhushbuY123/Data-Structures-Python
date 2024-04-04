class MyHash:
    def __init__(self,c):
        self.cap=c
        self.table=[-1]*c
        self.size=0
    def hash(self,x):
        return x%self.cap




