#FUNCTION EXERCISES

#Exercise 1 - Create a Function in python that takes two arguments, name and age and prints them out

def func(name, age):

    txt = "Hello {name}, you are {age} years old"
    print(txt.format(name = name, age = age))

#func(input("Enter Name: "), int(input("Enter Age: ")))

#Exercise 2 - Create a function with variable length of arguments

def func2(*vars):
    print("parameters")
    print(*vars)

#func2(10, 20)
#func2(10)

#Exercise 3 - Return multiple values from a function (addition and subtraction)

def calculation(a, b):
    return a + b, a - b

res = calculation(40, 10)

#print(res)

#Exercise 4 - Create a function with default argument

def showEmployee(a, b = 9000):
    txt = "Name: {a}, Salary: {b}"
    return txt.format(a = a, b = b)

print(showEmployee("Ben", 12000))
print(showEmployee("Jessa"))

#Exercise 5 - Create outer function accepting parameters a and b. Create inner function to calclate a + b, create mid layer function to add 5 to the inner layer function

def outer():
    a = int(input("Enter parameter a: "))
    b = int(input("Enter Parameter b: "))
    
    def inner(c, d):
        return c + d
    
    inner1 = inner(a, b)
    def Outer(e):
        return e + 5

    outer1 = Outer(inner1)

    return outer1

#print(outer())
