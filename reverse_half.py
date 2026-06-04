l=list(map(int,input().split()))
j=len(l)//2-1
for i in range(0,len(l)//4):
    temp=l[i]
    l[i]=l[j]
    l[j]=temp
    j-=1
print(l)
