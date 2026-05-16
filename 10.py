from itertools import combinations

nums = list(map(int, input().strip().split(',')))

triplets = set()

for triplet in combinations(nums, 3):
    if sum(triplet) == 0:
        triplets.add(str(sorted(triplet)))

# Преобразуем обратно из строки в список
result = [eval(t) for t in sorted(triplets)]

print(result)