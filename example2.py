# Step 1: Define the unsorted list
my_list = [64, 34, 25, 12, 22, 11, 90, 5]

# Step 2: Get the length of the list
n = len(my_list)
print("Unsorted array:", my_list)

# Step 3: Implement the Bubble Sort algorithm
for i in range(n-1):
    for j in range(n-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

# Step 4: Print the sorted array

print("Sorted array:", my_list)
