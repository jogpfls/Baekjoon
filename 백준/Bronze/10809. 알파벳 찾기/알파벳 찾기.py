array = [i*0-1 for i in range(26)]

S = input()
count = 0
for text in S:
  if(array[ord(text)-97] == -1):
    array[ord(text) - 97] = count
  count += 1

print(*array)