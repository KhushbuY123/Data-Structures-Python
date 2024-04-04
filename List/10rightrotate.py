l = [40, 70, 50, 10, 50]

if len(l) <= 1:
    print(l)
else:
    print([l[-1]] + l[:-1])

