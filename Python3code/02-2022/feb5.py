# Leetcode - Merge two sorted lists

# step 1: merge into one

# step 2: sort


def mergeInp(a, b):
    listM = a
    for i in b:
        listM.append(i)
    return listM

def bubblesort(a):
    for i in range(0, len(a) - 1):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
    return a

if __name__ == "__main__":
    testList1 = [1, 2, 3]
    testList2 = [2, 1, 4, 3, 2]

    #print(mergeInp(testList1, testList2))

    print(bubblesort(testList2))
