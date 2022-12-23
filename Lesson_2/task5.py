YourNumbers=[]
YourNumbers=input("Введіть ваш номер: ")
YourNumbers=list(map(int,YourNumbers.split(",")))
YourNumbers.sort()
print(YourNumbers)
print(min(YourNumbers))
print(max(YourNumbers))
print(sum(YourNumbers[1: -1]))