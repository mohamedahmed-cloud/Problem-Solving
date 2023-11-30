# create the original list
original_list = [1, 2, 3, [4, 5]]

# create a shallow copy of the original list
shallow_copy = original_list.copy()

# modify the first element of the nested list in the shallow copy
shallow_copy[2] = 10

# check if the change affected the original list
print("Original list:", original_list) # Output: Original list: [1, 2, 3, [10, 5]]
