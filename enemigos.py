import pygame, random


class Enemigos:
 
    def __init__(self):
        self.ancho_ene = 50
        self.largo_ene = 50 
        self.list_enemigos = []
        self.cord_x = 0
        self.cord_y = 0
        self.color_morado = (166,70,190)
        self.velocidad_y = 10
       
        
    def crear_enemigos(self,ancho_ventana):
        enemigo_nuevo = pygame.Rect(self.cord_x,self.cord_y,self.ancho_ene,self.largo_ene)
        self.cord_x = random.randint(0, (ancho_ventana - self.ancho_ene))
        enemigo_nuevo.x = self.cord_x
        self.list_enemigos.append(enemigo_nuevo)
        print(self.list_enemigos)
             
   
    def dibujar(self,ventana):
        for enemigo in self.list_enemigos:
            enemigo.y += self.velocidad_y
            pygame.draw.rect(ventana,self.color_morado,enemigo)
            
               

"""  
    def key_down(self,evento):
                    
        if evento.key == pygame.K_LEFT:    
            self.list_pos_cord[0] -= self.velocidad_x
        if evento.key == pygame.K_RIGHT:   
             self.list_pos_cord[0] += self.velocidad_x  

    def key_up (self,evento):
        if evento.key == pygame.K_LEFT:
            self.list_pos_cord[0] = self.list_pos_cord[0]
        if evento.key == pygame.K_RIGHT:
            self.list_pos_cord[0] = self.list_pos_cord[0]
    """
           
                