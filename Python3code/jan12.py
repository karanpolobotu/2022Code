#More Financial Functions

#Annuities

def annuity():
    #C, r, m, t, PV
    print('')
    print('1 --> PV')
    print('')
    print('2 --> Coupon payment (C)')
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
        print("PRESENT VALUE OF ANNUITY IS: " + str(PV))
        return 0

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
    var = int(input("Which Variable are you solving for: "))
    print('')

    if var == 1:
        C = float(input("Enter Coupon Payment (C): "))
        r = float(input("Enter discount rate/APR/stated rate: "))
        g = float(input("Enter per coupon growth rate (g)"))
        m = float(input("Enter compounding rate: "))
        t = float(input("Enter time of payment streams in years: "))
    
        pR = r/m #periodic rate
        T = m * t # total time periods
        PV = (C/(pR - g)) * (1 - ( ((1 + g)/((1 + pR))**T)) )
        print("PRESENT VALUE OF ANNUITY IS: " + str(PV))
        return 0

    elif var == 2:
        PV = float(input("Enter PV of Annuity: "))
        r = float(input("Enter discount rate/APR/stated rate: "))
        g = float(input("Enter per coupon growth rate (g)"))
        m = float(input("Enter compounding rate: "))
        t = float(input("Enter time of payment streams in years: "))
        
        pR = r/m #periodic rate
        T = m * t # total time periods
        C = (pR - g) * PV/(1 - ( ((1 + g)/((1 + pR))**T)) )
        print("COUPON VALUE/RECURRING PAYMENT IS: " + str(C))       
        return 0
    else:
        print("ALTERNATIVE OPTIONS NOT SUPPORTED")
        gannuity()
        
    return 0
