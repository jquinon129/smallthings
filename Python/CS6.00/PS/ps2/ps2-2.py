# Implement the compute_deriv function. This function computes the derivative of
# a polynomial function. It takes in a tuple of numbers poly and returns the
# derivative, which is also a polynomial represented by a tuple.

def compute_deriv(poly):
	res = ( )
	for i in range(1, len(poly) ):
		res = res + (poly[i] * i, )
	return res

poly = [-13.39, 0.0, 17.5, 3.0, 1.0]
print compute_deriv(poly)

