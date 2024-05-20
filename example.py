# Define the unsorted list: Start by defining an unsorted list of numbers.
# You can choose any list of numbers to sort.

my_list = [64, 34, 25, 12, 22, 11, 90, 5]

# Get the length of the list: Determine the length of the list to use it in loops later.
# Use the len() function to get the length of the list and store it in a variable.

n = len(my_list)
# print(list_length)


# Implement the Bubble Sort algorithm:
#
# Use nested loops to iterate over the list and compare adjacent elements.

# In the outer loop, iterate from 0 to n-1.
# In the inner loop, iterate from 0 to n-i-1, where i is the index of the outer loop.

print("Unsorted array:", my_list)


for i in range(n - 1):
    for j in range(n - i - 1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] =  my_list[j+1], my_list[j]

print("Sorted array:", my_list)
# Compare each element with its adjacent element.
# If the current element is greater than its adjacent element, swap them.
# Continue this process until the end of the list.

# Print the sorted array: After completing the sorting process, print the sorted array.
#
# Test the program: Run the program and verify that it correctly sorts the list of numbers in ascending order.