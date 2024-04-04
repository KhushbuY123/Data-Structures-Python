l=[1,1,0,1,0,1,0,0]
# two pointer approach......................
# start=0
# end=len(l)-1
# i=0
# while(i!=end):
#     #left swap 
#     if l[i]==0:
#         l[i],l[start]=l[start],l[i]
#         i+=1
#         start+=1
#     # right swap
#     else:
#         l[i],l[end]=l[end],l[i]
#         end-=1
# print(l)


#.......................
count=0
for i in range(len(l)):
    if l[i]==1:
        l[i],l[count]=l[count],l[i]
        count+=1
print(l)

#.......................
# Using Function
# print(sorted(l))

