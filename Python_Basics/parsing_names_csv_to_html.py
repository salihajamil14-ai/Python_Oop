# Parsinng names from a CSV file and converting to HTML

import csv

html_output = " "
names = []

with open("csv_module.csv", 'r') as data_file:
    csv_data = csv.reader(data_file)
    
    print(list(csv_data)) # Convert csv_reader to a list to print all rows at once
    
with open("csv_module.csv", 'r') as data_file:
    csv_data = csv.reader(data_file)
    
    next(csv_data)  # Skip header row
    next(csv_data)  # Skip second row if needed
    
    for line in csv_data:
        print(line)
        
with open("csv_module.csv", 'r') as data_file:
    csv_data = csv.reader(data_file)
    
    next(csv_data)  # Skip header row
    next(csv_data)  # Skip second row if needed
    
    for line in csv_data:
        names.append(f"{line[0]} {line[1]}")  # Assuming first column is first name and second is last name  
        
with open("csv_module.csv", 'r') as data_file:
    csv_data = csv.reader(data_file)
    
    next(csv_data)  # Skip header row
    next(csv_data)  # Skip second row if needed
    
    for line in csv_data:
        names.append(f"{line[0]} {line[1]}")  # Assuming first column is first name and second is last name  
        
for name in names:
    print(name)
    

with open("csv_module.csv", 'r') as data_file:
    csv_data = csv.reader(data_file)
    
    next(csv_data)  # Skip header row
    next(csv_data)  # Skip second row if needed
    
    for line in csv_data:
        if line[0] == 'No Reward':
            break
        names.append(f"{line[0]} {line[1]}")  # Assuming first column is first name and second is last name  
        
for name in names:
    print(name)
    
html_output += f'<p>There are currently {len(names)} names in the list.</p>'
print(html_output)