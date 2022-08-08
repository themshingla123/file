# Write a Python program to get the file size of a plain file
  
f=open("size.txt","r")
m=f.read()
count=0
i=0
while i<len(m):
    count+=1
    i=i+1
print(count)
f.close()

# f=open("size.txt","r")
# print(f.read())
# print(f.tell())

# import os
# print(os.path.getsize("size.txt"))