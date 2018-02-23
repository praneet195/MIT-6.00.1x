monthlyInterestrate=annualInterestRate/12.0
for i in range(1,13):
    minimummonthlyPayment=monthlyPaymentRate*balance
    monthlyUnpaidBalance= balance-minimummonthlyPayment
    balance=monthlyUnpaidBalance+(monthlyInterestrate*monthlyUnpaidBalance)
print("Remaining balance:",round(balance,2))