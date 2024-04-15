'''Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
'''

fruits = ['apple', 'banana', 'blueberry', 'peaches', 'lemon', 'Plum']
fruits_with_a = []
for x in fruits:
    if "a" in x:
        fruits_with_a.append(x)

print(fruits_with_a)