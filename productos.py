import util

class Abajo():
    def get_sprites(self): pass

class AbajoMario(Abajo):
    def get_sprites(self):
        return util.cargar_imagen('imagenes/mario_down.png')

class AbajoLuigi(Abajo):
    def get_sprites(self):
        return util.cargar_imagen('imagenes/luigi_down.png')

class Arriba():
    def get_sprites(self): pass

class ArribaMario(Arriba):
    def get_sprites(self):
        return util.cargar_imagen('imagenes/mario_up.png')

class ArribaLuigi(Arriba):
    def get_sprites(self):
        return util.cargar_imagen('imagenes/luigi_up.png')

class Derecha():
    def get_sprites(self): pass

class DerechaMario(Derecha):
    def get_sprites(self):
        return util.cargar_imagen('imagenes/mario_right.png')

class DerechaLuigi(Derecha):
    def get_sprites(self):
        return util.cargar_imagen('imagenes/luigi_right.png')

class Izquierda():
    def get_sprites(self): pass

class IzquierdaMario(Izquierda):
    def get_sprites(self):
        return util.cargar_imagen('imagenes/mario_left.png')

class IzquierdaLuigi(Izquierda):
    def get_sprites(self):
        return util.cargar_imagen('imagenes/luigi_left.png')

class Poder ():
    def get_sprites(self): pass


class PoderMario (Poder):
    def get_sprites(self):
        return util.cargar_imagen('imagenes/poder.png')

class PoderLuigi (Poder):
    def get_sprites(self):
        return util.cargar_imagen('imagenes/poder.png')        

class Inicio ():
    def get_sprites(self): pass

class InicioMario (Inicio):
    def get_sprites(self):
        return util.cargar_imagen('imagenes/mario.png')

class InicioLuigi (Inicio):
    def get_sprites(self):
        return util.cargar_imagen('imagenes/luigi.png')                    