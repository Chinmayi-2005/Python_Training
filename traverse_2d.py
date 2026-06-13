
l=[[1,2,3],[2,7,8],[9,8,7]]
target=2
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j]==target:
            return True
return False
#last ele's index in a matrix i*j-1
# i=mid ele//com
# j=mid%col