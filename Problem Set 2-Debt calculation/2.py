prevbalance=balance
monthlyInterestrate=annualInterestRate/12.0
minimummonthlyPayment=10
while True:
    for i in range(1,13):
     monthlyUnpaidBalance= prevbalance-minimummonthlyPayment
     prevbalance=monthlyUnpaidBalance+(monthlyInterestrate*monthlyUnpaidBalance)
    if prevbalance<=0:
        break
    else:
        prevbalance=balance
        minimummonthlyPayment+=10
print(minimummonthlyPayment)