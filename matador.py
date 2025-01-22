import pygame

class Matador:

    def __init__(self):
        self.ANCHO = 50
        self.ALTO = 50 
        self.cord_x = 300
        self.cord_y = 500
        self.color_rojo = (255,0,0)
        self.speed_x = 5

    def dibujar_matador(self,ventana):
        matador = pygame.Rect(self.cord_x,self.cord_y,self.ANCHO,self.ALTO) 
        pygame.draw.rect(ventana,self.color_rojo,matador)   

    def mov_matador(self,ventana_ancho):
        if self.cord_x >= ventana_ancho/ventana_ancho and self.cord_x <= ventana_ancho - (self.ANCHO + self.speed_x):
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                self.cord_x -= self.speed_x
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                self.cord_x += self.speed_x
        
        if self.cord_x <= ventana_ancho/ventana_ancho:
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                self.cord_x = self.cord_x
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                self.cord_x += self.speed_x    
        if self.cord_x >= ventana_ancho - (self.ANCHO + self.speed_x):
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                self.cord_x -= self.speed_x
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                self.cord_x = self.cord_x            
        
    
       
                        