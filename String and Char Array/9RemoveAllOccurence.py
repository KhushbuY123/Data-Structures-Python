part="abc"
s = "daabcbaabcbc"

# First Approach

while part in s:
    s=s.replace(part,"",1)
print(s)

# Second Approach

n=len(part)
while True:
    for i in range(len(s)-n+1):
        if s[i:i+n]==part:
            s=s[:i]+s[i+n:]
            break
    if part not in s:
        print(s)