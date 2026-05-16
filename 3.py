sweet_tooth = set(input().strip().split())
n = int(input())

# Множество всего, что нравится друзьям
friends_likes = set()

for _ in range(n):
    friends_likes.update(input().strip().split())

# Продукты, которые нравятся только Сладкоежкину
only_sweet_tooth = sweet_tooth - friends_likes

print(len(only_sweet_tooth))