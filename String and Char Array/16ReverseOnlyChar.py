s = "ab-cd"
def reverseOnlyLetters(s):
    i=0;j=len(s)-1
    s=list(s)
    while(i<j):
        if s[i].isalpha() and s[j].isalpha():
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        elif s[i].isalpha() and s[j].isalpha() ==False:
            j-=1
        elif s[i].isalpha()==False and s[j].isalpha():
            i+=1
        else:
            i+=1
            j-=1
    return ("".join(s))
print(reverseOnlyLetters(s))
        