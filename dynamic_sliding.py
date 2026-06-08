k=int(input("enter the capacity : "))
num=list(map(int,input().split()))
# formula find to length upper-lower+1
r,l,m,sum=0,0,0,0
while(r<len(num)):
    sum+=num[r]
    while(sum>k):
        sum-=num[l]
        l+=1
    length=r-l+1
    m=max(m,length)
    r+=1
print(m)    

#  here r and l point to 0th index then r move until sum>k if sum>k we subtract ele of lth index from sum and move 1 point of l
# else
# we find length update maximum length   