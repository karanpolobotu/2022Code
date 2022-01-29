#jan 13th, search algorithms

def linearSearch(l, c):

    for i in l:
        if i == c:
            return ("found")
            
    return("could not be found")

def binarySearch(l, c, d):
    L = len(l)
    end = l[L - 1]
    beginning = l[0]
    mid = (beginning + end)//2
    #pretty standard set up the middle, keep dividing the middle until we get what we want
    if mid == c:
        return("found " + str(mid) + " on interation: " + str(d))
    elif mid < c:
        newL = l[L//2:]
        return binarySearch(newL, c, d + 1)
    elif mid > c:
        newL = l[:L//2]
        return binarySearch(newL, c, d + 1)
    return 0

e = int(input("Enter bottom range: "))
f = int(input("Enter top range: "))
listT = []
for i in range (e, f + 1):
    listT.append(i)

g = int(input("Enter value to be searched: "))
print(linearSearch(listT, g))

print(binarySearch(listT, g, 1))
