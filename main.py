import pygame, sys
from enemigos import Enemigos 

pygame.init()

#Declaración de constantes
ANCHO = 600
LARGO = 600
FPS = 60
ventana = pygame.display.set_mode((ANCHO,LARGO))
tiempo = pygame.time.Clock()
jugando = True
enemigo = Enemigos()

#Lógica principal del juego
while jugando:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN: 
            enemigo.aparecer_enemigos(event)    
        if event.type == pygame.KEYUP:    
            enemigo.aparecer_enemigos(event)
       
            
    #Dibujar
    #enemigo.aparecer_enemigos()
    enemigo.dibujar(ventana)
    
    
    #Actualizar la ventana
    pygame.display.update()
    tiempo.tick(FPS)
   
