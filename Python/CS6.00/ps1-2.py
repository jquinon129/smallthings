balance = float(raw_input('Oustanding balance on the credit card: '))
annual_rate = float(raw_input('Annual interest rate as a decimal: '))
minimum_rate = 10.0
monthly_rate = annual_rate / 12.0
rem_balance = balance

while balance > 0:
	for x in xrange(1,13):
		balance = round(balance * (1 + monthly_rate) - minimum_rate, 2)
		if balance < 0:
			print 'RESULT'
			print 'Number of months needed to pay off debt: %r' % x
			print 'Balance: %r' % balance
			print 'Monthly payment to pay off debt in 1 year: %r' % minimum_rate
			break
	if balance > 0:
		balance = rem_balance
		minimum_rate += 10.0
	

	