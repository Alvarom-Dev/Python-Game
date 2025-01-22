import pygame, sys
from enemigos import Enemigos 
from matador import Matador

pygame.init()

#Declaración de constantes
ANCHO = 600
LARGO = 600
FPS = 60
BLACK = (0,0,0)
FONT = pygame.font.Font(None,20)
ventana = pygame.display.set_mode((ANCHO,LARGO))
texto_vida = FONT.render("VIDAS: ",0,(200,200,200))
texto_enemigos = FONT.render("ENEMIGOS ELIMINADOS",0,(200,200,200))
vidas = 3
tiempo = pygame.time.Clock()
jugando = True
enemigo = Enemigos()
matador = Matador()
segundos = 0
indice_anterior = 0
#Lógica principal del juego
while jugando:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
               

    #Movimiento del matador   

    matador.mov_matador(ANCHO)

    #Lógica de aparición y movilidad enemigos.

    contador= pygame.time.get_ticks()
    
    if contador < 90:
        enemigo.crear_enemigos(ANCHO)
    
    if contador - segundos >= 3000:
        enemigo.crear_enemigos(ANCHO)
        segundos = contador

   

    #Limpiamos la pantalla
    ventana.fill(BLACK)      
    
    #Dibujar
    ventana.blit(texto_vida,(1,1))
    ventana.blit(texto_enemigos,(1,20))
    enemigo.dibujar(ventana)
    matador.dibujar_matador(ventana)

    #Colision 
    
    #if enemigo.list_enemigos[-1].y + enemigo.largo_ene > matador.cord_y and enemigo.list_enemigos[-1].y < matador.cord_y + matador.ANCHO and enemigo.list_enemigos[-1].x + enemigo.ancho_ene > matador.cord_x and enemigo.list_enemigos[-1].x < matador.cord_x + matador.ANCHO:
    
    for colision in enemigo.list_enemigos:
        if colision.y + enemigo.largo_ene > matador.cord_y and colision.y < matador.cord_y + matador.ALTO and colision.x + enemigo.ancho_ene > matador.cord_x and colision.x < matador.cord_x + matador.ANCHO:
            print("Colisiona")
            sys.exit()
        else:
            print("No colisiona")    
    '''
    if len(enemigo.list_enemigos) > indice_anterior:
        print(enemigo.list_enemigos[-1])
    
    '''
    
    
    #Actualizar la ventana

    pygame.display.flip()
    tiempo.tick(FPS)
    
   
