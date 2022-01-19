#Exercise 15 - Use a loop to display elements from a given list present at odd index positions

def indices(a):
    for i in range(0, len(a)):
        if i % 2 == 0:
            continue
        else:
            print(a[i], end =' ')
    print()

#indices([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

#Exercise 16 - Calclate the cube of all numbers from 1 to a given number

def cuber(a):
    cubed = []
    for i in range(1, a + 1):
        cube = i **3
        cubed.append(cube)
    print(cubed)

#cuber(5)

#Exercise 17 - Find the sum of the series up to n terms

def summation(a):
    valSum = 0
    val = 0
    for i in range(0, a):
        val = val + (2 * (10 ** i))
        valSum += val
    print(valSum)
    
summation(5)
# Still solving

#Exercise 18 - TopBotPyramid

def pyra(a):
    for i in range(1, a):
        print("* " * i)
    for i in range(a, 0, -1):
        print("* " * i)


pyra(5)


