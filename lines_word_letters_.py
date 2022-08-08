f=open("words.txt","r")
lines=0
words=0
letters=0
for i in f:
    print(i)    
    letters+=len(i)
    b=i.split()
    words+=len(b)
    lines=lines+1
print("number of letter",letters)
print("number of word",words)
print("number of lines",lines)