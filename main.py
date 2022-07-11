from actions import *

# def database_update_best_time(time):
#     db = open('bd.txt', 'r')
#     old_time = db.readline()
#     if time < int(old_time):
#         db.close()
#         db = open('bd.txt', 'w')
#         db.write(str(time))
#         return time
#     return old_time


import pygame

matrix_field = init_field(font_size) # ВАЖНО
matrix_field = random_fill(matrix_field)

import time
start_time = time.time()


flag = True
max_number = 0
while flag:
    clock.tick(FPS)
    max_number = max_number if max_number == 2049 else 1
    flag = False
    for i in range(len(matrix_field)):
        for i1 in range(len(matrix_field)):
            try:
                if matrix_field[i][i1] == matrix_field[i][i1 + 1] or matrix_field[i1][i] == matrix_field[i1 + 1][i] or matrix_field[i][i1] == 0:
                    flag = True
                    break
            except IndexError:
                pass
    if not (flag):
        pygame.quit()
        break
    for i in range(len(matrix_field)):
        for i1 in range(len(matrix_field)):
            if matrix_field[i][i1] > max_number:
                max_number = matrix_field[i][i1]
    while max_number == 2048:
        game_time = int(round(time.time() - start_time, 0))
        #best_time = database_update_best_time(game_time)
        screen.fill((BLACK))
        win = pygame.image.load('win.bmp')
        win = pygame.transform.scale(win, WINSIZE)
        win_rect = win.get_rect(bottomright = WINSIZE)
        screen.blit(win,win_rect)
        pygame.display.flip()
        #pygame.display.set_caption(f"Your best time is {best_time} sec")
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
                matrix_field = way('s',matrix_field)
                matrix_field = random_fill(matrix_field)
                pygame.display.set_caption("2048")
            if event.key == pygame.K_w:
                matrix_field = way('w', matrix_field)
                matrix_field = random_fill(matrix_field)
                pygame.display.set_caption("2048")
            if event.key == pygame.K_a:
                matrix_field = way('a', matrix_field)
                matrix_field = random_fill(matrix_field)
                pygame.display.set_caption("2048")
            if event.key == pygame.K_d:
                matrix_field = way('d', matrix_field)
                matrix_field = random_fill(matrix_field)
                pygame.display.set_caption("2048")
    screen.fill((WHITE))
    count_str = 0
    for stroka in matrix_field:
        count_str += 1
        count_number = 0
        for number in stroka:
             count_number += 1
             number_rect = numbers[number].get_rect(bottomright = (count_number*number_height[0], count_str*number_height[1]))
             screen.blit(numbers[number],number_rect)
    pygame.display.flip()

