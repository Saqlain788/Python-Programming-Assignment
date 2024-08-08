# Q1: Add two numbers

# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# Prompt the user to enter the first number.
# Read the input and convert it to an integer.
# Prompt the user to enter the second number.
# Read the input and convert it to an integer.
# Calculate the sum of the two numbers.
# Print the total sum with an appropriate message.

num1 : int = int(input("Enter the first number: "))
num2 : int = int(input("Enter the second number: "))
sum = num1 + num2
print(f"The sum of {num1} and {num2} is {sum}.")

#==========================================================================================================================

# Q2: Agreement Boot
# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).
# Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):
# What's your favorite animal? cow
# My favorite animal is also cow!

animal : str = input("What's your favorite animal? ")
print(f"My favorite animal is also {animal}!")

#================================================================================================================================================================================================

# Q3: Fahrenheit to Celsius Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.
# The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!
# The equation you should use for converting from Fahrenheit to Celsius is the following:
# degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0
# (Note. The .0 after the 5 and 9 matters in the line above!!!)
# Here's a sample run of the program (user input is in bold italics):
# Enter temperature in Fahrenheit: 76

# Temperature: 76.0F = 24.444444444444443C

degree_Fahrenheit : float = float(input("Enter temperature in Fahrenheit: "))
degree_Celsius : float = (degree_Fahrenheit - 32) * 5.0/9.0
print(f"Temperature: {degree_Fahrenheit}F = {degree_Celsius}C")

#===============================================================================================
# Q4: Triangle Perimeters Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).
# Here's a sample run of the program (user input is in bold italics):
# What is the length of side 1? 3
# What is the length of side 2? 4
# What is the length of side 3? 5.5
# The perimeter of the triangle is 12.5

side1 : float = float(input("What is the length of side 1? "))
side2 : float = float(input("What is the length of side 2? "))
side3 : float = float(input("What is the length of side 3? "))
perimeter : float = side1 + side2 + side3
print(f"The perimeter of the triangle is {bold_italic_start}{perimeter}{bold_italic_end}.")

#===============================================================================================

# Q5: Square Number Ask the user for a number and print its square (the product of the number times itself).
# Here's a sample run of the program (user input is in bold italics):
# Type a number to see its square: 4
# 4.0 squared is 16.0

number : float = float(input("Type a number to see its square: "))
square : float = number * number
print(f"{number} squared is {square}.")

#===============================================================================================

# Q6: Delete a number Consider a list named numbers with the elements [1, 2, 3, 4, 5]. Use list method to delete the number 3?

numbers : list = [1, 2, 3, 4, 5]

numbers.remove(3)
print(numbers)

#===============================================================================================

# Q7: Creating a list You have two lists:
# list1 with elements [1, 2, 3]
# list2 with elements [4, 5, 6].
# Create a program using list method to add the elements of list2 to list1.

list1 : list = [1, 2, 3]
list2 : list = [4, 5, 6]

list1.extend(list2)
print(list1)
#===============================================================================================
# Q8: Pop method You have a list named items with the elements [10, 20, 30, 40]. If you use the pop method without any arguments, what will the list look like and what value will be removed?

items = [10, 20, 30, 40]

removed_item = items.pop()  # Removes the last element (40) and stores it

print(f"Removed item: {removed_item}")
print(f"List after pop: {items}")

#===============================================================================================
# Q9:Index Method You have a list called colors with the elements ['red', 'blue', 'green', 'yellow']. If you use the index method to find the position of 'green', what will the index be?

colors = ['red', 'blue', 'green', 'yellow']
green_index = colors.index('green')
print(f"The index of 'green' is: {green_index}")

#===============================================================================================
# Q10: Get last element Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.
def get_last_element(lst):
    print(lst[-1])

# Example usage
my_list = [1, 2, 3, 4, 5]
get_last_element(my_list)  # Output: 5


#===============================================================================================

# Q11: Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.
# Here's a sample run (user input is in blue):
# Enter a value: 1
# Enter a value: 2
# Enter a value: 3
# Enter a value:
# Here's the list: ['1', '2', '3']