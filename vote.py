n=5
age=[17,21,18,80,45]
vote=[1,3,2,3,2]
c=[0]*(max(vote))
for i in range(n):
    if age[i]>=18:
        c[vote[i]-1]+=1
print(c)
m=max(c)
print(m)
print(c.index(m)+1)
temp=sorted(c,reverse=True) #copy a list in reverse order another list 
if temp[0]==temp[1]:
    print(-1)
else:
    print(1)
# for i in range(n):
#     if age[i]<18:
#         vote.pop(i)
# d={}
# res=[]
# for i in vote:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)
# max=0
# for key in d:
#     if d[key]>=max:
#         max=d[key]
#         res.append(max)
# print(res)
# if len(res)>1:
#     print(-1)
# else:
#     print(1)