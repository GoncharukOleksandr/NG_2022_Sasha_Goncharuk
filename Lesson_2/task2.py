from collections import OrderedDict


my_list = ["VAG", "Mercedes", "BMW", "VAG", "Audi", "Wolkswagen", "Skoda", "Bentley"]
print("Оригінальний список: " + str(my_list))

li = list(OrderedDict.fromkeys(my_list))
print("Список після видалення дублікатів: " + str(li))