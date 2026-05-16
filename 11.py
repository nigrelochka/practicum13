board = [
    ["5","3",".",".","7",".",".",".","."],
    ["5",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

# Проверяем строки
for row in range(9):
    seen = []
    for col in range(9):
        cell = board[row][col]
        if cell != ".":
            if cell in seen:
                print("Ошибка в строке", row)
                exit()
            seen.append(cell)

# Проверяем столбцы
for col in range(9):
    seen = []
    for row in range(9):
        cell = board[row][col]
        if cell != ".":
            if cell in seen:
                print("Ошибка в столбце", col)
                exit()
            seen.append(cell)

# Проверяем квадраты 3x3
for square_row in range(3):      # 0, 1, 2
    for square_col in range(3):  # 0, 1, 2
        seen = []
        # Проходим по квадрату
        for i in range(3):
            for j in range(3):
                row = square_row * 3 + i
                col = square_col * 3 + j
                cell = board[row][col]
                if cell != ".":
                    if cell in seen:
                        print("Ошибка в квадрате", square_row, square_col)
                        exit()
                    seen.append(cell)

print("OK")