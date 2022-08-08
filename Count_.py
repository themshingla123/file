f=open("name.txt","r")
m=f.readlines()
i=0
count=0
while i<len(m):
    count+=1
    i=i+1
print(count)
f.close() 



