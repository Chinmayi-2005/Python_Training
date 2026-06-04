l=[1,2,2,4,6,5,5,8]
m,c=0,0
for i in l:
    if m<i:
        m=i
        c+=1
print(c)