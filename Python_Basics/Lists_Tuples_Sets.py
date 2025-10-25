
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
print(len(courses))
print(courses[0])
print(courses[3])
print(courses[-1])
#print(courses[4])
print(courses[0:2])
print(courses[:2])
print(courses[2:])  
courses.append('Art')
print(courses)
courses.insert(0, 'Art')
print(courses)
courses_2 = ['Art', 'Education']    
courses.insert(0, courses_2)
print(courses)
print(courses[0])
courses.extend(['Biology', 'Chemistry'])
print(courses)
courses.remove('Math')
print(courses)  
courses.pop()
print(courses)
popped_course = courses.pop()
print(popped_course)
print(courses)
courses.reverse()
print(courses)
#courses.sort()
print(courses)
num = [1, 5, 2, 4, 3]
num.sort()
print(num)          
print(max(num))     
print(min(num))
print(sum(num))     
print(courses.index('CompSci'))
print('Art' in courses)         
print('Math' in courses)
for courses in courses:
    print(courses)
for index, course in enumerate(courses):
    print(index, course)            
courses_str = ', '.join(courses)
print(courses_str)
courses_str = ' - '.join(courses)
print(courses_str)      

new_list = courses_str.split(' - ')
print(new_list)

# Tuples
# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)


# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

#tuple_1[0] = 'Art'  # This will raise an error

print(tuple_1)
print(tuple_2)

# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses)
print('Math' in cs_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))       
print(cs_courses.union(art_courses))

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()