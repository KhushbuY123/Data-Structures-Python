# Find Element in the given String................
def Find_Ele(s,n,i,k):
    if i>=n:
        return False
    if s[i]==k:
        print(i)
    return Find_Ele(s,n,i+1,k)
s="Khushbu"
k="u"
i=0
n=7
Find_Ele(s,n,i,k)