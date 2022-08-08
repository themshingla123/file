f=open("data.txt","r")
print(f.tell())
print(f.read(3))
print(f.tell())
f.seek(0)
print(f.read(47))
print(f.tell())
f.close

# f=open("data.txt","r") 
# print(f.tell())
# f.close


# user1=int(input("enter the number1"))
# user2=int(input("enter the number2"))
# i=1
# sum=0
# while i<=user2:
#     a=user1*i
#     sum=sum+a
# if user1==0 or user1==-1:
#     print("invalid")
#     i=i+1
# print(sum)
