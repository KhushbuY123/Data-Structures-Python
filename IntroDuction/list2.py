def average(l):
    sum=0
    for i in l:
        sum=sum+i
    return sum//len(l)
l=list(map(int,input("Enter marks").split()))
print(l)
print(average(l))
