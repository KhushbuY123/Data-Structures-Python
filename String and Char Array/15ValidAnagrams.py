s = "anagram";t = "nagaram"
def isAnagram(s, t):

    # First Approach

    # if len(s)!=len(t):
    #     return False
    # for i in set(s):
    #     if s.count(i)!=t.count(i):
    #         return False
    # return True

    # Second Approach

    # if sorted(s)==sorted(t):
    #     return True
    # else:
    #     return False

    # Third Approach
    dic={}  
    if len(s)!=len(t):
        print("False")
    for i in s:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for j in t:
        if j in dic:
            dic[j]-=1
        else:
            print("False")
    for i in dic:
        if dic[i]==0:
            print("True")
        else:
            print("False")
isAnagram(s,t)