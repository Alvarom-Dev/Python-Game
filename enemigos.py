import pygame, random


class Enemigos:
 
    def __init__(self):
        self.ancho_ene = 50
        self.largo_ene = 50 
        self.list_enemigos = []
        self.cord_x = 0
        self.cord_y = 0
        self.color_morado = (122,54,144)
        self.velocidad_y = 3
        self.enemigo_cubo = pygame.Rect(self.cord_x,self.cord_y,self.ancho_ene,self.largo_ene)
        
    def crear_enemigos(self,ancho_ventana):
        self.cord_x = random.randint(0, (ancho_ventana - self.ancho_ene))
        self.enemigo_cubo.x = self.cord_x
        self.list_enemigos.append(self.enemigo_cubo)
             
    
    def dibujar(self,ventana):
        for enemigo in self.list_enemigos:

            pygame.draw.rect(ventana,self.color_morado,enemigo)
            print(enemigo)
        #pygame.draw.rect(ventana,self.color_rojo,(self.list_pos_cord[0],self.list_pos_cord[1],self.ancho_ene,self.largo_ene))

    def movilidad_enemigos(self,largo_ventana):
        for enemigo in self.list_enemigos:
            if self.cord_y >= 0 and self.cord_y <= largo_ventana:

                 enemigo.y += self.velocidad_y 
                 self.cord_y += self.velocidad_y
                 self.velocidad_y += self.velocidad_y 
                 print("Pasa por movilidad")
            else:
                print("No pasa por el if")
        


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
           
                