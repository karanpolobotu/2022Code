#Exercise 7 - Return the count of a given substring from a string

def subStr(x, y):
    a = y.count(x)
    print(a)

b = "Emma is good developer. Emma is a writer"
c = "Emma"

#Exercise 8 - Print a specific pattern

def pyramid(x):

    for i in range(1, x + 1):
        print((str(i) + " ") * i)


#Exercise 9 - Write a program to check if a given number is a palindrome

def palindrome(x):
    y = str(x)
    
    z = reversed(y) #pointing at a reversed pointer, will fix tomorrow

    if (y == z):
        print("Yes, given number is a Palindrome")
    else:
        print("No, given number is not a palindrome")

x = int(input("Enter Number: "))
palindrome(x)
