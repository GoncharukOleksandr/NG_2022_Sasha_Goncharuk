Yournumber=int(input("Введіть число: "))
print("Результат: ")
while Yournumber>0:
    for row in range(-Yournumber, 0):
        print(-row,end=" ")
    print()
    Yournumber=Yournumber-1