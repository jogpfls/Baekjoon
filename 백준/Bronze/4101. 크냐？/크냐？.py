while(True):
	first, second = map(int, input().split())
	if first == 0 and second == 0:
		break
	if first > second:
		print("Yes")
	else:
		print("No")