'''
Write a program that takes a list of strings and sorts them based on the number of vowels in each string. Create a custom sort function that counts the number of vowels in a string and use it to sort the list.
'''

def myfunc(string):
    count_a = string.count('a')
    count_e = string.count('e')
    count_i = string.count('i')
    count_o = string.count('o')
    count_u = string.count('u')
    count_all = count_a + count_e + count_i + count_o + count_u 
    return count_all

strings = ['priscillaa', 'kaiy', 'aeiou', 'angela', 'billy', 'babooowethu']

strings.sort(key=myfunc)
print(strings)

