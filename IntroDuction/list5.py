l=[2,3,6,3,8]
d1={x:x**2 for x in l}
print(d1)
l1=[2,4,6,7]
l2=["a","b","c","d"]
res={l1[i]:l2[i] for i in range(len(l2))}
print(res)
d3=zip(l1,l2)
print(d3)
d4={101:"gfg",102:"practice",103:"ide"}
d5={v:k for (k,v) in d4.items()}
print(d5)