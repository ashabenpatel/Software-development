# dictionaries
person = {"name": "Alice", "age": 30, "city": "New York"}
print(person["name"])  # Output: Alice
person["age"] = 31   # Update an existing value

# Accessing non-existent keys results in a keyError
# try:
#  print(person["country"])
# except keyError:
#  print("key 'country' not found")

# List
fruits = ["apple", "banana"' "orange"]
print(fruits[1])  # OUtput: banana (access by index)
fruits.append("mango")  # Add an item to the end
fruits.insert(1, "kiwi")  # Insert an item at specific index

# Lists can be interated over using a for loop
for fruit in fruits:
    print(fruit)

# Tuples:
coordinates = (10, 20)
# coordinates[0] = 15 (would cause a TypeError)
# Tuples can be unpacked into variables
x, y = coordinates
print(f"X: {x}, {y}

# Searching and sorting
if "apple" in fruits:
      print("apple found in the list")
apple_index= fruits.index("apple")
print(f"Apple is at index: {apple_index}")

# sorting
numbers= [3,1,4,5,2]
numbers.sort()  # sort in ascending order.
print(numbers)  

def calculate_linear_regression(x, y):
n = len(x)
sum_x = sum(x)
sum_y = sum(y)

# Corrected calculation for sum_xy
sum_xy = sum([x_i * x_i, y_i in zip(x, y)])

          

