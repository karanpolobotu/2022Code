#STRING EXERCISES

#Exercise 1A  create a string made of the first, middle and last character. 

def strseq(string):
    newstr = string[0] + string[len(string)//2] + string[len(string) - 1]
    return newstr


#print(strseq("James"))

#Exercise 1B: Create a string made of the middle three characters

def strseq2(string):
    mid = len(string)//2
    newstr = string[mid - 1] + string[mid] + string[mid + 1]
    return newstr

#print(strseq2("James"))

#Exercise 2: join two strings together in a special way with S2 wedged in between S1

def strAppend(a, b):
    mid = len(a)//2    
    return a[:mid - 1] + b + a[mid:]

#print(strAppend("hello ","there"))

#Exercise 3 - Join a string made of special characters

def joinStr(a, b):
    return a[0] + b[0] + a[len(a)//2] +    b[len(b)//2] + a[len(a) - 1] + b[len(b) - 1]

#Exercise 4 - Arrange string characters such that lowercase letters should come first

def e4(s):
    x = ""
    for i in s:
        if str.islower(i) == True:
            x += i

    for i in s:
        if str.islower(i) == False:
            x += i

    return x

#print(e4("PyNative"))

#Exercise 5 - Count all letters, digits and special symbols in a string
def e5(s):
    #isalpha()
    #isdigit()
    dig = 0
    st = 0
    spec = 0
    for i in s:
        if str.isalpha(i) == True:
            st += 1
    
    for i in s:
        if str.isdigit(i) == True:
            dig += 1

    for i in s:
        if str.isdigit(i) == False and str.isalpha(i) == False:
            spec += 1
            
        return st, dig, spec

#print(e5("P@#yn26at^&i5ve"))

def e6(s1, s2):
    
    s3 = ""
    for i in range(len(s1)):
        s3 += s1[i]
        s3 += s2[i]        

    return s3

#print(e6("hot", "dog"))

def e7(s1, s2):
    boolean = False
    for i in s1:
        if i in s2:
            boolean = True
        else:
            boolean = False
            break
    return boolean

#print(e7("yn", "Pyn"))

#print(e7("f", "Pyn"))

def e8(s, c):
    
    temp_str = s.lower()

    # use count function
    count = temp_str.count(c.lower())
    return count

#print(e8("ff", "f"))

