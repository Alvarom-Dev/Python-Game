import pygame

class Matador:

    def __init__(self):
        self.ANCHO = 50
        self.ALTO = 50 
        self.cord_x = (600-self.ANCHO)
        self.cord_y = 500
        self.color_rojo = (255,0,0)
        self.speed_x = 5

    def dibujar_matador(self,ventana):
        matador = pygame.Rect(self.cord_x,self.cord_y,self.ANCHO,self.ALTO) 
        pygame.draw.rect(ventana,self.color_rojo,matador)   


    