from ps4 import *


# for i in range(28):
# 	print len(apply_shift('Do Androids Dream of Electric Sheep?', i))

t = apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
print t
print 'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'




# L = [35, 4, 5, 29, 17, 58, 0]

# def selSort(L):
# 	for i in range(len(L)- 1):
# 		minIndx = i
# 		minVal = L[i]
# 		j = i+1 
# 		while j < len(L):
# 			if minVal > L[j]:
# 				minIndx = j
# 				minVal = L[j]
# 			j += 1
# 		temp = L[i]
# 		L[i] = L[minIndx]
# 		L[minIndx] = temp
# 	return L

# print selSort(L)

# def merge(left, right, lt):
# 	

# strs = "hello, world!"
# lis = []
# for c in strs:
#     if c.isalnum() or c.isspace():
#         lis.append(c)
#     else:
#         lis.append(' ')

# new_strs = "".join(lis)
# print new_strs           #print 'Johnny Appleseed is a good farmer'
# print new_strs.split()         #prints ['Johnny', 'Appleseed', 'is', 'a', 'good', 'farmer