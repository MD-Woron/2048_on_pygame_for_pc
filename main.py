import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


from random import randint as rnt


def compress_a(l):
    """
    В случае хода справа налево
    Двигаясь слева направо проверяет наличие ноликов, а если их находит, то кидает в конец через append
    Мне лень писать более развёрнуто, так что вот пример
    0 2 2 2 >>>> 2 2 2 0
    """
    for i in range(len(l)):
        temp = 0
        for i1 in range(len(l)):
            if l[i][temp] == 0:
                l[i].pop(temp)
                l[i].append(0)
            else:
                temp += 1

    return (l)


def summa_a(l):
    """
    В случае хода справа налево
    Двигаясь слева направо суммирует элементы, если они равны
    Результат записывается в левый объект
    0 0 2 2 >>> 0 0 4 0
    """
    for i in range(len(l)):
        flag = True
        for i1 in range(len(l) - 1):
            if l[i][i1] == l[i][i1 + 1] and flag:
                l[i][i1] += l[i][i1 + 1]
                l[i][i1 + 1] = 0
                flag = False
            else:
                flag = True
    return (l)


def compress_d(l):
    """
    В случае с ходом слева направо
    Двигается справа налево до элемента с индексом -len + 1 т.к. это ссто процентов либо 0, либо число, с кучей чисел перед ним
    и находит 0.
    Ести находит 0, то помещает его в начало строки и удаляет из места нахождения
    """
    for i in range(len(l)):
        temp = -1
        for i1 in range(len(l)):
            if l[i][temp] == 0 and abs(temp) < len(l):
                l[i].pop(temp)
                l[i].insert(0, 0)
            else:
                temp -= 1
    return (l)


def summa_d(l):
    """
    В случае с ходом слева направо находит рядомстоящие элементы и если они совпадают, то
    Прибавляет к значению правого значение левого
    """
    for i in range(len(l)):
        for i1 in range(len(l) - 1):
            if l[i][i1 + 1] == l[i][i1]:
                l[i][i1 + 1] += l[i][i1]
                l[i][i1] = 0
    return (l)


def compress_w(l):
    for j in range(len(l)):
        i = 0  # индекс текущей строки
        s = 0  # индекс первого числа, не являющегося 0
        while i < len(
                l) - s:  # пока индекс строки меньше длинны строки ( работает только в случае если матрица квадратная ) минус индекса первого числа, не явл. 0
            # другими словами: нас интересуют только числа, являющиеся нулями в строке, их переносим в конец
            if l[i][j] == 0:  # итак, проверяем, что число являкется нулём
                k = i  # заносим индекс строки в отдельную переменную, чтобы ещё можно было изменять в цикле while
                s += 1  # переносим наш "указатель" на следующее число, так как предыдущее явл. 0 и нас не интересует
                while k < (len(l) - 1):  # тут можно было использовать for k in range(k, len(l)-1), но ладно
                    l[k][j] = l[k + 1][j]  # теперь вместо нолика в строке стоит элемент следующей строки на j'том месте
                    # другими словами: 0 0 0 >> 1 0 0
                    #                  0 0 0 >> 0 0 0
                    #                  1 0 0 >> 1 0 0
                    k += 1  # тупо переборный элемент, ничерта интересного!!!!!
                l[len(l) - 1][
                    j] = 0  # последний элемент ( можно было юзать -1, но замес об этом не знал ) теперь становится 0
            # другими словами: 1 0 0 >> без изм.
            #                  0 0 0 >> без изм.
            #                  1 0 0 >> 0 0 0
            # итого результат вроде должен быть заебись
            else:  # иначе переходим на следующую строку
                i += 1
    return (l)


def compress_s(l):
    l = list(reversed(l))
    for j in range(len(l)):
        i = 0
        s = 0
        while i < len(l) - s:
            if l[i][j] == 0:
                k = i
                s += 1
                for k in range(k, len(l) - 1):
                    l[k][j] = l[k + 1][j]
                    k += 1
                l[-1][j] = 0
            else:
                i += 1
    l = list(reversed(l))
    return (l)


def summa_s(l):
    for i in range(len(l)):
        for i1 in range(len(l) - 1, 0, -1):
            if l[i1][i] == l[i1 - 1][i]:
                l[i1][i] += l[i1 - 1][i]
                l[i1 - 1][i] = 0
    return (l)


def summa_w(l):
    for i in range(len(l)):
        for i1 in range(len(l) - 1):
            if l[i1][i] == l[i1 + 1][i]:
                l[i1][i] += l[i1 + 1][i]
                l[i1 + 1][i] = 0
    return (l)


