#Exercise 9 - Check if file is empty or not

import os

temp = os.stat('emptyFile.txt').st_size

if temp == 0:
    print("file is empty")
else:
    print("file has content")

#Exercise 10 - read line #4 from a file

with open ('test.txt', 'r') as fp:
    lines = fp.readlines()

#append all lines and return the 4th line
print(lines[3])

#PYTHON EXERCISES, if, else, for loops and range exercises

#Exercise 1 - Print first 10 natural numbers using a while loop

count = 0

while count < 10:
    print(count + 1)
    count += 1

#Exercise 2 - Print pyramid pattern

def pyramid(a):
    for i in range(0, a + 1):
        for j in range(0, i):
            print(j + 1, end =' ')
        print("\n")

#prints a pyramid lol
            

print(pyramid(5))

#Exercise 3 - Calculate the sum of all numbers from 1 to a given number

def summation(a):

    summ = 0
    for i in range(0, a + 1):
        summ += i

    return "sum of 0 to " + str(a) + " is " + str(summ)
print(summation(int(input("enter Number "))))




