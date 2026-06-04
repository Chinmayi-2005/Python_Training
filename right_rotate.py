l=list(map(int,input().split()))
x=l[-2]
y=l[-1]
for i in range(len(l)-1,-1,-1):
    l[i]=l[i-2]
l[0]=x
l[1]=y
print(l)
