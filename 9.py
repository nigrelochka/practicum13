from itertools import combinations

numbers = input().strip().split()
k = int(input())

# Сортируем для лексикографического порядка вывода
numbers.sort()

# Генерируем все K-элементные подмножества
for subset in combinations(numbers, k):
    print(' '.join(subset))