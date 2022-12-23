YourNumbers=[]
YourNumbers=input("Enter your number: ")
YourNumbers=list(map(int,YourNumbers.split(",")))
YourNumbers.sort()
print(YourNumbers)
print(min(YourNumbers))
print(max(YourNumbers))
print(sum(YourNumbers[1: -1]))