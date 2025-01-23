import pygame, random


class Enemigos:
 
    def __init__(self):
        self.ancho_ene = 50
        self.largo_ene = 50 
        self.cord_x = 0
        self.cord_y = 0
        self.color_morado = (166,70,190)
        self.velocidad_y = 2
        self.primer_enemigo = pygame.Rect(random.randint(0,550),self.cord_y,self.ancho_ene,self.largo_ene)
        self.list_enemigos = [self.primer_enemigo]
        
    def crear_enemigos(self,ancho_ventana):
        
        enemigo_nuevo = pygame.Rect(self.cord_x,self.cord_y,self.ancho_ene,self.largo_ene)
        self.cord_x = random.randint(0, (ancho_ventana - self.ancho_ene))
        enemigo_nuevo.x = self.cord_x
        self.list_enemigos.append(enemigo_nuevo)
    
    
    def dibujar_enemigos(self,ventana):
        for enemigo in self.list_enemigos:
            enemigo.y += self.velocidad_y
            pygame.draw.rect(ventana,self.color_morado,enemigo)
                      
           
                