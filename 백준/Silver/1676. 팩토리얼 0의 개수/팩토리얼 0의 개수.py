N = int(input())
gob = 1
for i in range(1, N+1):
	gob *= i

count = 0
for i in range(1, N):
	if str(gob)[-i] == "0":
		count += 1
	else:
		break

print(count)