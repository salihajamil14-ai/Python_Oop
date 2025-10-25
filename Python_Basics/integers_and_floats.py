# Integers

num = 3
print(type(num))

# Floats

num = 3.14
print(type(num))

# Arithemetic Operators:
# Addition (+)
# Subtraction (-)
# Multiplication (*)
# Division (/)
# Floor Division (//)
# Modulus (%)
# Exponentiation (**)

print(3 + 2)      # Addition output: 5
print(3 - 2)      # Subtraction output: 1
print(3 * 2)      # Multiplication output: 6
print(3 / 2)      # Division output: 1.5
print(3 // 2)     # Floor Division  output: 1
print(3 % 2)      # Modulus output: 1
print(3 ** 2)     # Exponentiation output: 9

print(3 * 2 + 1)  # Combination of operations output: 7
print(3 * (2 + 1)) # Using parentheses to change order of operations output: 9



num = 1
num = num + 1 # Incrementing by 1
print(num)  # Output: 2

num += 1      # Shorthand for incrementing by 1
print(num)  # Output: 3
num += 10   # Shorthand for incrementing by 10
print(num)  # Output: 13

print(abs(-3))  # Absolute value output: 3
print(round(3.75))  # Rounding output: 4
print(round(3.75, 1)) # Rounding to 1 decimal place output: 3.8

# Comparisons:
# Equal:              3 == 2
# Not Equal:         3 != 2
# Greater Than:      3 > 2
# Less Than:         3 < 2
# Greater or Equal:  3 >= 2
# Less or Equal:     3 <= 2

num_1 = 3
num_2 = 2
print(num_1 == num_2)  # Equal output: False
print(num_1 != num_2)  # Not Equal output: True
print(num_1 > num_2)   # Greater Than output: True
print(num_1 < num_2)   # Less Than output: False
print(num_1 >= num_2)  # Greater or Equal output: True
print(num_1 <= num_2)  # Less or Equal output: False

num_1 = '100' # string
num_2 = '200' # string

print(num_1 + num_2)  # String concatenation output: '100200'

num_1 = int(num_1)  # Convert to integer
num_2 = int(num_2)  # Convert to integer

print(num_1 + num_2)  # Integer addition output: 300