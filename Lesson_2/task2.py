from collections import OrderedDict


my_list = ["VAG", "Mercedes", "BMW", "VAG", "Audi", "Wolkswagen", "Skoda", "Bentley"]
print("The original list: " + str(my_list))

li = list(OrderedDict.fromkeys(my_list))
print("List after removing duplicates: " + str(li))