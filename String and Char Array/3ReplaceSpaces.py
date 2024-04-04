name="Khushbu Yadav"
name_l=list(name)
for i in range(len(name_l)):
    if name_l[i]==" ":
        name_l[i]="@"
name="".join(name_l)
print(name)