#Exercise 6 - Recursive Function to calculate the sum of numbers from 0 --> 10

def recurSum(num):
    if num == 0:    
        return num
    else:
        return num + recurSum(num - 1)

#print(recurSum(10))

#Exercise 7 - Assign a different name to function and call it through new name

def display_student(name, age):
    print(name, age)

show_student = display_student
#function aliasing

#show_student("Emma", 26)

#Exercise 8 - generate a python list of every even number from 4 to 30

def list_gen():
    gen = []
    for i in range (4, 32, 2):
        gen.append(i)
    return gen

#print(listGen())

#Exercise 9 - Find the largest item from a given list

def largest_item(arr):
    largest = 0
    for i in arr:
        if i > largest:
            largest = i
    return "Largest item: " + str(largest)

x = [4, 6, 8, 24, 12, 2]
print(largest_item(x))
