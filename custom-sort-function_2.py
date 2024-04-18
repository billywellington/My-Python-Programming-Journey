'''Write a program that takes a list of strings and sorts them based on the length of each string. Create a custom sort function that calculates the length of a list and use it to sort the list.
'''

def myfunc(string):
    length = len(string)
    return length

strings = ['priscillaa', 'kaiy', 'aeiou', 'angelaa', 'billy', 'babooowethu']

strings.sort(key=myfunc)
print(strings)