# Loops and Iterations in Python
# Loops are used to execute a block of code repeatedly until a certain condition is met.

nums = [1, 2, 3, 4, 5]

# For Loop
for num in nums:
    print(num)  # Output: 1 2 3 4 5 (each on a new line)
    

for num in nums:
    if num == 3:
        print("Found 3!")  # Output: Found 3!
        break  # Exit the loop when 3 is found
    print(num)  # Output: 1 2   
    

for num in nums:
    if num == 3:
        print("Found !")  # Output: Found 3!
        continue  # Skip the rest of the loop when 3 is found
    print(num) # Output: 1 2 4 5
    
    
for num in nums:
    for letter in 'abc':  # Nested loop
        print(num, letter)  # Output: 1 a 1 b 1 c 2 a 2 b 2 c 3 a 3 b 3 c 4 a 4 b 4 c 5 a 5 b 5 c
        
        
for i in range(10):  # Using range() function
    print(i)  # Output: 0 1 2 3 4 5 6 7 8 9 (each on a new line)
    
    
for i in range(1, 11): # Specifying start and end in range()
    print(i) # Output: 1 2 3 4 5 6 7 8 9 10 (each on a new line)
    
    
# While Loop

x = 0
while x < 10:
    print(x)
    x += 1  # Increment x by 1
    
x = 0
while True:
    if x == 5:
        break  # Exit the loop when x is 5
    print(x)
    x += 1  # Increment x by 1
    
while True: 
    if x == 5:
        break  # Exit the loop when x is 5
    print(x)
    x += 1  # Increment x by 1
    
    
while True:
    print(x)
    x += 1  # Increment x by 1