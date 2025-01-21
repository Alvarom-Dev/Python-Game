import pygame, sys
from enemigos import Enemigos 
from matador import Matador

pygame.init()

#Declaración de constantes
ANCHO = 600
LARGO = 600
FPS = 60
BLACK = (0,0,0)
ventana = pygame.display.set_mode((ANCHO,LARGO))
tiempo = pygame.time.Clock()
jugando = True
enemigo = Enemigos()
matador = Matador()
segundos = 0

#Lógica principal del juego
while jugando:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
               
        if event.type == pygame.KEYDOWN: 
            pass   
        if event.type == pygame.KEYUP:    
            pass

    #Movimiento del matador   

    matador.mov_matador(ANCHO)

    #Lógica de aparición y movilidad enemigos.
    contador= pygame.time.get_ticks()
    
    if contador - segundos >= 3000:
        enemigo.crear_enemigos(ANCHO)
        segundos = contador

    #Limpiamos la pantalla
    ventana.fill(BLACK)      
    
    #Dibujar
    
    enemigo.dibujar(ventana)
    matador.dibujar_matador(ventana)
    
    #Actualizar la ventana

    pygame.display.flip()
    tiempo.tick(FPS)
    
   
