Yourlist=input("Enter your list: ")
Lettercounts={}
uniqueletters=set(Yourlist)
for element in uniqueletters:
    Lettercounts[element]=Yourlist.count(element)
print("Your list: ")
print(Lettercounts)