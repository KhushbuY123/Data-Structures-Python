# def rev(x):
#     return x[::-1]
# l=rev("khushbu")
# print(l)
# ...................
# def rev(s):
#     new=""
#     for i in s:
#         new=i+new
#     return new
# s="khushbu"
# print(s)
# print(rev(s))
# ''''''''''''''''''''''''''
def rev(s):
    s="".join(reversed(s))
    return s
s="khushbu"
print(s)
print(rev(s))
