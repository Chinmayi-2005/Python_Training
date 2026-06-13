k=int(input("enter the num of rotation"))
l=list(map(int,input().split()))
n=len(l)
k=k%n
def rotate(i,j):
    while(i<j):
        l[i],l[j]=l[j],l[i]
        i=i+1
        j=j-1
rotate(0,k-1)
rotate(k,n-1)
rotate(0,n-1)
print(l)




# res=[]
# rem=k%len(l)
# res=l[0:rem]
# res.reverse()
# res1=l[rem:len(l)]
# res1.reverse()
# l1=res+res1
# l1.reverse()
# print(l1) 


    