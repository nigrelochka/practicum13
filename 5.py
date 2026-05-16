n = int(input())

# Все числа от 2 до n-1
all_numbers = set(range(2, n))

# Тут будем хранить простые числа
primes = set()

# Пока есть числа в множестве
while len(all_numbers) > 0:
    # Берем первое попавшееся число (превращаем множество в список и берем первый элемент)
    p = list(all_numbers)[0]
    primes.add(p)

    # Удаляем из all_numbers все числа, которые делятся на p
    for num in list(all_numbers):
        if num % p == 0:
            all_numbers.remove(num)

print(sorted(primes))