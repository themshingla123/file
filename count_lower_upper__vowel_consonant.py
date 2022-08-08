def count(fname):
    f=open("vowel_consonant.txt","r")
    a=f.read()
    print(a)
    vowel=0
    consonant=0
    lower=0
    upper=0
    i=0
    while i<len(a):
        if a[i].islower():
            lower+=1
        if a[i].isupper():
            upper+=1
        if a[i] in("a","e","i","o","u","A","E","I","O","U"):
            vowel+=1
        elif a[i] in ("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"
                      "B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"):
           consonant+=1   
        else:
            pass
            
        i+=1
    print("number of lower case",lower) 
    print("number of upper case" ,upper)
    print("number of vowel",vowel)
    print("number of consonant",consonant)
count("vowel_consonant.txt")     