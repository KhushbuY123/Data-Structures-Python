name="Khushbu"
name1="Khushbu"
if name==name1:
    print("yes")
else:
    print("no")

# Another Approach
i=0
j=0
while(i<len(name) and j<len(name1)):
    if name[i]!=name1[j]:
        print("No")
        break
    else:
        i+=1
        j+=1
print("yes")