#Exercise 1 - Calculate the multiplication and sum of two numbers


def multiAdd():
    
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    c = a + b
    d = a * b

    print("a times b is: " + str(d))
    print("a plus b is: " + str(c))

#Exercise 2 - Print the sum of the current number and previous number

def currentPrev():
    
    currentNum = 0
    prevNum = 0    
    for i in range(0, 10):
        currentNum = i
        if (currentNum == 0):
            prevNum = 0
        else:
            prevNum = currentNum - 1
        sumT = currentNum + prevNum
        print ("Current Number " + str(currentNum) + " Previous Number" + str(prevNum) + "Sum: " + str(sumT))

#Exercise 3 - Print characters frm a string that are present at an even index number

def eIndex():

    a = str(input("Enter string: "))
    
    for i in range (0, len(a)):
        if (i % 2 == 0):
            print(a[i])

#Exercise 4 - Remove first n characters from a string

def nIndex(a, b):
    #a is string
    #b is number of characters to be removed
    
    #if b < len(a) --> INCOMPLETE
        
    return 0

c = str(input("string here: "))
d = str(input("integer here: "))

nIndex(c, d)
