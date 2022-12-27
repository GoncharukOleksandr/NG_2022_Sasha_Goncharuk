first=0
second=0
act=0
result=0
def numbers():
    first=int(input("Your first number: "))
    second=int(input("Your first number: "))
    return [first,second]
def action():
    numberlist=numbers()
    act=str(input("Your first number: "))
    if act=='+':
        result=numberlist[0]-numberlist[1]
    if act=='-':
        result=numberlist[0]-numberlist[1]
    if act=='*':
        result=numberlist[0]-numberlist[1]
    if act=='/':
        result=numberlist[0]-numberlist[1]
    print(result)    