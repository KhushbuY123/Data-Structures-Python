def print_num(i,n):
    if (i>n):
        return
    print_num(i+1,n)
    print(i)
print_num(0,10)
