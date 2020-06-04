import sys
import pygame
import util
from pygame.locals import *
from heroe import *
from constructores import *
import copy

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 900
#ICON_SIZE = 32


def game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Mario_Cambios")
    background_image = util.cargar_imagen('imagenes/fondo.jpg')
    pygame.mouse.set_visible(False)
    director = Director()
    director.setBuilder(ConstructorLuigi())
    heroe = director.getHeroe()
    ejecutando = True
    jugando = True 
    while ejecutando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False
                sys.exit()
        screen.blit(background_image, (0, 0))
        if jugando:
            heroe.update(sprite)
            heroe.draw(screen)
        pygame.display.update()  

if __name__ == '__main__':
    game()

