from itertools import combinations

numbers = input().strip().split()

#для упорядоченного вывода
numbers.sort()

#список всех подмножеств
subsets = []

#подмножества всех размеров от 0 до len(numbers)
for r in range(len(numbers) + 1):
    for combo in combinations(numbers, r):
        subsets.append(combo)

for subset in subsets:
    print(' '.join(subset))