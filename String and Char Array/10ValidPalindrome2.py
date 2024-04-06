# Given a String s , return True if the s can be plaindrome after deleting at most one char from it.

s="abca"
def checkpalindrome(s,i,j):
    while(i<=j):
        if s[i]!=s[j]:
            return False
        else:
            i+=1
            j-=1
    return True
def validpalindrome(s):
    i=0
    j=len(s)-1
    while(i<=j):
        if s[i]!=s[j]:
            return checkpalindrome(s,i+1,j) or checkpalindrome(s,i,j-1)
        else:
            i+=1
            j-=1
    return True
print(validpalindrome(s))