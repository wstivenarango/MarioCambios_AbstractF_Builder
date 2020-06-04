import pygame
from pygame.sprite import Sprite
from pygame import *


class Heroe(Sprite):
    def __init__(self):
        Sprite.__init__(self)

    def set_sprites(self, sprite):
        
        self.imagenes = sprite
  
    def update(self,sprite):
        self.image= self.imagenes[5]      
        teclas = pygame.key.get_pressed()
        if teclas[K_LEFT]:
            self.image=self.imagenes[1]
        if teclas[K_RIGHT]:
            self.image= self.imagenes[0]
        if teclas[K_UP]:
            self.image= self.imagenes[3]
        if teclas[K_DOWN]:
            self.image= self.imagenes[2]
        if teclas[K_SPACE]:
            self.image= self.imagenes[4]


    def draw(self, screen):
        screen.blit(self.image, (410,560))
