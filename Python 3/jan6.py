#Exercise 9 - Write a program to check if a given number is a palindrome

def palindrome(x):
    y = str(x)
    
    z = y[::-1] 

    if (y == z):
        print("Yes, given number is a Palindrome")
    else:
        print("No, given number is not a palindrome")

#x = int(input("Enter Number: "))
#palindrome(x)


#Exercise 10 - given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list


def oddEvenList(x, y):

    mergeList = []

    for i in x:
        if (i % 2 != 0):
            mergeList.append(i)
    for i in y:
        if (i % 2 == 0):
            mergeList.append(i)
    
    return mergeList

oddList = [10, 20, 25, 30, 35]
evenList = [40, 45, 60, 75, 90]

#print(oddEvenList(oddList, evenList))


#testing array input.... works!

#y = []

#for i in range (1, 5):
#    x = int(input("enter number: "))
#    y.append(x)

#print(y)

#Exercise 11 - Write a program to extract each digit from an integer in the reverse order

def reversal(x):
    a = str(x)
    
    b = a[::-1] 
    
    c = ""
    for i in b:
        i = i + " "
        c = c + i
    return c

#y = int(input("Enter number: "))
#print(reversal(y))

#Exercise 12 - Calculate income tax for the given income by adhering to the below rules

def tax(x):

    y = 0 #taxable income
    if (x > 10000 and x <= 20000):
        y = (x - 10000) * 0.1
    elif (x > 20000):
        y = ((x - 10000) * 0.1) + ((x - 20000) * 0.2)

    return y

a = int(input("Enter Income: "))

print(tax(a))

# messed up the calculations but out of time, will continue tomorrow
