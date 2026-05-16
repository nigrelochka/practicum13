print("Результаты расшифровки ХОД+ХОД+ХОД=МАТ:")

for hod in range(100, 334):  # 334*3 > 999
    # Цифры ХОД
    X = hod // 100
    O = (hod // 10) % 10
    D = hod % 10

    # Проверка, что цифры ХОД разные
    if X == O or X == D or O == D:
        continue

    # Результат МАТ = 3 * ХОД
    mat = hod * 3
    if mat >= 1000:
        continue

    M = mat // 100
    A = (mat // 10) % 10
    T = mat % 10

    # Проверка, что цифры МАТ разные
    if M == A or M == T or A == T:
        continue

    # Проверка, что все 6 букв разные цифры
    if len({X, O, D, M, A, T}) == 6:
        print(f"{hod}+{hod}+{hod}={mat}")