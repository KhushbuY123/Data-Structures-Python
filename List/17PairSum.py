a=[1,3,5,7,2,4,6]
sum=9
res=[]
for i in range(len(a)):
    one=a[i]
    for j in range(i+1,len(a)):
        if one+a[j]==sum:
         print(one,a[j])