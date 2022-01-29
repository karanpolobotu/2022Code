#Exercise 12 - Display Fibonacci sequence up to 10 terms

def Fib10():
    #using hint to solve
    num1 = 0
    num2 = 1
    for i in range(1, 10):
        print(num1)
        res = num1 + num2
        num1, num2 = num2, res

#Fib10()

def factorial(a):
    fact = a
    for i in range(a - 1, 0, -1):
        fact *= i
    print(fact)

#factorial(5)
