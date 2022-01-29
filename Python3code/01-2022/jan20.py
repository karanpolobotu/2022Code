#Exercise 14 - Reverse a given integer number

def reversal(a):
    num = a
    revNum = 0
    while num > 0:
        remainder = num % 10
        revNum = (revNum * 10) + remainder
        num = num//10
    print(revNum)

print(reversal(76542))
