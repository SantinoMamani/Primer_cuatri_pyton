""" 
A. Analizar detenidamente el set de datos.
B. Recorrer la lista guardando en sub-listas: la pregunta, cada opción y la respuesta
correcta.
C. Crear 2 botones (rectángulos) uno con la etiqueta “Pregunta”, otro con la etiqueta
“Reiniciar”
D. Imprimir el Score: 999 donde se va a ir acumulando el puntaje de las respuestas
correctas. Cada respuesta correcta suma 10 puntos.
E. Al hacer clic en el botón (rectángulo) “Pregunta” debe mostrar las preguntas
comenzando por la primera y las tres opciones, cada clic en este botón pasa a la
siguiente pregunta.
F. Al hacer clic en una de las tres palabras que representa una de las tres opciones, si es
correcta, debe sumar el score y dejar de mostrar las opciones.
G. Solo tiene 2 opciones para acertar la respuesta correcta y sumar puntos, si agotó ambas
opciones, deja de mostrar las opciones y no suma score
H. Al hacer clic en el botón (rectángulo) “Reiniciar” debe mostrar las preguntas
comenzando por la primera y las tres opciones, cada clic pasa a la siguiente pregunta.
También debe reiniciar el Score. """
from datos import *
from constantes import *
import pygame
pygame.init() #Se inicializa pygame
pygame.mixer.init()  # Inicializa el módulo de sonido de Pygame
sonido_correcto = pygame.mixer.Sound("y2mate.com - Sonido de pregunta correcta.mp3")
sonido_incorrecto = pygame.mixer.Sound("y2mate.com - SONIDO RESPUESTA INCORRECTA 1.mp3")
musica_fondo = pygame.mixer.Sound("4kLOu3813BU_48.mp3")
pantalla = pygame.display.set_mode([800, 600]) #Se crea una ventana
pygame.display.set_caption("Preguntados")   #Se coloca titulo
titulo = ""
opcion_1 = ""
opcion_2 = ""
opcion_3 = ""
#Se define una imagen
imagen = pygame.image.load("logo.jpg")
imagen = pygame.transform.scale(imagen,(80,80))
imagen_personajes = pygame.image.load("Preguntados_personajes-removebg-preview.png")
imagen_personajes = pygame.transform.scale(imagen_personajes,(500,120))
imagen_marco = pygame.image.load("marco-removebg-preview-removebg-preview.png")
imagen_marco = pygame.transform.scale(imagen_marco,(800,610))
rectangulo1 = pygame.Rect(100, 490, 200, 80)
rectangulo2 = pygame.Rect(500, 490, 200, 80)

# Texto para los rectángulos
fuente = pygame.font.SysFont("Arial", 27)
texto_rectangulo1 = fuente.render("Pregunta", True, COLOR_AZUL)
texto_rectangulo2 = fuente.render("Reiniciar", True, COLOR_AZUL)
#Definir textos
fuente_opcion = pygame.font.SysFont("Arial", 25)
fuente_texto_final = pygame.font.SysFont("Arial", 35)
texto_titulo = fuente.render(str(titulo), True, (COLOR_BLANCO))
texto_opcion_1 = fuente_opcion.render(str(opcion_1), True, (COLOR_BLANCO))
texto_opcion_2 = fuente_opcion.render(str(opcion_2), True, (COLOR_BLANCO))
texto_opcion_3 = fuente_opcion.render(str(opcion_3), True, (COLOR_BLANCO))
posicion = 0
oportunidades = 0
puntaje = 0
errores_totales = 0
texto_puntaje = fuente.render(f"Score: {puntaje}", True, (COLOR_BLANCO))
respueestas_correctas = []
lista_preguntas = []
lista_opciones = []
lista_opciones_2 = []
lista_opciones_3 = []

for e_lista in lista:
    lista_opciones.append(e_lista["a"])
    lista_opciones_2.append(e_lista["b"])
    lista_opciones_3.append(e_lista["c"])
    lista_preguntas.append(e_lista["pregunta"])
    respueestas_correctas.append(e_lista["correcta"])

musica_fondo.set_volume(0.1)
musica_fondo.play()

