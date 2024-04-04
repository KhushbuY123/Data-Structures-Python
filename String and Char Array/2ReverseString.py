name="Khushbu Yadav"

# first approach
print(name[::-1])

# second approach
print(reversed(name))

# Third Approach
s=""
for i in name:
    s=i+s
print(s)