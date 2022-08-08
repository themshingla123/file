list="my name is katimla"
l2=[]
i=0
while i<len(list):
    if list[i] not in l2 and list[i]!=" ":
        l2.append(list[i])
    i+=1
i=0
d=[]
while i<len(l2):
    j=0
    c=0
    while j<len(list):
        if l2[i]==list[j]:
            c+=1
        a=l2[i],c
        j+=1 
    d.append(a)
    i+=1
print(d)