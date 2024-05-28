# How it works:

# Start with the two first Fibonacci numbers 0 and 1.
# Add the two previous numbers together to create a new Fibonacci number.
# Update the value of the two previous numbers.
# Do point a and b above 18 times.

# Start with the two first Fibonacci numbers 0 and 1.
x = 0
y = 1
i = 0

# Loop to generate Fibonacci numbers
while i < 18:
    # Add the two previous numbers together to create a new Fibonacci number.
    sum = x + y
    # Print the current Fibonacci number
    print(sum)
    # Update the value of the two previous numbers.
    x = y
    y = sum
    # Increment the counter
    i += 1


