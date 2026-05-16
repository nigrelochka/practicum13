from itertools import permutations

# Чтение данных
numbers = input().strip().split()

# permutations сам выдаёт в лексикографическом порядке, если исходный список отсортирован
for perm in sorted(permutations(numbers)):
    print(' '.join(perm))