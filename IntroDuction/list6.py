l=[2,5,9,4]
res=l[0]
if len(l)>0:
 for i in range(len(l)):
    if res<l[i]:
        res=l[i]
else:
   print("List is empty")
print(res)