# Write a Python program to count the frequency of words in a 
f=open("ching.txt","r")
c=f.read()
word=c.split()
user=input("enter the word:-")
i=0
count=0
while i<len(word):
    if word[i]==user:
        count=count+1
    i=i+1
print(count)
f.close()

i=1
while i<=5:
    j=1
    while j<=5:
        if j<=i:
            print(i,end="")
        else:
            print(j,end="")
        j=j+1
    i=i+1
    print()


