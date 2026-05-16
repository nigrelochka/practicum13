set1 = set(input().strip().split())
set2 = set(input().strip().split())
number = input().strip()

# Проверка принадлежности пересечению
if number in set1 and number in set2:
    print("YES")
else:
    print("NO")