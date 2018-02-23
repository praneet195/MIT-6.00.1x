monthlyInterestrate=annualInterestRate/12.0
lowmonth=balance/12
highmonth=(balance*((1+monthlyInterestrate)**12))/12.0
minimummonthlyPayment=(lowmonth+highmonth)/2.0
prevbal=balance
while True:
    for i in range(0,12):
     monthlyUnpaidBalance= prevbal-minimummonthlyPayment
     prevbal=monthlyUnpaidBalance+(monthlyInterestrate*monthlyUnpaidBalance)
    if prevbal<-0.1:
        highmonth=minimummonthlyPayment
        prevbal=balance
        minimummonthlyPayment = (lowmonth + highmonth)/2.0
    elif prevbal >0.1:
        lowmonth = minimummonthlyPayment
        prevbal = balance
        minimummonthlyPayment = (lowmonth + highmonth) / 2.0
    else:
        break
print(round(minimummonthlyPayment,2))