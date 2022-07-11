def summing_down(matrix_field):
    """
    Двигаясь сверху вниз суммируем одинаковые элементы
    Результат записывается в нижнюю ячейку
    """
    for i in range(len(matrix_field)):
        for i1 in range(len(matrix_field) - 1, 0, -1):
            if matrix_field[i1][i] == matrix_field[i1 - 1][i]:
                matrix_field[i1][i] += matrix_field[i1 - 1][i]
                matrix_field[i1 - 1][i] = 0

    return matrix_field


def summing_left(matrix_field):
    """
    В случае хода справа налево
    Двигаясь слева направо суммирует элементы, если они равны
    Результат записывается в левую ячейку матрицы
    0 0 2 2 >>> 0 0 4 0
    """
    for i in range(len(matrix_field)):
        flag = True
        for i1 in range(len(matrix_field) - 1):
            if matrix_field[i][i1] == matrix_field[i][i1 + 1] and flag:
                matrix_field[i][i1] += matrix_field[i][i1 + 1]
                matrix_field[i][i1 + 1] = 0
                flag = False
            else:
                flag = True

    return matrix_field


def summing_right(matrix_field):
    """
    В случае с ходом слева направо находит рядомстоящие элементы и если они совпадают, то
    Прибавляет к значению правого значение левого
    """
    for i in range(len(matrix_field)):
        for i1 in range(len(matrix_field) - 1):
            if matrix_field[i][i1 + 1] == matrix_field[i][i1]:
                matrix_field[i][i1 + 1] += matrix_field[i][i1]
                matrix_field[i][i1] = 0

    return matrix_field


def summing_up(matrix_field):
    """
     Двигаясь снизу вверх суммирует одинаковые элементы
     Результат записывается в верхнюю ячейку
    """
    for i in range(len(matrix_field)):
        for i1 in range(len(matrix_field) - 1):
            if matrix_field[i1][i] == matrix_field[i1 + 1][i]:
                matrix_field[i1][i] += matrix_field[i1 + 1][i]
                matrix_field[i1 + 1][i] = 0

    return matrix_field