from ps4 import *

L = [35, 4, 5, 29, 17, 58, 0]

def selSort(L):
	for i in range(len(L)- 1):
		minIndx = i
		minVal = L[i]
		j = i+1 
		while j < len(L):
			if minVal > L[j]:
				minIndx = j
				minVal = L[j]
			j += 1
		temp = L[i]
		L[i] = L[minIndx]
		L[minIndx] = temp
	return L

print selSort(L)