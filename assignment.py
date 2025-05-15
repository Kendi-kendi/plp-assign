# Step 1: Create an empty list called my_list
my_list = []

# Step 2: Append elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After step 2:", my_list)

# Step 3: Insert 15 at the second position
my_list.insert(1, 15)
print("After step 3:", my_list)

# Step 4: Extend with another list
my_list.extend([50, 60, 70])
print("After step 4:", my_list)

# Step 5: Remove the last element
my_list.pop()
print("After step 5:", my_list)

# Step 6: Sort in ascending order
my_list.sort()
print("After step 6:", my_list)

# Step 7: Find and print the index of 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
