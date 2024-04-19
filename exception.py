try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Please enter a number to divide by: "))
    result = numerator / denominator

except ZeroDivisionError as error:
    print(error)
    print("You can't divide by zero you idiot!")

except ValueError as error:
    print(error)
    print("Please enter only numbers")

except Exception as error:
    print(error)
    print("Sorry! Something went wrong :(")
else:
    print(result)
finally:
    print("\nYou've reached the end. Bye bye!")