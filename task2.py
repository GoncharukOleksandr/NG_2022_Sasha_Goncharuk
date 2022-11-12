import math
f_num = float(input("Введіть перше число>>"))
oper = input("Введіть операцію>>")
s_num = float(input("Введіть друге число>>"))
if oper == '+' :
  print(f_num + s_num)
elif oper == "-" :
  print(f_num - s_num)
elif oper == '*':
  print(f_num * s_num)
elif oper == '/':
  print(f_num / s_num)
elif oper == '^':
  print(math.pow(f_num, 2))
  print(math.pow(s_num, 2))
elif oper == 'sqrt':
  print(math.sqrt(f_num))
  print(math.sqrt(s_num))
elif oper == 'coren':
  print(math.pow(f_num, 1/s_num))
else:
  print("Error")
input()
