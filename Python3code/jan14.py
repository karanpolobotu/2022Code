#Exercise 6 - Write all content to a given file into a new file but skip line 5

with open ('test.txt', 'r') as fp:
    lines = fp.readlines()

with open("new_file.txt", "w") as fp:
    i = 0
    for line in lines:
        if i == 4:
            i += 1
            continue
        else:
            fp.write(line)
        i += 1


#Exercise 7 - Accept any three string input from one input() call

name1, name2, name3 = input("Enter three random strings separated by space ").split()
print("\n")
print(name1)
print(name2)
print(name3)

#Exercise 8 - Format Variables using a string.format() method

totalMoney, price = float(input("enter total amount: ")), float(input("Enter price: "))
 
quantity = totalMoney/price

txt = "I have {totalMoney:.2f} dollars so I can buy {quantity} football for {price:.2f} dollars."

print(txt.format(totalMoney = totalMoney, quantity = quantity, price = price))
