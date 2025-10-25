# CSV Module Basics

import csv

with open('csv_module.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    print(csv_reader) # <csv.reader object at 0x000001E2C4B3D700>
    
with open('csv_module.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    for line in csv_reader:
        print(line) # prints each line as a list of values

with open('csv_module.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line[2]) # prints the value in the third column for each row
        
with open('csv_module.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    next(csv_reader)
    
    for line in csv_reader:
        print(line[2]) # prints each line except the header
        

with open('csv_module.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='-')
        
        for line in csv_reader:
            print(line[2])
            
            
with open('csv_module.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')
        
        for line in csv_reader:
            csv_writer.writerow(line)