#Exercise 9 - sum of digits and average of digits that appear in a string

def e9(s):

    count = 0
    summ = 0
    for i in s:
        if str.isdigit(i) == True:
            count += 1
            summ += int(i)
             
    
    avg = summ/count
    print("Sum is: " + str(summ) + " average is: " + str(avg))

#e9("PYnative29@#8496")

#Exercise 10 - Write a program to count occurences of all characters within a string

def e10(s):

    for i in s:
        print(i, s.count(i))

#e10("apple")

#Exercise 11 - Reverse a given string

def e11(s):
    rs = ""
    for i in range(len(s) - 1, -1, -1):
        rs += (s[i])
    
    return(rs)

#print(e11("rev"))

#Exercise 12 - Find the last position of a given substring

def e12(sub, s):
    index = s.rfind(sub)
    return index


print(e12("Emma", "Emma is a data scientist who knows Python. Emma works at google."))
