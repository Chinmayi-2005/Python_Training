l=[1,3,1,3,1,2,1,4,2,2,2,2]
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)

max=0
for key in d:
    if(d[key]>max):
        max=key
print(max)