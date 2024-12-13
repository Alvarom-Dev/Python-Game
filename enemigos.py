import pygame


class Enemigos:
    ancho_ene = 50
    largo_ene = 50 
    list_pos_cord = [300,300]
    cord_x = 0
    cord_y = 0
    color_rojo = (255,0,0)
    velocidad_x = 3
 
 
    def __init__(self):
        pass

    def dibujar(self,ventana):
        #pygame.draw.rect(ventana,color_rojo,(list_pos_cord[0],list_pos_cord[1],ancho_ene,largo_ene))
        pygame.draw.rect(ventana,self.color_rojo,(self.list_pos_cord[0],self.list_pos_cord[1],self.ancho_ene,self.largo_ene))
        
    def aparecer_enemigos(self):
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.KEYDOWN: 
                if evento.key == pygame.K_LEFT:
                    #self.velocidad_x -= self.velocidad_x
                    self.list_pos_cord[0] -= self.velocidad_x
                if evento.key == pygame.K_RIGHT:
                    #self.velocidad_x += self.velocidad_x  
                    self.list_pos_cord[0] += self.velocidad_x   
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT:
                     #self.velocidad_x = 0
                     self.list_pos_cord[0] = 0
                if evento.key == pygame.K_RIGHT:
                     #self.velocidad_x = 0
                     self.list_pos_cord[0] = 0
                #self.list_pos_cord[0] += self.velocidad_x
                print(self.list_pos_cord[0])         
 