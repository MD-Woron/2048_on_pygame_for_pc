def compress_down(matrix_field):
    """
    Логика идентична модулю "compress_up", за исключением того, что поле 2 раза переворачивается:
    В начале и в конце
    """
    matrix_field = list(reversed(matrix_field))
    for j in range(len(matrix_field)):
        i = 0
        s = 0
        while i < len(matrix_field) - s:
            if matrix_field[i][j] == 0:
                k = i
                s += 1
                for k in range(k, len(matrix_field) - 1):
                    matrix_field[k][j] = matrix_field[k + 1][j]
                    k += 1
                matrix_field[-1][j] = 0
            else:
                i += 1
    matrix_field = list(reversed(matrix_field))

    return matrix_field


def compress_left(matrix_field):
    """
    В случае хода справа налево
    Двигаясь слева направо проверяет наличие ноликов, а если находит, то удаляет 0
    а потом помещает его в конец
    0 2 2 2 >>>> 2 2 2 0
    """
    for i in range(len(matrix_field)):
        temp = 0
        for i1 in range(len(matrix_field)):
            if matrix_field[i][temp] == 0:
                matrix_field[i].pop(temp)
                matrix_field[i].append(0)
            else:
                temp += 1

    return matrix_field



def compress_right(matrix_field):
    """
    В случае с ходом слева направо
    Двигается справа налево до элемента с индексом -len + 1
    и ищет 0.
    Ести находит 0, то сначала удаляет его из ячейки, потом добавляет в начало строки
    """
    for i in range(len(matrix_field)):
        temp = -1
        for i1 in range(len(matrix_field)):
            if matrix_field[i][temp] == 0 and abs(temp) < len(matrix_field):
                matrix_field[i].pop(temp)
                matrix_field[i].insert(0, 0)
            else:
                temp -= 1

    return matrix_field


def compress_up(matrix_field):
    for j in range(len(matrix_field)):
        i = 0  # индекс текущей строки
        s = 0  # индекс первого числа, не являющегося 0
        while i < len(matrix_field) - s:  # пока индекс строки меньше длинны строки ( работает только в случае если матрица квадратная ) минус индекса первого числа, не явл. 0
            # другими словами: нас интересуют только числа, являющиеся нулями в строке, их переносим в конец
            if matrix_field[i][j] == 0:  # итак, проверяем, что число являкется нулём
                k = i  # заносим индекс строки в отдельную переменную, чтобы ещё можно было изменять в цикле while
                s += 1  # переносим наш "указатель" на следующее число, так как предыдущее явл. 0 и нас не интересует
                while k < (len(matrix_field) - 1):  # тут можно было использовать for k in range(k, len(l)-1), но ладно
                    matrix_field[k][j] = matrix_field[k + 1][j]  # теперь вместо нолика в строке стоит элемент следующей строки на j'том месте
                    # другими словами: 0 0 0 >> 1 0 0
                    #                  0 0 0 >> 0 0 0
                    #                  1 0 0 >> 1 0 0
                    k += 1  # тупо переборный элемент, ничерта интересного!!!!!
                matrix_field[len(matrix_field) - 1][
                    j] = 0  # последний элемент ( можно было юзать -1, но замес об этом не знал ) теперь становится 0
            # другими словами: 1 0 0 >> без изм.
            #                  0 0 0 >> без изм.
            #                  1 0 0 >> 0 0 0
            else:  # иначе переходим на следующую строку
                i += 1

    return matrix_field
