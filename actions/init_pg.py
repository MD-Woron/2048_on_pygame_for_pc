import sys
import os


def resource_path(relative_path):
    base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


import pygame
import ctypes


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

numbers = dict()

numbers[0] = pygame.transform.scale(pygame.image.load('0.bmp'), (number_height))

for i in range(1,12):
    n = 2**i
    asset_url = resource_path(f'{n}.bmp')
    number = pygame.image.load(asset_url)
    number.set_colorkey((255,255,255))
    number = pygame.transform.scale(number,number_height)
    numbers[n] = number

