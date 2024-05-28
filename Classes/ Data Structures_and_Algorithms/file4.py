# Create a variable 'minVal' and set it equal to the first value of the array.
# Go through every element in the array.
# If the current element has a lower value than 'minVal', update 'minVal' to this value.
# After looking at all the elements in the array, the 'minVal' variable now contains the lowest value.

my_array = [73,12,9,11,39]

minVal = my_array[0]
for i in my_array:
    if i < minVal:
        minVal = i

print(f"Minimum value is {minVal}")
