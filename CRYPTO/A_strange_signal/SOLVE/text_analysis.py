import sys

file = open(sys.argv[1], 'r').read()
arr_simb = []
for i in file:
	if(i not in arr_simb):
		arr_simb.append(i)
arr_simb = sorted(arr_simb)
#print(len(arr_simb))
new_arr = []
for i in arr_simb:
	q = 0
	for j in file:
		if (i == j):
			q += 1
	new_arr.append([i, round(q/len(file), 5)])
arr_A, arr_B = [], []
for i in new_arr:
	arr_A.append(i[0])
	arr_B.append(i[1])
print(arr_A)
print(arr_B)
#print(sum(arr_B), len(file))
