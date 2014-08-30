# Implement the evaluate_poly function. This function evaluates a polynomial
# function for the given x value. It takes in a tuple of numbers poly and a
# number x. By number, we mean that x and each element of poly is a float.
# evaluate_poly takes the polynomial represented by poly and computes its value
# at x. It returns this value as a float.

def evaluate_poly(poly, x):
	res = 0.0
	for i in range(len(poly)):
		res += poly[i] * (x ** i)
	return res 

poly = (0.0, 0.0, 5.0, 9.3, 7.0)
x = -13
print evaluate_poly(poly, x)
