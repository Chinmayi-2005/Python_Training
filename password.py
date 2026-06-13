p=input("enter the password : ")
c1,c2,c3,c4=0,0,0,0
i=0
for i in p:
    if i.isalnum():
        c1+=1
    if i in ["_","@","#","$"]:
        c2+=1
    if i.isupper():
        c3+=1
    if i.islower():
        c4+=1

if c1>=1 and c2>=1 and c3>=1 and c4>=1 and len(p)>8:
    print("valid")
else:
    print("invalid")