def random(l):
    """
    помещает на случайное место в двумерном массиве число "2" или "4", если на этом месте не стоит 0
    """
    counter = 0
    x3 = rnt(0, 1)
    x1 = rnt(0, len(l) - 1)
    x2 = rnt(0, len(l) - 1)
    pygame.display.set_caption("Загрузка")
    while l[x1][x2] != 0:
        counter += 1
        x1 = rnt(0, len(l) - 1)
        x2 = rnt(0, len(l) - 1)
        if counter == 100000:
            return(l)
    if x3 == 0:
        l[x1][x2] = 2
    else:
        l[x1][x2] = 4
    return (l)


def init2048(field_side):
    """
    Созадние квадратного поля для игры в 2048 со стороной field_side
    """
    l = []
    for i in range(field_side):
        l.append([])
        for i1 in range(field_side):
            l[i].append(0)
    return(l)

def way(way,l):
    if way == 'a':
        l = compress_a(l)  # из 0 2 2 2 >>>>>> 2 2 2 0
        l = summa_a(l)  # из 2 2 2 0 >>>> 4 0 2 0
        l = compress_a(l)  # из 4 0 2 0 >>>> 4 2 0 0
    if way == 'd':
        l = compress_d(l)  # аналогично
        l = summa_d(l)
        l = compress_d(l)
    if way == 'w':
        l = compress_w(l)
        l = summa_w(l)
        l = compress_w(l)
    if way == 's':
        l = compress_s(l)
        l = summa_s(l)
        l = compress_s(l)
    return(l)

def database_update_best_time(time):
    db = open('bd.txt', 'r')
    old_time = db.readline()
    if time < int(old_time):
        db.close()
        db = open('bd.txt', 'w')
        db.write(str(time))
        return time
    return old_time

def set_size(text, color):
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                if event.key == pygame.K_RETURN:
                    return int(text)
                text += event.unicode
                screen.fill((30,30,30))
                text_surface = font.render(text, True, color)
                screen.blit(text_surface, (50,100))
                pygame.display.flip()

import pygame
import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

WIDTH = screensize[0]//2
HEIGHT = screensize[1]//2
FPS = 60
WINSIZE = (screensize[0]//2,screensize[1]//2)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()

font_color = pygame.Color('dodgerblue2')

pygame.display.set_caption("Введите размер поля")
font = pygame.font.SysFont('arial', 32)
text = ''


screen = pygame.display.set_mode((WIDTH, HEIGHT))
font_size = set_size(text,font_color)
pygame.display.set_caption("2048")
clock = pygame.time.Clock()


number_height = tuple(map(lambda param: param//2//font_size, screensize))

numbers = [0]*2049
numbers[0] = pygame.transform.scale(pygame.image.load('0.bmp'), (number_height))
for i in range(1,12):
    n = 2**i
    asset_url = resource_path(f'{n}.bmp')
    number = pygame.image.load(asset_url)
    number.set_colorkey((255,255,255))
    number = pygame.transform.scale(number,number_height)
    numbers[n] = number

l = init2048(font_size) # ВАЖНО


import time
start_time = time.time()


flag = True
max_number = 0
while flag:
    clock.tick(FPS)
    max_number = max_number if max_number == 2049 else 1
    flag = False
    for i in range(len(l)):
        for i1 in range(len(l)):
            try:
                if l[i][i1] == l[i][i1 + 1] or l[i1][i] == l[i1 + 1][i] or l[i][i1] == 0:
                    flag = True
                    break
            except IndexError:
                pass
    if not (flag):
        pygame.quit()
        break
    for i in range(len(l)):
        for i1 in range(len(l)):
            if l[i][i1] > max_number:
                max_number = l[i][i1]
    while max_number == 2048:
        game_time = int(round(time.time() - start_time, 0))
        best_time = database_update_best_time(game_time)
        screen.fill((BLACK))
        win = pygame.image.load('win.bmp')
        win = pygame.transform.scale(win, WINSIZE)
        win_rect = win.get_rect(bottomright = WINSIZE)
        screen.blit(win,win_rect)
        pygame.display.flip()
        pygame.display.set_caption(f"Your best time is {best_time} sec")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                flag = False
                break
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    max_number += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flag = False
            break
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                l = way('s',l)
                l = random(l)
                pygame.display.set_caption("2048")
            if event.key == pygame.K_w:
                l = way('w', l)
                l = random(l)
                pygame.display.set_caption("2048")
            if event.key == pygame.K_a:
                l = way('a', l)
                l = random(l)
                pygame.display.set_caption("2048")
            if event.key == pygame.K_d:
                l = way('d', l)
                l = random(l)
                pygame.display.set_caption("2048")
    screen.fill((WHITE))
    count_str = 0
    for stroka in l:
        count_str += 1
        count_number = 0
        for number in stroka:
            count_number += 1
            number_rect = numbers[number].get_rect(bottomright = (count_number*number_height[0], count_str*number_height[1]))
            screen.blit(numbers[number],number_rect)
    pygame.display.flip()

