s = "hello"
def reverseVowels(s):
        vowel=["a","e","i","o","u","A","E","I","O","U"]
        i=0;j=len(s)-1
        s=list(s)
        while(i<j):
            if(s[i] in vowel and s[j] in vowel):
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            elif(s[i] in vowel and s[j] not in vowel):
                j-=1
            else:
                i+=1
        return("".join(s))
print(reverseVowels(s))