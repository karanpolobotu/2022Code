#More Financial Functions

#Perpituities

def perpituity():
    print('')
    print('1 --> PV')
    print('')
    print('2 --> Coupon payment (C)')
    print('')
    print('3 --> discount rate (r)')
    print('')    
    var = int(input("Which Variable are you solving for: "))
    print('')
    
    if var == 1:
        C = float(input("Input Coupon payment: "))
        r = float(input("Discount rate: "))
        PV = C/r
        print("PRESENT VALUE OF CONSOL/PERPITUITY: " + str(PV))
        return 0
    elif var == 2:
        PV = float(input("Present Value of Perpituity: "))
        r = float(input("Discount rate: "))
        C = PV * r
        print("Coupon payment amount: " + str(C))
        return 0
    elif var == 3:
        C = float(input("Input Coupon payment: "))
        PV = float(input("Present Value of Perpituity: "))
        r = C/PV
        print("Interest rate/stated rate: " + str(r))
        return 0
    else:
        print("SELECTION DOES NOT EXIST")
        perpituity()
    return 0

#Growing Perpituities

def gperpituity():
    print('')
    print('1 --> PV')
    print('')
    print('2 --> Coupon payment (C)')
    print('')
    print('3 --> discount rate (r)')
    print('') 
    print('4 --> Coupon payment growth rate (g)')
    print('')    
    var = int(input("Which Variable are you solving for: "))
    print('')
    
    if var == 1:
        C = float(input("Input Coupon payment (C): "))
        r = float(input("Discount rate (r): "))
        g = float(input("Coupon payment growth rate (g): "))
        PV = C/(r - g)
        print("PRESENT VALUE OF CONSOL/PERPITUITY: " + str(PV))
        return 0
    elif var == 2:
        PV = float(input("Present Value of Perpituity: "))
        r = float(input("Discount rate: "))
        g = float(input("Coupon payment growth rate (g): "))
        C = PV * (r - g)
        print("Coupon payment amount: " + str(C))
        return 0
    elif var == 3:
        C = float(input("Input Coupon payment: "))
        PV = float(input("Present Value of Perpituity: "))
        g = float(input("Coupon payment growth rate (g): "))
        r = C/PV + g
        print("Interest rate/stated rate: " + str(r))
        return 0
    elif var == 4:
        C = float(input("Input Coupon payment: "))
        PV = float(input("Present Value of Perpituity: "))
        r = float(input("Discount rate: "))
        g = r - C/PV
        print("Interest rate/stated rate: " + str(r))
        return 0
    else:
        print("SELECTION DOES NOT EXIST")
        perpituity()
    return 0
    return 0

