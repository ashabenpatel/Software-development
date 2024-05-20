# portfolio- 3
# Activity-1
# List of even numbers up to 20
even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Display the first 3 elements from the list one by one
print("First 3 elements from the list:")
for i in range(3):
    print(even_numbers[i])

# Display all numbers in the list using the range function
print("\nAll numbers in the list:")
for num in even_numbers:
    print(num)

# Calculate the average of the even numbers in the list
average = sum(even_numbers) / len(even_numbers)
print("\nAverage of the even numbers in the list:", average)

# Activity- 2
# List of 5 numbers
numbers = [1, 2, 3, 4, 5]

# Print the first 3 elements from the list using slice expression
print("First 3 elements from the list using slice expression:", numbers[:3])

# Update the elements in the list to be times 2 of the previous value
numbers = [2 * num for num in numbers]

# Display the updated list
print("Updated list with each element multiplied by 2 of the previous value:", numbers)

# Display the minimum and maximum values in the list
print("Minimum value in the list:", min(numbers))
print("Maximum value in the list:", max(numbers))

# Activity- 3
# Define the initial lists
summer = ['Dec', 'Jan', 'Feb']
autumn = ['Mar', 'Apr', 'May']
winter = ['Jun', 'Jul', 'Jul', 'Aug']
spring = ['Oct', 'Nov']

# Remove excess month 'Jul' from the list 'winter'
winter.remove('Jul')

# Add month 'Sep' at the beginning of the 'spring' list
spring.insert(0, 'Sep')

# Make two new lists: MonthsISleep and MonthsIParty
MonthsISleep = summer[2:] + autumn + winter + spring[:-2]
MonthsIParty = spring[-2:]

# Display elements from both lists: MonthsISleep and MonthsIParty
print("Months I Sleep:", MonthsISleep)
print("Months I Party:", MonthsIParty)

# Display the elements of list 'summer' in reverse order
print("Summer months in reverse order:", summer[::-1]

# portfolio-1
# activity -1
# START
kilometers = float(input("Enter the distance in kilometers: "))
miles = kilometers * 0.621371
print("Equivalent distance in miles:", miles)
# END

# Activity-2
# START
radius = float(input("Enter the radius: "))  # Prompt the user to enter the radius
area = 3.14159 * radius ** 2  # Calculate the area using the formula π * radius^2
print("Area of the circle:", area)  # Display the calculated area
# END

# Activity-3
# START
# Prompt the user to enter the projected amount of total sales
total_sales = float(input("Enter the projected amount of total sales: "))

# Calculate the profit as 23% of the total sales
profit = 0.23 * total_sales

# Display the profit
print("The profit from the projected total sales is:", profit)
# END

# Activity- 4
#START
# Step 1: Prompt the user to enter the total square feet in the tract of land
total_square_feet = float(input("Enter the total square feet in the tract of land: "))

# Step 2: Calculate the number of acres in the tract
acres = total_square_feet / 43560

# Step 3: Display the calculated number of acres
print("The number of acres in the tract of land is:", acres)

#END
