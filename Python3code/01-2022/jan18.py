#Exercise 11 - Write a program to display all prime numbers within a range

def primes(a, b):
    for i in range(a, b + 1):
        if i > 1:
            #identifies primes, took SO LONG
            for j in range(2, i):
                if (i % j == 0):
                    break
            else:
                print(i)

primes(1, 10)
