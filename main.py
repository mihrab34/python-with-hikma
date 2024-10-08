# # Main Data Types
#
# firstname: str = "Rahmat"
# lastname = "Akintola"
#
# fullname = f"{firstname} Olajumoke {lastname}"  # string interpolation with f-strings
# print(fullname)
#
# price = 50
#
# print(f'{price} GHS')
#
# total = 30
# #
# prices = '50'
#
# print(int(prices) + total)  # type conversion
#
# print(total // 10)
#
# print(type(total))

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

# fruits = {"name": "orange", "quantity": 20, "status": False}
#
# fruits['name'] = "Apple"
# print(f" I have {fruits['quantity']} {fruits['name']}s")
# fruits.pop("status")
# print(fruits)

# Tuples

my_fruits = ('banana', 'apple', 'cherry')
post_ids = 12345, 54321, 'hello!'

print(my_fruits[1])
# nesting tuples
post_fruits = my_fruits, post_ids, (1, 2, 3, 4, 5)

print(post_fruits)  # (('banana', 'apple', 'cherry'), (12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
print(post_fruits[1][1])  # 54321



