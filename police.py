t=int(input())
police,unsolved=0,0
event=list(map(int,input().split()))
for e in event:
    if e==-1:
        if police>0:
            police=police-1
        else:
            unsolved+=1
    else: #assign no of police now present if no crime occur
        police+=e
print(unsolved)
    
