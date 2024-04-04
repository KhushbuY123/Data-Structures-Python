class A:
    varA="Wlcome to class A"
class B:
    varB="Welcome to class B"
class C(A,B):
    varC="Welcome to class C"
c1=C()
print(c1.varA)