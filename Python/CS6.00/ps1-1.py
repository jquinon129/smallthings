#Calc the credit card balance after one year if a person only pays the minimum
balance = float(raw_input("Enter the outstanding balance on your credit card: "))
annual_interest_rate = float(raw_input('Enter the annual credit card interest rate as a decimal: '))
min_payment_rate = float(raw_input ("Enter the minimum monthly payment rate as a decimal: "))
month = 1
total_paid = 0

while month <= 12:
	min_payment = round(min_payment_rate * balance, 2)
	interest_paid = round((annual_interest_rate / 12) * balance, 2)
	prin_paid = round (min_payment - interest_paid, 2)
	balance = round( balance - prin_paid, 2)
	print('Month: %r \n Minimum Monthly Payment: %r \n Principle Paid: %r \n Remaining Balance: %r') % (month, min_payment, prin_paid, balance)
	total_paid += min_payment
	month += 1

print ('RESULT \n Total amount paid: %r \n Remaining balance: %r') % (round(total_paid, 2) , balance)