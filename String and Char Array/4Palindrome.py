# Frist Appraoch
name="Khushbu"
if name==name[::-1]:
    print("This is palindrome")
else:
    print("Not a Palidrome")

# Second Approach
name1="BABAB"
i=0
j=len(name1)-1
while(i<=j):
    if (name1[i]!=name1[j]):
        print("Not Palindrome")
        break
    else:
        i+=1
        j-=1
print("Palindrome")   # TC - O(n)