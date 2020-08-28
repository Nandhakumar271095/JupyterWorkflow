import os

courses = ['History', 'Math', 'Physics', 'CompSci']


print(os.getcwd())















'''from my_module import find_index, test
import sys

courses = ['History', 'Math', 'Physics', 'compSci']

index = find_index(courses, 'Math')

# print(index)
# print(test)

print(sys.path)
'''




#Sets
'''cs_courses = {'history', 'Math', 'Pyhsics', 'CompSci'}

print(cs_courses)'''





'''# Immutable
tuple_1 = ['History', 'Math', 'Physics', 'CompSci']
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1.insert(0, 'art')

print(tuple_1)
print(tuple_2)'''


'''courses = ['python', 'javascipt', 'c', 'c++']

nums = [2, 1, 3, 7, 5, 4, 6]

for index, courses in enumerate(courses, start=1):
    print(index, courses)'''

'''#Sorted function in varible form

sorted_courses = sorted(courses)
sorted_nums = sorted(nums)

print(sum(nums))

print(sorted_courses)
'''



'''#Reverse: it provide the values in descending order

courses.sort(reverse=True)
nums.sort(reverse=True)

print(nums)

print(courses)'''


#Sort: It will provide the value in alphabetical order.
'''nums = [2, 1, 3, 7, 5, 4, 6]


courses.sort()
nums.sort()

print(nums)

print(courses)'''




#Reverse: it will provide the list in reverse

'''courses.reverse()
print(courses)'''












#Pop variable: it will revome the value and will provide the revomed value.
'''popped = courses.pop()

print(popped)
print(courses)'''






#Pop : Its removes the last value in the list
'''courses.pop()
print(courses)'''

#Revome: it remove the particular value in the list
'''courses.remove('c')
print(courses)
'''
















#Slicing
#print(courses[0:3])

#Append: i will insert the object in the list at last index
'''courses.append('DS')
print(courses)'''

#Insert: will insert the object at particular index
'''courses.insert(2,'DS')
print(courses)'''

#Extend: will insert the objects in a index
'''skills_in = ['DS', 'ML']
courses.extend(skills_in)
print(courses)'''