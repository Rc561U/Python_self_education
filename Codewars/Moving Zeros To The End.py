a = [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]


#b = [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# zero = []
# for i in a:
# 	if a == 0:
# 		zero.append(a.pop())

def move_zeros(lst):
	result = list(filter(lambda x: x!=0, a))
	return result + ((len(lst)-len(result)) * [0])

print(move_zeros(a))