Yourlist=input("Введіть ваш список: ")
Lettercounts={}
uniqueletters=set(Yourlist)
for element in uniqueletters:
    Lettercounts[element]=Yourlist.count(element)
print("Ваш список: ")
print(Lettercounts)