import pygame


class Enemigos:
    ancho_ene = 50
    largo_ene = 50 
    list_pos_cord = [300,300]
    cord_x = 0
    cord_y = 0
    color_rojo = (255,0,0)
 
 
    def __init__(self):
        pass

    def dibujar(self,ventana):
        #pygame.draw.rect(ventana,color_rojo,(list_pos_cord[0],list_pos_cord[1],ancho_ene,largo_ene))
        pygame.draw.rect(ventana,self.color_rojo,(self.list_pos_cord[0],self.list_pos_cord[1],self.ancho_ene,self.largo_ene))

    def mover():
        pass
 