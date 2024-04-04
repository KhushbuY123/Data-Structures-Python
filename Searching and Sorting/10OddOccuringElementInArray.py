l=[2,2,2,3,3,1,4,4,4,4,4]
dic={}
for num in l:
    if num in dic:
        dic[num]+=1
    else:
        dic[num]=1
for key , val in dic.items():
    if val%2!=0:
        print(key)
    else:
        print(-1)
    