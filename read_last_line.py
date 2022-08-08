# Write a Python program to read last n lines of a file.
f=open("last.txt")
m=f.readlines()
line=int(input("enter last n line:"))
print(m[-line:])