bandera_correr = True
# Se verifica si el usuario cerro la ventana
while bandera_correr:
    
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            bandera_correr = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(event.pos)
            print(posicion_click)
            if(posicion_click[0] > 100 and posicion_click[0] < 300) and (posicion_click[1] > 500 and posicion_click[1] < 578):
                titulo = lista_preguntas[posicion] 
                texto_titulo = fuente.render(str(titulo), True, (COLOR_BLANCO))
                opcion_1 = lista_opciones[posicion]
                texto_opcion_1 = fuente_opcion.render(str(opcion_1), True, (COLOR_BLANCO))
                opcion_2 = lista_opciones_2[posicion]
                texto_opcion_2 = fuente_opcion.render(str(opcion_2), True, (COLOR_BLANCO))
                opcion_3 = lista_opciones_3[posicion]
                texto_opcion_3 = fuente_opcion.render(str(opcion_3), True, (COLOR_BLANCO))
                oportunidades = 0
            elif (posicion_click[0] > 500 and posicion_click[0] < 700) and (posicion_click[1] > 500 and posicion_click[1] < 578):
                # Lógica para reiniciar el juego
                posicion = 0
                puntaje = 0
                oportunidades = 0
                texto_puntaje = fuente.render(f"Score: {puntaje}", True, (COLOR_BLANCO))
                titulo = lista_preguntas[posicion] 
                texto_titulo = fuente.render(str(titulo), True, (COLOR_BLANCO))
                opcion_1 = lista_opciones[posicion]
                texto_opcion_1 = fuente_opcion.render(str(opcion_1), True, (COLOR_BLANCO))
                opcion_2 = lista_opciones_2[posicion]
                texto_opcion_2 = fuente_opcion.render(str(opcion_2), True, (COLOR_BLANCO))
                opcion_3 = lista_opciones_3[posicion]
                texto_opcion_3 = fuente_opcion.render(str(opcion_3), True, (COLOR_BLANCO))
                
            if (posicion_click[0] > 144 and posicion_click[0] < 344) and (posicion_click[1] > 244 and posicion_click[1] < 394):
                print("a")
                if "a" != respueestas_correctas[posicion]:
                    oportunidades += 1
                    errores_totales += 1
                    sonido_incorrecto.play()
                elif "a" == respueestas_correctas[posicion]:
                    puntaje += 10
                    posicion += 1
                    texto_puntaje = fuente.render(f"Score: {puntaje}", True, (COLOR_BLANCO))
                    texto_opcion_1 = fuente.render(str(opcion_1), True, COLOR_VERDE)
                    texto_opcion_2 = fuente_opcion.render(str(opcion_2), True, (COLOR_ROJO))
                    texto_opcion_3 = fuente_opcion.render(str(opcion_3), True, (COLOR_ROJO))
                    sonido_correcto.play()
                if oportunidades == 2:
                    posicion += 1
                    titulo = lista_preguntas[posicion] 
                    texto_titulo = fuente.render(str(titulo), True, (COLOR_BLANCO))
                    opcion_1 = lista_opciones[posicion]
                    texto_opcion_1 = fuente_opcion.render(str(opcion_1), True, (COLOR_BLANCO))
                    opcion_2 = lista_opciones_2[posicion]
                    texto_opcion_2 = fuente_opcion.render(str(opcion_2), True, (COLOR_BLANCO))
                    opcion_3 = lista_opciones_3[posicion]
                    texto_opcion_3 = fuente_opcion.render(str(opcion_3), True, (COLOR_BLANCO))    
                    oportunidades = 0
                
            if (posicion_click[0] > 344 and posicion_click[0] < 544) and (posicion_click[1] > 244 and posicion_click[1] < 394):
                print("b")
                if "b" != respueestas_correctas[posicion]:
                    oportunidades += 1
                    errores_totales += 1
                    sonido_incorrecto.play()
                elif "b" == respueestas_correctas[posicion]:
                    puntaje += 10
                    posicion += 1
                    texto_puntaje = fuente.render(f"Score: {puntaje}", True, (COLOR_BLANCO))
                    texto_opcion_1 = fuente.render(str(opcion_1), True, COLOR_ROJO)
                    texto_opcion_2 = fuente_opcion.render(str(opcion_2), True, (COLOR_VERDE))
                    texto_opcion_3 = fuente_opcion.render(str(opcion_3), True, (COLOR_ROJO))
                    sonido_correcto.play()
                if oportunidades == 2:
                    posicion += 1
                    titulo = lista_preguntas[posicion] 
                    texto_titulo = fuente.render(str(titulo), True, (COLOR_BLANCO))
                    opcion_1 = lista_opciones[posicion]
                    texto_opcion_1 = fuente_opcion.render(str(opcion_1), True, (COLOR_BLANCO))
                    opcion_2 = lista_opciones_2[posicion]
                    texto_opcion_2 = fuente_opcion.render(str(opcion_2), True, (COLOR_BLANCO))
                    opcion_3 = lista_opciones_3[posicion]
                    texto_opcion_3 = fuente_opcion.render(str(opcion_3), True, (COLOR_BLANCO))
                    oportunidades = 0
                
            if (posicion_click[0] > 544 and posicion_click[0] < 744) and (posicion_click[1] > 244 and posicion_click[1] < 394):
                print("c")
                if "c" != respueestas_correctas[posicion]:
                    oportunidades += 1
                    errores_totales += 1
                    sonido_incorrecto.play()
                elif "c" == respueestas_correctas[posicion]:
                    puntaje += 10
                    posicion += 1
                    texto_puntaje = fuente.render(f"Score: {puntaje}", True, (COLOR_BLANCO))
                    texto_opcion_1 = fuente.render(str(opcion_1), True, COLOR_ROJO)
                    texto_opcion_2 = fuente_opcion.render(str(opcion_2), True, (COLOR_ROJO))
                    texto_opcion_3 = fuente_opcion.render(str(opcion_3), True, (COLOR_VERDE))
                    sonido_correcto.play()
                if oportunidades == 2:
                    posicion += 1
                    titulo = lista_preguntas[posicion] 
                    texto_titulo = fuente.render(str(titulo), True, (COLOR_BLANCO))
                    opcion_1 = lista_opciones[posicion]
                    texto_opcion_1 = fuente_opcion.render(str(opcion_1), True, (COLOR_BLANCO))
                    opcion_2 = lista_opciones_2[posicion]
                    texto_opcion_2 = fuente_opcion.render(str(opcion_2), True, (COLOR_BLANCO))
                    opcion_3 = lista_opciones_3[posicion]
                    texto_opcion_3 = fuente_opcion.render(str(opcion_3), True, (COLOR_BLANCO))
                    oportunidades = 0
            
            # Verificar si se ha alcanzado la última pregunta
            if posicion == len(lista_preguntas):
                pantalla.fill(COLOR_AZUL)  # Limpia la pantalla
                texto_puntaje_final = fuente_texto_final.render(f"Score total: {puntaje}", True, COLOR_BLANCO)
                texto_total_errores = fuente.render(f"Erorres totales: {errores_totales}", True, COLOR_BLANCO)
                pantalla.blit(texto_puntaje_final, (400 - texto_puntaje_final.get_width() // 2, 300 - texto_puntaje_final.get_height() // 2))
                pantalla.blit(texto_total_errores, (400 - texto_total_errores.get_width() // 2, 510 - texto_total_errores.get_height() // 2))
                pygame.display.flip()
                
                # Esperar a que el usuario presione una tecla para cerrar la ventana
                esperando_cierre = True
                while esperando_cierre:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                            esperando_cierre = False
                bandera_correr = False
                
            
    pantalla.fill((COLOR_AZUL)) #Se pinta elfondo de la ventana
    pantalla.blit(imagen,(39,29))#Se funde la imagen
    pantalla.blit(imagen_personajes,(190,18))
    pantalla.blit(imagen_marco,(0,0))
    pygame.draw.rect(pantalla, COLOR_BLANCO, rectangulo1)
    pygame.draw.rect(pantalla, COLOR_BLANCO, rectangulo2)
    pygame.draw.rect(pantalla, COLOR_AZUL, (144,344,180,50)) #primer numero izquierda, segundo top, ancho, largo
    pygame.draw.rect(pantalla, COLOR_AZUL, (344,344,180,50))
    pygame.draw.rect(pantalla, COLOR_AZUL, (544,344,190,50))
    pantalla.blit(texto_puntaje, (39, 105))
    pantalla.blit(texto_titulo,(150,150))
    pantalla.blit(texto_opcion_1,(170,350))
    pantalla.blit(texto_opcion_2,(370,350))
    pantalla.blit(texto_opcion_3,(570,350))
    
    # Dibujar el texto en los rectángulos
    pantalla.blit(texto_rectangulo1, (rectangulo1.centerx - texto_rectangulo1.get_width() // 2, rectangulo1.centery - texto_rectangulo1.get_height() // 2))
    pantalla.blit(texto_rectangulo2, (rectangulo2.centerx - texto_rectangulo2.get_width() // 2, rectangulo2.centery - texto_rectangulo2.get_height() // 2))
    pygame.display.flip()# Muestra los cambios en la pantalla  
pygame.quit()