# def fun():
#     print("GFg")
#     fun()
# fun()


#This cause an error maximum recursion depth bcoz of stack implementation here , So We have to correct this with given no of times
def fun(n):
    if n<0:
        return
    print("GFG")
    fun(n-1)
fun(5)  