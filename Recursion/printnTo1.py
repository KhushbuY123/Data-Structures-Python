def print_num(i,n):
    if n<=0:
        return 
    print_num(n-i,n)
    print(n-i)
print_num(0,10)