l=list(map(int,input().split()))
x=l[0]
y=l[1]
for i in range(len(l)-2):
    l[i]=l[i+2]
l[-1]=x
l[-2]=y
print(l)