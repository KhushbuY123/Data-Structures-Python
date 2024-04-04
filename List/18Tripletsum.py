# find 3 number in list whose addition equal to the sum
a=[10,20,30,40,50]
sum=80
for i in range(len(a)):
    one=a[i]
    for j in range(i+1,len(a)):
        two=a[j]
        for k in range(j+1,len(a)):
            if one+two+a[k]==sum:
                print(one,two,a[k])