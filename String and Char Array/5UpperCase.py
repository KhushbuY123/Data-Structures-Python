name="Khushbu Yadav"

#First Approach
print(name.upper())
print(name.capitalize())
print(name.casefold())

# Second Approach  
upper="" 
for char in name:
    if 'a' <=char <='z':
        upper+=chr(ord(char)-ord('a')+ord('A'))
    else:
        upper+=char
print(upper)

