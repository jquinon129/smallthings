
def evaluate_poly(poly, x):
	res = 0.0
	for i in range(len(poly)):
		res += poly[i] * (x ** i)
	return res 


def compute_deriv(poly):
	res = ( )
	for i in range(1, len(poly) ):
		res = res + (poly[i] * i, )
	return res

def compute_root(poly, x_0, epsilon):
	number = 1
	while True:
		if abs(evaluate_poly(poly, x_0)) > epsilon:
			number += 1
			x_0 -= evaluate_poly(poly, x_0) / evaluate_poly(compute_deriv(poly), x_0)
		else:
			break
	return x_0, number

poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
x_0 = .1
epsilon = .0001
print compute_root(poly, x_0, epsilon)

