from collections import deque

# Create a deque
my_deque = deque([1, 2, 3, 4, 5])

# Find the index of the middle element
middle_index = len(my_deque) // 2

# Pop the element at the middle index
removed_element = my_deque.remove(middle_index)

# Print the updated deque
print("Removed element:", removed_element)
print("Updated deque:", my_deque)
