from fabricas import *
from heroe import *

class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getHeroe(self):
        heroe = Heroe()
        heroe.set_sprites(self.__builder.get_sprites())
        return heroe

class Constructor():
    def get_sprites(self): pass

class ConstructorMario(Constructor):
    def __init__(self):
        self.fabrica = FabricaSpritesMario()

    def get_sprites(self):
        return [self.fabrica.crear_derecha(),
                self.fabrica.crear_izquierda(),
                self.fabrica.crear_abajo(),
                self.fabrica.crear_arriba(),
                self.fabrica.crear_poder(),
                self.fabrica.crear_personaje()]


class ConstructorLuigi(Constructor):
    def __init__(self):
        self.fabrica = FabricaSpritesLuigi()

    def get_sprites(self):
        return [self.fabrica.crear_derecha(),
                self.fabrica.crear_izquierda(),
                self.fabrica.crear_abajo(),
                self.fabrica.crear_arriba(),
                self.fabrica.crear_poder(),
                self.fabrica.crear_personaje()]

