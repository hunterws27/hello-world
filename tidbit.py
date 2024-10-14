purchasePrice = float(input("Enter the purchase price: "))
downPayment = purchasePrice * 0.10
annualInterestRate = 0.12
monthlyPaymentRate = 0.05

    
balance = purchasePrice - downPayment

month = 1

print(f"{'Month':<10}{'Total Balance':<20}{'Interest Owed':<20}{'Principal Owed':<20}{'Payment':<20}{'Remaining Balance':<20}")
print("-" * 110)

while balance > 0:
    monthlyPayment = purchasePrice * monthlyPaymentRate
    interest = balance * (annualInterestRate / 12)
    principal = monthlyPayment - interest
        
    if balance < monthlyPayment:
        monthlyPayment = balance + interest
        principal = balance

    remainingBalance = balance - principal

    print(f"{month:<10}{balance:<20.2f}{interest:<20.2f}{principal:<20.2f}{monthlyPayment:<20.2f}{remainingBalance:<20.2f}")

    balance = remainingBalance
    month += 1
