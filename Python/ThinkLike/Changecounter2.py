changerem=input('Amount of cash to be given in cents ')

#name, value in cents, quantity remaining
currencies1 = [('quarters', 25, 1), ('dimes', 10, 2), ('nickels', 5, 3), ('pennies', 1, 100)]


for i in currencies1:
	if changerem > 0:
		changegive = changerem // i[1]
		changerem = changerem % i[1]
		if changegive > 0:
			print "You give %r %s" % (changegive, i[0])