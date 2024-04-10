s="aaa"
def expandAroundIndex(s,i,j):
    count=0
    while(i>=0 and j<len(s) and s[i]==s[j]):
        count+=1
        i-=1
        j+=1
    return count
def countString(s):
    count=0
    for i in range(len(s)):
        # odd
        oddly=expandAroundIndex(s,i,i)
        count+=oddly
         # even
        evenly =expandAroundIndex(s,i,i+1)
        count+=evenly
    return count
print(countString(s))