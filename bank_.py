# bank_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]

# a=open("bank.txt","w")
# i=0
# while i<len(bank_list):
#     a.write(bank_list[i])
#     a.write("\n")
#     i=i+1
# print(a)
# a.close()


a=["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
f=open("bank.txt","r")
d=f.read()
i=0
while i<len(a):
    i=i+1
print(d)
f.close()


