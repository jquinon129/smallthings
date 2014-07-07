cash=input()

quarters = 0
dimes = 0
nickels = 0
pennies = 0
changerem = cash



#change given by value
if cash > 0:
	quarters = cash// 25
	changerem = cash % 25
if changerem >= 10:
	dimes = changerem // 10
	changerem = changerem % 10
if changerem >=5:
	nickels = changerem // 5
	changerem = changerem % 5
if changerem >= 1:
	pennies = changerem // 1
	changerem = changerem %1

print "Your change is %r quarters, %r dimes, %r nickels, and %r pennies" % (quarters, dimes, nickels, pennies)

#total number of combinations per value 
#need to revise, stack overflow
comquart =  12
comdim = 4
comnick = 2
compen = 1
totcom = comquart*quarters + comdim*dimes + comnick*nickels + compen * pennies
print "There are %r ways of giving this change out" % totcom