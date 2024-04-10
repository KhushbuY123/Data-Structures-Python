order = "bcafg",
s = "abcd"

# output : abcd

# Problem is to find new str in reverse of s and all element of s sholud be present
dic={}
for i in s:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
res=""
for x in order:
    if x in s:
        res+=dic[x]*x
for y in s:
    if y not in res:
        res+=dic[y]*y
print(res)

