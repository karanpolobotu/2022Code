#Exercise 4 - Remove first n characters from a string

def nIndex(a, b):
    #a is string
    #b is number of characters to be removed
    
    if b > len(a):
        print("cannot remove more characters than entire word")
        return 0
    else:
        print(a[b:len(a)])
        
    return 0

#c = str(input("string here: "))
#d = int(input("integer here: "))

#nIndex(c, d)

#Exercise 5 - Check if the first and last number of a list is the same

def lIndex(x):
    
    if (x[0] == x[len(x) - 1]):
        return True

y = [10, 21, 32, 40, 10]

#Exercise 6 - Display numbers divisible by 5 from a list

def divisFive(x):
    for i in x:
        if (i%5 == 0):
            print(i)

divisFive(y)

#Exercise 7 - Return the count of a given substring from a string

def subStr(x, y):
    count = 0
    for i in range (1, len(x)):
        if x[i] = y[i]
