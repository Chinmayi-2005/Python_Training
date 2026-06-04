# in this pgm we can only use 1 sort 1 temp list . here we need if element is odd it is in ascending order and even no in descending order and first even no then odd
l=[6,2,1,4,3,7,5] 
l.sort()
res=[]
for i in l:
    if i%2!=0:
        res.append(i)
    else:
        res.insert(0,i)
print(res)