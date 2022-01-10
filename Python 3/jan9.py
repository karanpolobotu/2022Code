# Simple Financial functions

import math

def main():
    func = int(input("Press 1 for simple interest, 2 for compound interest: "))
    
    if func == 1:
        print(SimpleInterest())
    elif func == 2:
        print(CompoundInterest())

# Simple Interest

def SimpleInterest():
    print("LEAVE UNSOLVED VALUE MISSING")
    A = (input("Enter Future Value: "))
    P = (input("Enter deposit amount: "))
    r = (input("Enter annual interest rate (make sure % is decimal, ex. 8% is 0.08): "))
    period = (input("Periods per year? Semi annual = 2, annual = 1, etc: "))
    t = (input("total time: "))

    #FV, PV, R, Period, T = float(A), float(P), float(r), float(period), float(t)

    #FUTURE VALUE
    if A == '':
        FV, PV, R, Period, T = 0, float(P), float(r), float(period), float(t)
        FV = PV * (1 + (R/Period) * T)
        return 'Future Value is: ' + str(FV)
    
    #PRESENT VALUE
    elif P == '':
        FV, PV, R, Period, T = float(A), 0, float(r), float(period), float(t)
        PV = FV/(1 + (R/Period) * T)
        return 'Present Value is: ' + str(PV)

    #ANNUAL INTEREST RATE
    elif r == '':
        FV, PV, R, Period, T = float(A), float(P), 0, float(period), float(t)
        R = ((Period * (FV/PV - 1))/T)
        return 'Annual Interest rate is: ' + str(R)
    
    #COMPOUNDING PERIOD
    elif period == '':
        FV, PV, R, Period, T = float(A), float(P), float(r), 0, float(t)
        Period = (R * T)/((FV/PV) - 1)
        return 'Compounding Period is: ' + str(Period)
    
    #TIME PERIOD
    elif t == '':
        FV, PV, R, Period, T = float(A), float(P), float(r), float(period), 0
        T = (Period * ((FV/PV) - 1))/R
        return 'Time period (in years) is: ' + str(T)

    else:
        return "Something is wrong, most likely more than 1 missing input. check again" 

# Compound Interest

def CompoundInterest():
    print("LEAVE UNSOLVED VALUE MISSING")
    A = (input("Enter Future Value: "))
    P = (input("Enter deposit amount: "))
    r = (input("Enter annual interest rate (make sure % is decimal, ex. 8% is 0.08): "))
    period = (input("Compounding Periods per year? Semi annual = 2, annual = 1, etc: "))
    t = (input("total time: "))


    #FV, PV, R, Period, T = float(A), float(P), float(r), float(period), float(t)

    #FUTURE VALUE
    if A == '':
        FV, PV, R, Period, T = 0, float(P), float(r), float(period), float(t)
        FV = PV * ((1 + (R/Period))**T)
        return 'Future Value is: ' + str(round(FV, 2))
    
    #PRESENT VALUE
    elif P == '':
        FV, PV, R, Period, T = float(A), 0, float(r), float(period), float(t)
        PV = FV/((1 + (R/Period))**T)
        return 'Present Value is: ' + str(round(PV, 2))

    #ANNUAL INTEREST RATE
    elif r == '':
        FV, PV, R, Period, T = float(A), float(P), 0, float(period), float(t)
        R = Period * ((FV/PV)**(1/T) - 1)
        return 'Annual Interest rate is: ' + str(round(R, 4))
    
    #COMPOUNDING PERIOD
    elif period == '':
        FV, PV, R, Period, T = float(A), float(P), float(r), 0, float(t)
        Period = R/((FV/PV)**(1/T) - 1)
        return 'Compounding Period is: ' + str(round(Period, 2))
    
    #TIME PERIOD
    elif t == '':
        FV, PV, R, Period, T = float(A), float(P), float(r), float(period), 0
        T = (math.log10(FV/PV))/(math.log10(1 + (R/Period)))
        return 'Time period (in years) is: ' + str(round(T, 2))

    else:
        return "Something is wrong, most likely more than 1 missing input. check again" 


main()
