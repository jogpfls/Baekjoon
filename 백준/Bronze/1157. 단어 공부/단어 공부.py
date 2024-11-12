from collections import Counter

N = input().upper()

count = Counter(N)

max_count = max(count.values())

most_common = [char for char, freq in count.items() if freq == max_count]

if len(most_common) > 1:
    print("?")
else:
    print(most_common[0])
