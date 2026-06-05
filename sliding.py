k=int(input("enter the capacity"))
l=list(map(int,input().split()))
s=sum(l[:k])
m=s
#m=0
# for i in range(len(l)-k):
#     sum=0
#     for j in range(i,i+k):
#         sum+=l[j]
#     m=max(m,sum)
# print(m)
for i in range(1,len(l)-k+1):
    s=s-l[i-1]+l[i+k-1]
    m=max(m,s)
print(m)
    

