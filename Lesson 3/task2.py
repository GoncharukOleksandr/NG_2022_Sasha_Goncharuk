print("Firstly you should write your list")
result=0
list=input("Enter your list: ")
def youractions():
    action=input("Enter your list: ")
    if action=='1':
        result=set(list)
        print(result)
    if action=='2':
        result={}
        count=set(list)
        for element in count:
            result[element]=list.count(element)
        print(result)
    if action=='3.1':
        vowels={'a','e','i','o','u','y'}
        for letters in list:
         if letters in vowels:
            print(letters)
    if action=='3.2':
         vowels={'a','e','i','o','u','y'}        
         result=set(list)-set(vowels)
         print(result)       
    if action=='4':
        Yourlist=list.split(" ")
        result=Yourlist[::-1]
        print(result)
    if action=='5':
        i=0
        Yourlist2=list.split(" ")
        for element in Yourlist2: 
                 i=i+1
                 print(element+" This number: "+str(i))
    if action=='6':
        list2=(input("Enter your new list: "))
    if action=='7':
        SystemExit
    else:
        print("Error")                     