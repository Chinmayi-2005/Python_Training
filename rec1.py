# def fun(n):
#         if n==0:
#             return n
#         print(n,end=" ")
#         fun(n-1)

# n=5
# fun(n)
# def fun(n):
#     if n==0:
#         return
#     fun(n-1)
#     print(n,end=" ")
    
# n=5
# fun(n) 
# 
# def fun(n):
#     if n==0:
#         return
#     fun(n-2)
#     print(n,end=" ")
# fun(10)
# def fun(n):
#     if n==0:
#         return
#     print(n,end=" ")
#     fun(n-2)
# fun(10)
# def fun(n):
#     if n==0:
#         return 1
#     print(n,end=" ")
#     fun(n-1)
#     if n<3:
#         print(n+1,end=" ")
# fun(3)

# def fun(n):
#     if n==0:
#         return 200
#     print(n,end=" ")
#     x=fun(n-1)
#     return x
# x=fun(5)
# print(x)
#output 5 4 3 2 1 200
# def fun(n):
#     if n==0:
#         return
#     if n%2==0:
#         print(n,end=" ")
#     fun(n-1)
#     if n%2==0 and n>2:
#         print(n,end=" ")
# fun(10)
def fun(n,m=0):
    if n==m:
        return
    print(m+1,end=" ")
    fun(n,m+1)
    if m>=1:
        print(m,end=" ")
fun(5)

