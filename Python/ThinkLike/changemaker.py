_memo = {}
 
def make_change(change, denoms):
	return _make_change(change, sorted(denoms, reverse=True))
 
def _make_change(cents, denoms):
	if cents in _memo:
		return _memo[cents]

	ways = []
	for denom in denoms:
		if cents == denom:
			ways.append([denom])
		if cents > denom:
			remainder = cents - denom
			for way in _make_change(remainder, denoms):
				if way[0] <= denom:
					ways.append([denom] + way)
	_memo[cents] = ways
	return ways
 

# make change for a 25 cents
for way in make_change(25, [1, 5, 10, 25]):
	print way