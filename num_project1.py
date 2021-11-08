a = int(input("Enter number of row: "))

for i in range(a):
	for j in range(a):
		if i == j or i + j == a-1:
			print(i+1, end=' ')
		else:
			print(' ', end=' ')
	print()