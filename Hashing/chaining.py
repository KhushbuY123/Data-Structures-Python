class Chaining:
    def __init__(self,b):
        self.Bucket=b
        self.table=[[] for i in range(b)]
    def insert(self,x):
        i=x%self.Bucket
        self.table[i].append(x)
        self.print_table()
    def remove(self,x):
        i=x%self.Bucket
        self.table[i].remove(x)
    def search(self,x):
        i=x%self.Bucket
        if x in self.table[i]:
            return x
        self.print_table()
    def print_table(self):
        for i in range(self.Bucket):
            print(f"Bucket{i}:{self.table[i]}")
hashtable=Chaining(10)
choice=input("Enter Your Choice eg. insert/search/delete:")
if choice=="insert":
    x=int(input("Enter a number:"))
    hashtable.insert(x)
elif choice=="delete":
    x=int(input("Enter a number:"))
    hashtable.delete(x)
elif choice=="search":
    x=int(input("Enter a number:"))
    result=hashtable.search(x)
    if result:
        print("present")
    else:
        print("not found")
else:
    print("Enter valid choice please")


