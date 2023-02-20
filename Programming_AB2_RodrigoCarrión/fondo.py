
import pygame
from configuracion import *


class fondo1(pygame.sprite.Sprite):  #Clase que crea el fondo de las montañas                   
    def __init__(self):         #funcion de la configuración del fondo
        super().__init__()
        self.image = pygame.image.load("fondo.jpg").convert()  #selección de la imágen
        self.y = 0  #ubicación de la imágen en el eje de y
        self.x = 0  #ubicación de la imagen en el eje de x

    def draw(self,ventana):   #funcion que pinta el fondo en la ventana
        ventana.blit(self.image, (self.x, self.y))
        
class fondo2(pygame.sprite.Sprite):   #Clase que crea el suelo
    def __init__(self):  #funcion de la configuración del suelo
        super().__init__()
        self.image = pygame.image.load("suelo.jpg")   #selección de la imágen
        self.x = 0      #ubicación de la imagen en el eje de x
        self.y =800     #ubicación de la imágen en el eje de y
    
    def update(self):   #funcion de la configuración del movimiento del suelo
        self.x -= 3     # a que velocidad se mueve el suelo
        if self.x <= -60:   #si el eje de x llega al FPS -60 vuelve a pintarse 
            self.x = 0#      en el pixel 0. Se pinta todo el rato el mismo trozo
                             # de suelo dando la impresión del movimiento
        

    def draw(self,ventana):  #función que pinta el suelo
        ventana.blit(self.image, (self.x, self.y)) 
        