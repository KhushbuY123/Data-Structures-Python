# 1. Naive Approach 
# def isPrime(n):
#     if n<=1:return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# def CountPrime(n):
#     count=0
#     for i in range(2,n):
#         if isPrime(i):
#             count+=1
#     return count
# print(CountPrime(10))    # Time Limit Exceeded o(n)


# 2. Sqrt Approach
# import math
# def isPrime(n):
#     s=int(math.sqrt(n))
#     if n<=1:return False
#     for i in range(2,s+1):
#         if n%i==0:return False
#     return True
# def CountPime(n):
#     count=0
#     for i in range(0,n):
#         if isPrime(i):
#             count+=1
#     return count
# print(CountPime(10))   # Time Limit Exceeded 0(nrootn)
    