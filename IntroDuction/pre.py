l = ["jojo", "appendix", "jack", "john", "appillo", "radha", "appolo"]
p = "ap"

i = 0  

while i < len(l):
    if p not in l[i]:
        del l[i] 
    else:
        i += 1  
print(l)

