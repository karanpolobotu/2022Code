#Exercise 8 - Print list in reverse order using loop

def revLoop(a):
    for i in range(len(a) - 1, -1, -1):
        #weird that the for loop has to terminate at -1 haha
        print(a[i])

#revLoop([10, 20, 30, 40, 50])

#Exercise 9 - Display numbers from -10 to -1

def revDis():
    negArr = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
    for i in negArr:
        print(i)

#revDis()

#Exercise 10 - Use else block to display a message "done" after sucessful execution of loop

def execution():
    for i in range(5):
        if i < 4:
            print(i)
        else: 
            print(i)
            print("Done!")

#execution()

#Exercise 11 - Write a program to display all prime numbers within a range

def primes(a, b):
    newArr = []
    for i in range (a, b + 1):
        newArr.append(i)
    
    for i in newArr:
        counter = 0
        for j in range (1, i):
            if(i % j == 0):
                counter += 1
        if counter > 2:
            newArr.remove(i)

    print(newArr)

#INCOMPLETE    


primes(25, 50)
