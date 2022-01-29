#More Financial Functions

import math

#Annuities

def annuity():
    #C, r, m, t, PV
    print('')
    print('1 --> PV')
    print('')
    print('2 --> Coupon payment (C)')
    print('')
    print('3 --> interest rate (r) (in beta testing, will not give perfect result)')
    print('')
    print('4 --> Time (T) (beta testing still required)')
    print('')

    var = int(input("Which Variable are you solving for: "))
    print('')

    if var == 1:
        C = float(input("Enter Coupon Payment (C): "))
        r = float(input("Enter discount rate/APR/stated rate: "))
        m = float(input("Enter compounding rate: "))
        t = float(input("Enter time of payment streams in years: "))
    
        pR = r/m #periodic rate
        T = m * t # total time periods
        PV = (C/pR) * (1 - (1/((1 + pR)**T)))
        print("PRESENT VALUE OF ANNUITY AT START DATE IS: " + str(PV))
        print('')        
        print("REMINDER: PLEASE CHECK QUESTION. IF PAYMENTS START LATER, USE COMPOUD INTEREST CALCULATOR TO FIND ACTUAL PV DISCOUNTED FOR N-1 YEARS")

    elif var == 2:
        PV = float(input("Enter PV of Annuity: "))
        r = float(input("Enter discount rate/APR/stated rate: "))
        m = float(input("Enter compounding rate: "))
        t = float(input("Enter time of payment streams in years: "))
        
        pR = r/m #periodic rate
        T = m * t # total time periods
        C = pR * (PV/(1 - (1/((1 + pR)**T))))
        print("COUPON VALUE/RECURRING PAYMENT IS: " + str(C))        
        return 0

    elif var == 3:
        C = float(input("Enter Coupon Payment (C): "))
        PV = float(input("Enter PV of Annuity: "))
        r = 50
        m = int(input("Enter annual compounding rate/frequency: "))
        t = int(input("Enter time of payment streams in years: "))

        print(binaryAnnuities(PV, C, r, 0, m, t))
        return 0
    elif var == 4:
        C = float(input("Enter Coupon Payment (C): "))
        PV = float(input("Enter PV of Annuity: "))
        r = float(input("Enter discount rate/APR/stated rate: "))
        t = math.log(((r) * (PV))/C + 1)/math.log((1)/(1 + r))
        print(t)
        return 0
    else:
        print("ALTERNATIVE OPTIONS NOT SUPPORTED")
        annuity()
    return 0

#Growing Annuities

def gannuity():
    # C, r, g, m, t, PV
    
    print('')
    print('1 --> PV')
    print('')
    print('2 --> Coupon payment (C)')
    print('')
    print('3 --> interest rate (r)')
    print('')
    print('4 --> Time (T) (beta testing still required)')
    print('')
    
    var = int(input("Which Variable are you solving for: "))
    print('')

    if var == 1:
        C = float(input("Enter Coupon Payment (C): "))
        r = float(input("Enter discount rate/APR/stated rate: "))
        g = float(input("Enter per coupon growth rate (g)"))
        m = float(input("Enter annual compounding rate/frequency: "))
        t = float(input("Enter time of payment streams in years: "))
    
        pR = r/m #periodic rate
        T = m * t # total time periods
        PV = (C/(pR - g)) * (1 - ( ((1 + g)/((1 + pR))**T)) )
        print("PRESENT VALUE OF ANNUITY IS: " + str(PV))
        print('')        
        print("REMINDER: PLEASE CHECK QUESTION. IF PAYMENTS START LATER THAN 1 YEAR, USE COMPOUD INTEREST CALCULATOR TO FIND ACTUAL PV DISCOUNTED FOR N-1 YEARS")
        return 0

    elif var == 2:
        PV = float(input("Enter PV of Annuity: "))
        r = float(input("Enter discount rate/APR/stated rate: "))
        g = float(input("Enter per coupon growth rate (g)"))
        m = float(input("Enter annual compounding rate/frequency: "))
        t = float(input("Enter time of payment streams in years: "))
        
        pR = r/m #periodic rate
        T = m * t # total time periods
        C = (pR - g) * PV/(1 - ( ((1 + g)/((1 + pR))**T)) )
        print("COUPON VALUE/RECURRING PAYMENT IS: " + str(C))       
        return 0

    elif var == 3:
        C = float(input("Enter Coupon Payment (C): "))
        PV = float(input("Enter PV of Annuity: "))
        r = 50
        g = float(input("Enter per coupon growth rate (g)"))
        m = int(input("Enter annual compounding rate/frequency: "))
        t = int(input("Enter time of payment streams in years: "))

        print(binaryAnnuities(PV, C, r, g, m, t))
        return 0
    elif var == 4:
        C = float(input("Enter Coupon Payment (C): "))
        PV = float(input("Enter PV of Annuity: "))
        r = float(input("Enter discount rate/APR/stated rate: "))
        g = float(input("Enter per coupon growth rate (g): "))
        t = math.log(((r - g) * (PV))/C + 1)/math.log((1 + g)/(1 + r))
        print(t)
        
        #find time periods
        return 0
    else:
        print("ALTERNATIVE OPTIONS NOT SUPPORTED")
        gannuity()
        
    return 0

def binaryAnnuities(PV, C, r, g, m, t):

    R = r/(100 * m)
    pR = round(R, 4)

    LHS = PV

    if g == 0:
        RHS = (C/pR) * (1 - (1/((1 + pR)**t)))

    else:
        RHS = (C/(pR - g)) * (1 - ( ((1 + g)/((1 + pR))**t)) )

    lLHS = round(LHS, 3)
    rRHS = round(RHS, 3)
    print("LHS: " + str(lLHS))
    print("RHS: " + str(rRHS))
    print("interest rate: " + str(r) + "%")
    while True:
        try:
            if (rRHS < lLHS * 1.001) and (rRHS > lLHS * 0.9999):
                print("Closest Guess is: " + str(r))
                return 0
            elif lLHS > rRHS:
                newr = r - r/2
                binaryAnnuities(PV, C, newr, g, m, t)
            elif lLHS < rRHS:
                newr = r + r/2
                binaryAnnuities(PV, C, newr, g, m, t)
            break
        except RecursionError:
            print(r)
            return 0
