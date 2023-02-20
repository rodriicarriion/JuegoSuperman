import pygame, random
from configuracion import *

class obstaculo(pygame.sprite.Sprite):   #creación de la clase del molino, originalmente iba a ser un obstáculo pero ya no lo es
    def __init__(self):         # funcion que marca su configuración
        super().__init__()      
        self.image = pygame.image.load("obstaculo1.png")   #cargar la imágen
        self.valor = 500  #tamaño de la imagen
        self.image = pygame.transform.scale(self.image,(self.valor,self.valor)) #escalar la imagen con la variable anterior (pxs)
        self.rect = self.image.get_rect() 
        self.rect.y = 1000 - (193 + self.valor)  #ubicacion del eje y
        self.rect.x = ANCHO_PANTALLA          #ubicación del eje x
        self.speed = 3      # velocidad del movimiento (esta ha de ser la misma que la velocidad del suelo para dar la impresión 
                             #de que esta sobre el suelo)

    def update(self):  #función que marca el movimiento del molino
        if self.rect.x + self.valor <= 0:  #condicional con el que marcamos el movimiento sobre el eje x. 
            self.rect.x = 1300            #en caso de que el molino llegue al px 0 este reaparecerá en el 1300.
        else:#                              esto da la impresión de que hay varios molinos pero siempre es el mismo
            self.rect.x -= self.speed

            
    def draw(self, ventana):   #función que pinta el molino
        ventana.blit(self.image, self.rect)

class pajaro(pygame.sprite.Sprite):   # crecaión del objeto "pajaro"
    def __init__(self):    #función que marca su configuración
        super().__init__()
        self.image = pygame.image.load("pajaro.png")   #cargar la imagen
        self.valor = random.randint(50,150)     #tamaño aleatorio del pajaro entre ese rango de px
        self.image = pygame.transform.scale(self.image,(self.valor,self.valor))  #escalar la imagen para que no se deforme 
        self.rect = self.image.get_rect() 
        self.rect.y = random.randint(0, 700)   #ubicación aleatotia en el eje y
        self.rect.x = 1300     #ubicación del eje x
        self.speed = random.randrange(6,9)   #velocidad aleatoria entre 6 y 9
        self.radius = int(self.valor)//2     # marcar el radio del pajaro para detectar su colisión

    def update(self):    #funcion que marca el movimiento del pájaro
        if self.rect.x + self.valor <= 0: #condicional para mover el pajaro y reiniciar el el eje de y
            self.rect.x = 1300
            self.rect.y = random.randrange(0, 600)  #aparecer en px aleatorio del eje y entre 0 y 600
            self.speed = random.randrange(4,9)    #velocidad aleatoria
        else:
            self.rect.x -= self.speed

    def draw(self, ventana):  # función que pinta el pájaro
        ventana.blit(self.image, self.rect)

class arbol1(pygame.sprite.Sprite): # crecaión del objeto "arbol", también iba a ser un obstaculo pero finalmente no lo es
    def __init__(self): #función que marca su configuración
        super().__init__()
        self.image = pygame.image.load("arbol1.png") #cargar la imagen
        self.valor = 600  #tamañom de la imagen
        self.image = pygame.transform.scale(self.image,(self.valor,self.valor))  #escalar la imagen al tamaño seleccionado
        self.rect = self.image.get_rect() 
        self.rect.y = 1000 - (72 + self.valor)  #ubicación en el eje y
        self.rect.x = ANCHO_PANTALLA + 750   #ubicación en el eje x
        self.speed = 3   #velocidad del movimiento

    def update(self):   #funcion que marca el movimiento del árbol
        if self.rect.x + self.valor <= 0:   #condicional para mover el árbol y reiniciar el el eje de y
            self.rect.x = 1300
        else:
            self.rect.x -= self.speed

            
    def draw(self, ventana):    # función que pinta el árbol
        ventana.blit(self.image, self.rect)
