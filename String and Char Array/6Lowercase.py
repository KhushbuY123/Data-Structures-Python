name="KHuSHBU YADAV"
lower=""
for char in name:
    if 'A' <=char<="Z":
        lower+=chr(ord(char)-ord("A")+ord("a"))
    else:
        lower+=char
print(lower)        # TC : O(n)