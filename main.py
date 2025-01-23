import pygame, sys
from enemigos import Enemigos 
from matador import Matador

pygame.init()
pygame.display.set_caption("Juego Naves")

#Declaración de constantes
ANCHO = 600
LARGO = 600
FPS = 60
BLACK = (0,0,0)
BLANCO =(255,255,255)
ROJO = (255,0,0)
FONT = pygame.font.SysFont("Calibri",20)
font_gameover = pygame.font.Font(None,80)
ventana_juego = pygame.display.set_mode((ANCHO,LARGO))
ventana_gameover = pygame.display.set_mode((ANCHO,LARGO))
vidas = 3
tiempo = pygame.time.Clock()
jugando = True
enemigo = Enemigos()
matador = Matador()
segundos = 0
controlador_segundos = 2000
contador_eliminaciones = 0

#Lógica principal del juego
while jugando:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                matador.crear_balas()    

    #Movimiento del matador   

    matador.mov_matador(ANCHO)

    #Lógica de aparición y movilidad enemigos.

    contador= pygame.time.get_ticks()
    
    if contador - segundos >= controlador_segundos:
        enemigo.crear_enemigos(ANCHO)
        segundos = contador
    
    if contador_eliminaciones > 5:
        enemigo.velocidad_y= 3
        controlador_segundos = 1000
    
    if contador_eliminaciones > 10:
        controlador_segundos = 800

    #Limpiamos la pantalla

    ventana_juego.fill(BLACK)      
    
    #Renderizado de textos
    text_vida = f"Vidas: {vidas}"
    texto_vida = FONT.render(text_vida,True,BLANCO)
    text_enemigo = f"Kills enemigos: {contador_eliminaciones}"
    texto_enemigos = FONT.render(text_enemigo,True,BLANCO)

    #Dibujar
    ventana_juego.blit(texto_vida,(1,10))
    ventana_juego.blit(texto_enemigos,(1,30))
    enemigo.dibujar_enemigos(ventana_juego)
    matador.dibujar_matador(ventana_juego)
    matador.dibujar_balas(ventana_juego)

    #Colision y gestion de vidas
    
    for enemy in enemigo.list_enemigos:
        if enemy.y + enemigo.largo_ene > matador.cord_y and enemy.y < matador.cord_y + matador.ALTO and enemy.x + enemigo.ancho_ene > matador.cord_x and enemy.x < matador.cord_x + matador.ANCHO:
            pygame.time.delay(500)
            enemy.y = 600
            vidas -= 1
        elif enemy.y + enemigo.largo_ene > ANCHO and enemy.y + enemigo.largo_ene < ANCHO + 3:
            vidas -=1     
        
        elif vidas <= 0:
            ventana_juego.fill(BLACK)
            texto_game_over = font_gameover.render("GAME OVER",0,ROJO)
            ventana_juego.blit(texto_game_over,(150,300))
 
        else:
            pass
            
       
    #Eliminacion enemigos
    
    for bala in matador.lista_balas:
        for meteorito in enemigo.list_enemigos:
            if bala.y + matador.largo_bala > meteorito.y and bala.y < meteorito.y + enemigo.largo_ene and bala.x + matador.ancho_bala > meteorito.x and bala.x < meteorito.x + enemigo.ancho_ene:
                enemigo.list_enemigos.remove(meteorito)
                matador.lista_balas.remove(bala)
                contador_eliminaciones += 1
     
    #Actualizar la ventana

    pygame.display.flip()
    tiempo.tick(FPS)
    
