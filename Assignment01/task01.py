## Q1: Problem Statement: Write a program to solve this age-related riddle! Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
# Anton is 21 years old.
# Beth is 6 years older than Anton.
# Chen is 20 years older than Beth.
# Drew is as old as Chen's age plus Anton's age.
# Ethan is the same age as Chen.
# Your code should store each person's age to a variable and print their names and ages at the end.
# Anton is 3
# Beth is 4
# Chen is 5
# Drew is 6
# Ethan is 7 
 
# Assign ages based on the given information
anton_age : int = 21
beth_age : int = anton_age + 6
chen_age : int = beth_age + 20
drew_age : int = chen_age + anton_age
ethan_age : int = chen_age

# Print each person's name and age
print(f"Anton is {anton_age} years old.")
print(f"Beth is {beth_age} years old.")
print(f"Chen is {chen_age} years old.")
print(f"Drew is {drew_age} years old.")
print(f"Ethan is {ethan_age} years old.")

#==========================================================================================================================


# Q2: Formatted String Interpolation

# Task: Given the variables name, age, and city, use f-strings to construct a sentence that describes a person using these variables.
# name:str = "Alice"
# age:int = 30
# city:str = "New York"
# Instructions: Use an f-string to create a sentence in the format: "Alice is 30 years old and lives in New York."
# Expected Output:
# Alice is 30 years old and lives in New York.

name:str = "Alice"
age:int = 30
city:str = "New York"

print(f"{name} is {age} years old and lives in {city}.")

#==========================================================================================================================

# Q3: String Manipulation

# Task: Given the string s, use string methods to:
# Capitalize the first letter: make the first character uppercase and the rest of the string lowercase.
# Convert to uppercase: change all characters in the string to uppercase.
# Convert to lowercase: change all characters in the string to lowercase.
# s:str = "hElLo WoRlD"
# Expected Output:
# Hello world
# HELLO WORLD
# hello world

s:str = "hElLo WoRlD"

print(s.capitalize())
print(s.upper())
print(s.lower())

#==========================================================================================================================


# Q4: Substring Search

# Task: Given the string s, use string methods to:
# Find the index of "fox": get the starting index of the substring "fox". If "fox" is not found, it should return -1.
# Count occurrences of "the": Use the string's built-in method to count how many times the substring "the" appears in the string.
# s:str ="the quick brown fox jumps over the lazy dog"
# Expected Output:
# index of 'fox' is 16
# 'the' appears 2 times

s1:str ="the quick brown fox jumps over the lazy dog"

print(f"index of 'fox' is {s1.find('fox')}" )
print(f"'the' appears {s1.count('the')} times" )

#==========================================================================================================================

# Q5: String Replacement

# Task: Given the string s, use string methods to:
# Replace "Python" with "Java": substitute "Python" with "Java".
# s:str ="I love programming in Python"
# Expected Output:
# I love programming in Java

s2:str ="I love programming in Python"

print(s2.replace("Python","Java"))                    
#==========================================================================================================================

# Q6: String Splitting and Joining

# Task: Given the string s, use string methods to:
# Split into a list: break the string into a list of substrings based on the delimiter ,.
# Join with spaces: combine the list of substrings back into a single string, with each element separated by a space.
# s:str ="apple,banana,cherry,dates"
# Expected Output:
# ["apple", "banana", "cherry", "dates"]
# apple banana cherry dates

s3:str ="apple,banana,cherry,dates"

print(s3.split(","))
print(" ".join(s3.split(",")))

#==========================================================================================================================

# Q7: String Stripping and Justifying

# Task: Given the string s, use string methods to:
# Remove leading/trailing spaces: remove all leading and trailing whitespace characters from the string.
# Left justify with '*': left justify the string within a field of width 20, using * as the fill character.
# Right justify with '*': right justify the string within a field of width 20, using * as the fill character.
# s:str ="   Python is fun!   "
# Expected Output:
# Python is fun!
# Python is fun!*****
# *****Python is fun!

s4 : str = "   Python is fun!   "

# Remove leading/trailing spaces
stripped = s4.strip()
print(stripped)

# Left justify within a field of width 20 using '*'
left_justified = stripped.ljust(20, '*')
print(left_justified)

# Right justify within a field of width 20 using '*'
right_justified = stripped.rjust(20, '*')
print(right_justified)
#==========================================================================================================================

# Q8: Convert an integer to its binary representation

# Task: Given an integer num
# Obtain the binary representation of num
# num:int = 45
# Expected Output:
# Binary representation : 0b101101


num:int = 45

print(f"Binary representation : {bin(num)}") 

#==========================================================================================================================

# Q9: Calculate Powers of Numbers.

# Task: Given two integers base and exponent
# Compute base raised to the power of exponent.
# base:int = 3
# exponent:int = 4
# Expected Output:
# Power result: 81

base:int = 3
exponent:int = 4

print(f"Power result: {base**exponent}")

#==========================================================================================================================

# Q10: Round floating-point numbers

# Task: Given a floating-point number value
# Round value to the nearest integer.
# Round value to two decimal places.
# value:float = 12.34567
# Expected Output:
# Rounded to nearest integer: 12
# Rounded to two decimal places: 12.35

value:float = 12.34567

print(f"Rounded to nearest integer: {round(value)}")
print(f"Rounded to two decimal places: {round(value,2)}")
#==========================================================================================================================
