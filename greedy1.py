n=[1,2,3,3,2]
print(n)
max=0
max2=0
# for i in n:
#     if max<i:
#         max=i
# for l in n:
#    if l>max2 and l!=max:
#        max2=l
# print(max2)
for i in n:
    if i>max:
        max2=max
        max=i
    elif i>max2 and i!=max:
        max2=i
print(max2)
