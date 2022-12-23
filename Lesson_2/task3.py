Yournumber=int(input("Enter a number: "))
print("Result: ")
while Yournumber>0:
    for row in range(-Yournumber, 0):
        print(-row,end=" ")
    print()
    Yournumber=Yournumber-1