import pygame, random
from configuracion import *
from obstaculo import *


class jugador(pygame.sprite.Sprite):   #clase que crea el jugador
    def __init__(self):     #funcion que marca su configuración
        super().__init__()
        self.image = pygame.image.load("jugador.png")    #cargar la imágen
        self.image = pygame.transform.scale(self.image,(150,100))   #escalar la imagen al tamaño deseado
        self.rect = self.image.get_rect()
        self.height = 150     #altura
        self.rect.y = 100     #ubicación del eje de y
        self.rect.x = 500     #ubicación del eje de y
        self.velocidad = 6    # velocidad de movimiento
        self.radius = 100//3  # radio del jugador con el que detectar la colisións
        


    def update(self):   #funcion que marca el movimiento del jugador
        keys = pygame.key.get_pressed()   #variable con la que indicamos al programe que mire que teclas son pulsadas
        if self.rect.x <= 0:              #condicional para creal un limite para el jugador en el eje x
            self.rect.x = 0
        if self.rect.x >= 1200:           #condicional para creal un limite para el jugador en el eje x
            self.rect.x = 1200
        if self.rect.y <= 50:             #condicional para creal un limite para el jugador en el eje y
            self.rect.y = 50    
        if self.rect.y >= 700:            #condicional para creal un limite para el jugador en el eje y
            self.rect.y = 700

        if keys[pygame.K_UP]:               #marcar el movimiento de jugador cuando pulsas la flecha para arriba
            self.rect.y -= self.velocidad   
        if keys[pygame.K_DOWN]:             #marcar el movimiento de jugador cuando pulsas la flecha para abajo
            self.rect.y += self.velocidad
        if keys[pygame.K_LEFT]:             #marcar el movimiento de jugador cuando pulsas la flecha para la izquierda
            self.rect.x -= self.velocidad
        if keys[pygame.K_RIGHT]:            #marcar el movimiento de jugador cuando pulsas la flecha para la derecha
            self.rect.x += self.velocidad

    def draw(self,ventana):    #función que pinta el jugador
        ventana.blit(self.image, self.rect)