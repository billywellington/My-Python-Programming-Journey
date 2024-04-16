#The correct syntax for using List Comprehensions
#newlist = [expression for item in iterable if condition == True]

numbers = [1, 2, 3, 4, 5, ]
squared_numbers = [x ** 2 for x in numbers if (x % 2 == 0)]
print(squared_numbers)