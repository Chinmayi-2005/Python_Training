# l=input().split()
# print(l)

# l.extend("a")
# print(l)

# l2=l
# l2.append("b") #becoz of refernce l and l2 on same obj
# print(l)
# l3=l.copy()
# (l3.extend("chinnu"))

l4=[1,2,3,4]
for i in l4:
    l4.remove(i)
print(l4)
l3=[1,2,3,4,5,6]
print(l3[5:0:-1])