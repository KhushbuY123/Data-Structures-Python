from sys import maxsize

def Cut_Seg(n, x, y, z):
    if n == 0:
        return 0
    if n < 0:
        return -maxsize
    a = Cut_Seg(n - x, x, y, z) + 1
    b = Cut_Seg(n - y, x, y, z) + 1
    c = Cut_Seg(n - z, x, y, z) + 1
    ans = max(a, max(b, c))
    return ans if ans >= 0 else 0

n = 7
x = 5
y = 2
z = 2
ans = Cut_Seg(n, x, y, z)
print(ans)

