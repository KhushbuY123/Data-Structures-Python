def longestSubstring(s):
    def findAround(s,left,right):
        max_len=0
        substring=""
        while left>=0 and right <len(s) and s[left]==s[right]:
            if max_len<right+1:
                max_len=right-left+1
                substring=s[left:right+1]
            left-=1
            right+=1
        return substring
    res=""
    for i in range(len(s)):
        odd=findAround(s,i,i)
        even=findAround(s,i,i+1)
        if len(odd)>len(res):
            res=odd
        if len(even)>len(res):
            res=even
    return res
s="happiapapp"
left=len(s)//2+1
right=len(s)//2+1
print(longestSubstring(s))
