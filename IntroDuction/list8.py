# l=[10,20,30]
# if len(l)==0:
#    print("yes")
# else:
#     if l==sorted(l):
#         print("yes")
#     else:
#         print("No")
def insort(l):
    i=1
    while(i<len(l)):
        if l[i]<l[i-1]:
            return False
        i=i+1
    return True
l=[20.50,40,40]
print(insort(l))