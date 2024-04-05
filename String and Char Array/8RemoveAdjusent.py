s="abbaca"
ans=[]
for i in s:
    if ans and ans[-1]==i:
        ans.pop()
        continue
    else:
        ans.append(i)
print("".join(ans))