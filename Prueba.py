from data import lista_bzrp
import pygame
from constantes import *

posicion = 0
lista_titulos = []

for e_lista in lista_bzrp:
    lista_titulos.append(e_lista["title"])


titulo = ""
pygame.init() #Se inicializa pygame
pantalla = pygame.display.set_mode([800, 600]) #Se crea una ventana
pygame.display.set_caption("Preguntados")   #Se coloca titulo
#Se define una imagen
imagen = pygame.image.load("logo.jpg")
imagen = pygame.transform.scale(imagen,(80,80))
#Definir textos
fuente = pygame.font.SysFont("Arial", 30)
texto_titulo = fuente.render(str(titulo), True, (COLOR_GRIS))


bandera_correr = True
# Se verifica si el usuario cerro la ventana
while bandera_correr:
    
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            bandera_correr = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(event.pos)
            #print(posicion_click)
            titulo = lista_titulos[posicion]
            texto_titulo = fuente.render(str(titulo), True, (COLOR_GRIS))
            if posicion > len(lista_titulos):
                posicion = 0
            else:
                posicion = posicion + 1
        
    pantalla.fill((COLOR_AZUL)) #Se pinta el fondo de la ventana
    pantalla.blit(imagen,(10,10))#Se funde la imagen
    pantalla.blit(texto_titulo,(150,170))
    pygame.display.flip()# Muestra los cambios en la pantalla
    
    
    
    
pygame.quit()