# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

x = 600851475143 
b = 0

for i in range(int(x ** .5)+1):		#range avoids repeats
	if (x % (i+1) == 0):
		b = i+1
		print '%r is a factor' % b	#finds if it's NOT a prime
		for i in range(3,int(b ** .5)+1,2):
			if  (b % i == 0):
				print '%r is NOT a prime' % b


