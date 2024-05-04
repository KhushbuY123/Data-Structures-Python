def Find_Subsequences(s,i,output):
    if i>=len(s):
        return output

    # exclude 
    excluded=Find_Subsequences(s,i+1,output)
    
    # include
    output+=s[i]
    included=Find_Subsequences(s,i+1,output)

    return excluded+" "+included

s="abc"
i=0
output=''
v=[]
ans=Find_Subsequences(s,i,output)
print(ans)
