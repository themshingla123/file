# Write a Python program to write a list to a file
list=["them","salu","lan","heli"]
f=open("ring.txt","w")
i=0
while i<len(list):
    f.write(list[i])
    f.write("\n")
    i=i+1
# print(m)
f.close()
