s=input()
c=1
s1=""
k=0
for i in range(1,len(s)):
    if s[k]==s[i]:
        c+=1
    else:
        s1+=s[i-1]+str(c)
        k=i
        c=1
s1+=s[-1]+str(c)
print(s1)






