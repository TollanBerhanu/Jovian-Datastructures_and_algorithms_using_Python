def loan_emi(amount, duration, rate=0.05, down_payment=0):
    """Calculates the equal montly installment (EMI) for a loan.
        Arguments:  amount - Total amount to be spent (loan + down payment)
                    duration - Duration of the loan (in months)
                    rate - Rate of interest (monthly)
                    down_payment (optional) - Optional intial payment (deducted from amount)"""
    loan_amount = amount - down_payment
    emi = loan_amount * rate * ((1+rate)**duration) / (((1+rate)**duration)-1)
    return emi

help(loan_emi) # Prints out the 'docstring' help text in the function
print(loan_emi(1260000, 8*12, 3e2)) # 3 x 10^2
print(loan_emi(1260000, 8*12))
emi1 = loan_emi(
    amount=1260000, 
    duration=8*12, 
    rate=0.1/12, 
    down_payment=3e5
)
print(emi1)

import math
print(math.ceil(1.5))

def division(a, b):
    try:
        result = a / b
        print(result)
    except ZeroDivisionError:
        print('Division by zero error')
division(5, 0)



