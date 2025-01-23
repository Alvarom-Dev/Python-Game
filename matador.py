import pygame

class Matador:

    def __init__(self):
        self.ANCHO = 50
        self.ALTO = 50 
        self.color_blanco = (255,255,255)
        self.lista_balas = []
        self.bala_speed = 5
        self.cord_x = 300
        self.cord_y = 500
        self.color_rojo = (255,0,0)
        self.speed_x = 5
        self.ancho_bala = 10
        self.largo_bala = 10
        self.cord_x_bala = 0
        self.cord_y_bala = 0

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

    def crear_balas(self):
        self.cord_x_bala = self.cord_x
        self.cord_y_bala = self.cord_y
        objeto_bala = pygame.Rect(self.cord_x_bala + self.ANCHO/2,self.cord_y_bala + self.ALTO/2,self.ancho_bala,self.largo_bala)   
        self.lista_balas.append(objeto_bala)
     
       
    def dibujar_balas(self,ventana):
        for bala in self.lista_balas:
            bala.y -= self.bala_speed
            pygame.draw.rect(ventana,self.color_blanco,bala)   
            
        
       
                        