# You need to write a function that checks whether 
# if the number passed into it is a prime number or not.

# You need to write a function that checks whether 
# if the number passed into it is a prime number or not.

def prime_checker(number):
    if (number % number == 0) and (number % 1 == 0):
       for i in range(1, number + 1):
        if number % i == 0:
           break
           print("It's not a prime number.")
           
        else:
          print("It's a prime number.")
    else:
      print("It's not a prime number.")

  
    # else:
    #   print("It's not a prime number.")

import random
test_number = random.randint(1, 100)
print(f"Test number is: {test_number}")
prime_checker(number=test_number)