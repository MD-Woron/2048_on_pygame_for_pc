from .compress import *
from .summing import *

def way(way,matrix_field):
    if way == 'a':
        matrix_field = compress_left(matrix_field)
        matrix_field = summing_left(matrix_field)
        matrix_field = compress_left(matrix_field)
    if way == 'd':
        matrix_field = compress_right(matrix_field)
        matrix_field = summing_right(matrix_field)
        matrix_field = compress_right(matrix_field)
    if way == 'w':
        matrix_field = compress_up(matrix_field)
        matrix_field = summing_up(matrix_field)
        matrix_field = compress_up(matrix_field)
    if way == 's':
        matrix_field = compress_down(matrix_field)
        matrix_field = summing_down(matrix_field)
        matrix_field = compress_down(matrix_field)

    return matrix_field