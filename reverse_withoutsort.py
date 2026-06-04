l=list(map(int,input().split()))
j=len(l)-1
for i in range(len(l)//2):
    temp=l[i]
    l[i]=l[j]
    l[j]=temp
    j-=1
print(l)