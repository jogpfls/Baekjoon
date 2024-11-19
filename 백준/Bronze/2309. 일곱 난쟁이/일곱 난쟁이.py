count = 0
array = []
flag = True

for _ in range(9):
    N = int(input())
    array.append(N)
    count += N

for i in range(8):
    for j in range(i+1, 9):
        if array[i] + array[j] == count-100:
            array.pop(j)
            array.pop(i)
            flag = False
            break
    if(flag == False):
        break
            

for value in sorted(array):
    print(value)
