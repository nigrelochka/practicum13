first_line = list(map(int, input().split()))
second_line = int(input().strip())

if first_line.count(second_line) > 1:
    print("YES")
else:
    print("NO")
