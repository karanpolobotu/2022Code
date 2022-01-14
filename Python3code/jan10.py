#More Financial Functions

import math

#Net Present Value (NPV)

def NPV():
    # solve for PV, r (one period), C0, C1
    
    print('')
    print('1 --> NPV')
    print('')
    print('2 --> r (one period)')
    print('')
    print('3 --> C0 (one period)')
    print('')
    print('4 --> C1 (one period)')
    print('')    
    var = int(input("Which Variable are you solving for: "))
    print('')
    
    if var == 1:

        time = int(input("Enter Number of years: "))
        initialC = float(input("Enter Initial Cash Outflow (IN POSITIVE): "))
        wacc = float(input("Enter Discount rate (from percent to decimal): "))
        NPV =  0 - initialC
        C = []
        CPV = []
        oneWacc = 1 + wacc
        for i in range (0, time):
            imp = float(input("Enter Cash Inflow " + str(i + 1) + ": "))
            impV = imp/(oneWacc ** (i + 1))            
            C.append(imp)
            CPV.append(impV)
            print('')
                
        for i in range (0, len(C)):
            print("CASH FLOW " + str(i + 1) + ": " + str(C[i]) + "           PV of Cash Flow: " + str(CPV[i]))
            print('')
            NPV += CPV[i]
                
        print("NET PRESENT VALUE: " + str(round(NPV, 2)))
        return 0

    elif var == 2:
        time = 1
        NPV = int(input("Enter NPV: "))
        initialC = float(input("Enter Initial Cash Outflow (IN POSITIVE): "))
        COne = float(input("Cash Flow 1: "))

        wacc = (COne/(initialC + NPV) - 1)
        print("Discount Rate/wacc is: " + str(round(wacc)))
        return 0

    elif var == 3:
        time = 1
        NPV = int(input("Enter NPV: "))
        wacc = float(input("Enter Discount rate (from percent to decimal): "))
        COne = float(input("Cash Flow 1: "))
        initialC = COne/(1 + wacc) - NPV
        print("Initial Cash Outflow: " + str(round(initialC)))
        return 0

    elif var == 4:
        time = 1
        NPV = int(input("Enter NPV: "))
        wacc = float(input("Enter Discount rate (from percent to decimal): "))
        initialC = float(input("Enter Initial Cash Outflow (IN POSITIVE): "))
        COne = (1 + wacc) * (initialC + NPV)
        print("Initial Cash Inflow (year 1): " + str(round(COne)))
        return 0

    else:
        print("SELECTION DOESNT EXIST. SORRY")
        NPV()
    
    
#APR and EAR

def rates():
    print('')
    print('Cannot find m, sorry')
    print('')
    print('1 --> EAR')
    print('')
    print('2 --> APR')
    print('')
        
    var = int(input("Which Variable are you solving for: "))
    print('')

    if var == 1:
        APR = float(input("Enter APR (DECIMAL, ex. 0.08): "))
        m = float(input("Enter Compounding Frequency (semiannual = 2, annual = 1, quarterly = 4, etc. ): "))
        EAR = (1 + (APR/m))**m - 1
        print("EFFECTIVE ANNUAL RATE: " + str(round(EAR, 4)))
        return 0

    elif var == 2:
        EAR = float(input("Enter EAR (DECIMAL, ex. 0.08): "))
        m = float(input("Enter Compounding Frequency (semiannual = 2, annual = 1, quarterly = 4, etc. ): "))
        APR = m * ((EAR + 1)**(1/m) - 1)
        print("ANNUAL PERCENTAGE RATE/ STATED RATE / R: " + str(round(APR, 4)))
        return 0
        
    else:
        print("SELECTION DOESNT EXIST. SORRY")
        rates()

    return 0

#Continuous Compounding

def contComp():
    print('')
    print('Cannot find m, sorry')
    print('')
    print('1 --> FV')
    print('')
    print('2 --> Principal amount')
    print('')
    print('3 --> Annual rate')
    print('')
    print('4 --> Time (in years)')
    print('')
    var = int(input("Which Variable are you solving for: "))
    print('')

    if var == 1:
        initialC = float(input("Principal Amount: "))
        r = float(input("Annual Effective Rate/stated rate: "))
        time =  float(input("time in years: "))
        FV = initialC * ((math.e) ** (r * time))
        print("CONTINUOUS COMPOUNDING IS: " + str(round(FV, 2)))
        return 0

    elif var == 2:
        FV =  float(input("final value: "))
        r = float(input("Annual Effective Rate/stated rate: "))
        time =  float(input("time in years: "))
        initialC = FV/((math.e) ** (r * time))
        print("PRINCIPAL AMOUNT: " + str(round(initialC, 2)))
        return 0
    elif var == 3:
        FV =  float(input("final value: "))
        initialC = float(input("Principal Amount: "))
        time =  float(input("time in years: "))
        r = (math.log(FV/initialC))/time
        print("ANNUAL INTEREST RATE IS: " + str(round(r, 2)))
        return 0
    elif var == 4:
        FV =  float(input("final value: "))
        initialC = float(input("Principal Amount: "))
        r = float(input("Annual Effective Rate/stated rate: "))
        time = (math.log(FV/initialC))/r
        print("TOTAL TIME IN YEARS: " + str(round(time, 2)))

    return 0
