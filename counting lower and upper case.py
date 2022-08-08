# f=open("case count","w")
# f.write("My name is themshingla.\nI love python.Python")
# f=open("case count","r")
# d=f.read().split("\n")
# i=0
# c=0
# c1=0
# while i<len(d):
#     j=0
#     while j<len(d[i]):
#         if d[i][j].isupper():
#             c=c+1
#         elif d[i][j].islower():
#             c1=c1+1
#         j=j+1
#     i=i+1
# print("upper case:",c,"lower case:",c1)
# f.close()

# def count(fname):
f=open("vowel_consonant.txt","r")
a=f.read()
print(a)
lower=0
upper=0
i=0
while i<len(a):
    if a[i].islower():
            lower+=1
    if a[i].isupper():
            upper+=1 
    i+=1
print("number of lower case",lower) 
print("number of upper case" ,upper)
# count("vowel_consonant.txt")