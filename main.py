import pygame, sys
from enemigos import Enemigos 

pygame.init()

ventana = pygame.display.set_mode((600,600))

game_over = False
enemigo = Enemigos()
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #Dibujar
   
    enemigo.dibujar(ventana)
    
    
    #Actualizar la ventana
    pygame.display.update()
