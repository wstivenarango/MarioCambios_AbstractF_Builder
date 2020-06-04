from productos import *

class FabricaAbstracta():
    def crear_izquierda(self): pass
    def crear_derecha(self): pass
    def crear_arriba(self): pass
    def crear_abajo(self): pass
    def crear_poder(self): pass
    def crear_personaje(self): pass

class FabricaSpritesMario(FabricaAbstracta):
    def crear_izquierda(self):
        izquierda = IzquierdaMario()
        return izquierda.get_sprites()

    def crear_derecha(self):
        derecha = DerechaMario()
        return derecha.get_sprites()

    def crear_poder(self):
        Poder = PoderMario()
        return Poder.get_sprites()

    def crear_arriba(self):
        arriba = ArribaMario()
        return arriba.get_sprites()

    def crear_abajo(self):
        abajo = AbajoMario()
        return abajo.get_sprites()

    def crear_personaje(self):
        personaje = InicioMario()
        return personaje.get_sprites()    

class FabricaSpritesLuigi(FabricaAbstracta):
    def crear_izquierda(self):
        izquierda = IzquierdaLuigi()
        return izquierda.get_sprites()

    def crear_derecha(self):
        derecha = DerechaLuigi()
        return derecha.get_sprites()

    def crear_arriba(self):
        arriba = ArribaLuigi()
        return arriba.get_sprites()

    def crear_abajo(self):
        abajo = AbajoLuigi()
        return abajo.get_sprites()

    def crear_poder(self):
        Poder = PoderLuigi()
        return Poder.get_sprites()        

    def crear_personaje(self):
        personaje = InicioLuigi()
        return personaje.get_sprites()     