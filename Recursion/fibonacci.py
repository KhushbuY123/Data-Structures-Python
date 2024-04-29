def fibonacci(i):
    if i<0:
        print("Incorrect input")
    elif i==0:
        return 0
    elif i==1 or i==2:
        return 1
    else:
        return fibonacci(i-1)+fibonacci(i-2)  
for i in range(9):
    print(fibonacci(i),end=", ")
