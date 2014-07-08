#asks user to input amount of cash and returns
#denominations taking limits into consideration

#name, value in cents, quantity remaining
#need to make it possible to input and change to use dictionaries
currencies1 = [('quarters', 25, 1), ('dimes', 10, 2), ('nickels', 5, 3), ('pennies', 1, 100)]

#Presents how much of each denomination on has
for i in currencies1:
	print 'You have %r %s' % (i[2], i[0])

#asks for user input will ask again if too high
totalcash = 0
for i in currencies1:
	totalcash += i[2]*i[1]

changerem=input('Amount of change to be given in cents ')

while changerem > totalcash:
	changerem=input('You do not have enough please try again ')

#if too much change to be given will substract value
#otherwise will run like ver 2
for i in currencies1:
	if changerem > 0:
		changegive = changerem // i[1]
		if changegive > i[2]:
			changerem -= i[2]*i[1]
			print "You give %r %s" % (i[2], i[0]) 
		else:
			changerem = changerem % i[1]
			if changegive > 0:
				print "You give %r %s" % (changegive, i[0])
