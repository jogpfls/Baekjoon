arr = []
num = []
for i in range(0, 28):
	arr.append(int(input()))

for i in range(1, 31):
	if i not in arr:
		num.append(i)

for i in range(len(num)):
	print(num[i])