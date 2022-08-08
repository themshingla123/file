f=open("shimla","r")
u=f.read().split()
i=0
max=u[i]
while i<len(u):
    if len(u[i])>len(max):
        max=u[i]
    i=i+1
print(max)
f.close()

