#Exercise 12 - Calculate income tax for the given income by adhering to the below rules

def tax(x):

    if (x <= 10000):
        return 0
    elif (x >= 10000 and x < 20000):
        return (x - 10000)*(0.1)
    else:
        return (10000)*(0.1) + (x - 20000)*(0.2)

#a = int(input("Enter Income: "))

#print(tax(a))

#Exercise 13 - Print the multiplication table of x and y

def multi(x, y):
    
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            print(i * j, end = " ") #end condition gives formatting
        print('')

#a = int(input("Enter x: "))
#b = int(input("Enter y: "))

#multi(a, b)


#Exercise 14 - Print an asterisk pyramid upside down

def star(x):

    for i in range (x, 0, -1): #range() takes a 3rd parameter which can dictate increment or decrement
        print(i * '* ')


a = int(input("Enter y: "))

star(a)
