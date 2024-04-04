a=[2,4,5,3,6,1]
b=[2,4,5,1,56]
# for i in range(len(a)):
#     for j in range(len(b)):
#         if b[j] not in a:
#             a.append(b[j])
# print(a)
ans=[]
for i in range(len(a)):
    ans.append(a[i])
for i in range(len(b)):
    ans.append(b[i])
print(ans)
