#Exercise 4 - program for multiplication tables

def tables(a):
    for i in range(0, 11):
        print(a * i)

#tables(int(input('Enter number: ')))

#Exercise 5 - Display numbers from a list using loop

def loopList(a):
    for i in a:
        if i > 500:
            break
        elif i > 150:
            continue
        elif i % 5 == 0:
            print(i)
    return 0

#loopList([12, 75, 150, 180, 145, 525, 50])

#Exercise 6 - count total number of digits in a number

def counter(a):
    b = str(a)
    print(len(b))


#counter(534325)

#Exercise 7 - Print a reverse looped pyramid pattern

def rPyramid(a):
    for i in range(a, 0, -1):
        for j in range(i, 0, -1):
            print(j, end = ' ')
        print()

#rPyramid(5)
