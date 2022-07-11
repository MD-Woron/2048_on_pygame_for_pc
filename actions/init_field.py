from random import randint as rnt
import pygame

def init_field(field_side):
    """
    Созадние квадратного поля для игры в 2048 со стороной field_side
    """
    matrix_field = []
    for i in range(field_side):
        matrix_field.append([])
        for i1 in range(field_side):
            matrix_field[i].append(0)
    return matrix_field


def random_fill(matrix_field):
    """
    помещает на случайное место в двумерном массиве число "2" или "4", если на этом месте не стоит 0
    """
    counter = 0
    x3 = rnt(0, 1)
    x1 = rnt(0, len(matrix_field) - 1)
    x2 = rnt(0, len(matrix_field) - 1)
    pygame.display.set_caption("Загрузка")
    while matrix_field[x1][x2] != 0:
        counter += 1
        x1 = rnt(0, len(matrix_field) - 1)
        x2 = rnt(0, len(matrix_field) - 1)
        if counter == 100000:

            return matrix_field
    if x3 == 0:
        matrix_field[x1][x2] = 2
    else:
        matrix_field[x1][x2] = 4

    return matrix_field

