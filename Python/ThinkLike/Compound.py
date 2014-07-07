def final_amt(p, r, n, t):
	a = p * (1 +r/n) ** (n*t)
	return a

toInvest = float(input('How much? \n'))
fnl= final_amt(toInvest, .08, 12, 5)
print ("you will have ", fnl)