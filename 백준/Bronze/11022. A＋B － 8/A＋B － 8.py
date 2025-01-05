T = int(input())
hop = []
num1 = []
num2 = []
for i in range(T):
  text1, text2 = map(int, input().split())
  num1.append(text1)
  num2.append(text2)
  hop.append(text1+text2)

for i in range(T):
  print(f"Case #{i+1}: {num1[i]} + {num2[i]} = {hop[i]}")