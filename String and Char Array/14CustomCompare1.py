# Sort the String in reverse order without using a function

s="129053"
new=sorted(list(s))
new=[new[i] for i in range(len(new)-1,-1,-1)]
print("".join(new))
    