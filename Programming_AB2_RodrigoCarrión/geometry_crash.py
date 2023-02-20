import pygame, sys, random
from obstaculo import *                    #importar todo el codigo del fichero"obstaculo"
from jugador import *                         #importar todo el codigo del fichero"jugador"
from configuracion import *                 #importar todo el codigo del fichero"configuracion"
from fondo import *                        #importar todo el codigo del fichero"fondo"

pygame.init()                               #iniciar pygame
#Configuración ventana
ventana = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))       #configuramos y abrimos ventana con las variables
                                                                         #procedentes del fichero "configuracion"
#Zona creación de objetos                                                   Aquí creamos todos los objetos definidos en otros ficheros
miFondo1 = fondo1()
miFondo2 = fondo2()
miObstaculo = obstaculo()
miArbol1 = arbol1()

lista_pajaros = pygame.sprite.Group()          #creamos lista con el numero de pajaros que queramos que haya en el juego.
for i in range(8):
	miPajaro = pajaro()
	lista_pajaros.add(miPajaro)

miJugador = jugador()

sonidopajaro = pygame.mixer.Sound("sonidopajaro.wav")

clock = pygame.time.Clock()                 #Variable que sirve para definir la velocidad a la que queremos que transcurra el juego segun los fps
running = True
while running:                                #Bucle principal del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    hits = pygame.sprite.spritecollide(miJugador,lista_pajaros,True,pygame.sprite.collide_circle) 
                                                                    #variable que define como son las colisiones(entre que objetos, de que forma)
    if hits:           #bucle para aplicar las colisiones
        fuente = pygame.font.Font(None, 80)        
                                                                                 #añadir color y texto que quieres poner    
        HAS_PERDIDO = fuente.render("JAJAJA PERDISTE!", 1, (0, 0, 0))
                                                                               #ubicacion del texto   
        ventana.blit(HAS_PERDIDO, (ANCHO_PANTALLA/3.6, ALTO_PANTALLA/7))
                                                                                #actualizar pantalla    
        pygame.display.update()
        sonidopajaro.play()
        pygame.time.delay(1700)
        running = False
    
    ##Zona de pintado                               Zona donde se pintan todos los objetos creados
    miFondo1.draw(ventana)
    miFondo2.draw(ventana)
    miObstaculo.draw(ventana)
    miArbol1.draw(ventana)
    lista_pajaros.draw(ventana)
    miJugador.draw(ventana)

    ##Zona de movimiento
    miFondo1.update()
    miFondo2.update()
    miObstaculo.update()
    miArbol1.update()
    lista_pajaros.update()
    miJugador.update()

    clock.tick(80)                 #Velocidad en la que quieres que se muevan los fps por segundo

    pygame.display.flip()
pygame.quit()                       #en cuanto se acaba el bucle se cierra la ventana    