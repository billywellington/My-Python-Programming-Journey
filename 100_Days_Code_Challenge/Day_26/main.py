# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# # print(new_list)
#
# new_list = [n * 2 for n in range(1, 5)]
# print(new_list)
#
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

new_names = [name.upper() for name in names if (len(name) > 5)]
print(new_names)