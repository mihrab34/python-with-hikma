# # Main Data Types
#
# firstname: str = "Rahmat"
# lastname = "Akintola"
#
# fullname = f"{firstname} Olajumoke {lastname}"
# print(fullname)
#
# price = 50
#
# print(f'{price} GHS')
#
# total = 30
#
# prices = '50'
#
# print(int(prices) + total)
#
# print(total // 10)
#
# print(type(total))
from typing import List, Dict

# Lists
# names = ["sola", 89, True, {"message": "Form created"}]
#
# print(names)
#
# names[0] = "Hikma"
#
# names.append(24)
# names.pop()
# print(len(names))
# names.insert(3, "Demo")
# print(names)

# Dictionary

fruits = {"name": "orange", "quantity": 20, "status": False}

fruits['name'] = "Apple"
print(f" I have {fruits['quantity']} {fruits['name']}s")
fruits.pop("status")
fruit
print(fruits)


