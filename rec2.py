def reduceto1(n):
    if n==1:
        return 0
    elif n%2==0:
        return 1+reduceto1(n//2)
    else:
        return 1+min(reduceto1(n-1),reduceto1(n+1))
n=15
print(reduceto1(n))
     