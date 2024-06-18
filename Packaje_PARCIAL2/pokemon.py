from funciones import manejar_evento, dibujar
import pygame
import sys

NEGRO = (0,0,0)    
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)
BLANCO = (255,255,255)


color_backgraund = (AZUL_CLARO)

posicion_titulo_x = 50
posicion_titulo_y = 40

ancho_ventana = 1200
alto_ventana = 1000

ancho_imagen =  600 
alto_imagen = 500
posicion_imagen_x =  ancho_ventana//2
posicion_imagen_y =  450



pygame.init()

ventana = pygame.display.set_mode((ancho_ventana, alto_ventana)) 
pygame.display.set_caption("¿Quien es ese Pokemon?")

icono = pygame.image.load("Packaje_PARCIAL2\pikachu.png")
pygame.display.set_icon(icono)

imagen = pygame.image.load(r"Packaje_PARCIAL2\Imagenes_pokemones\IMG\1gen\charmeleon_black.png")
img_rect = imagen.get_rect(center=(posicion_imagen_x, posicion_imagen_y))

fuente = pygame.font.SysFont("consolas", 40)

texto = fuente.render("¿Quien es ese pokemon?", True, BLANCO)
text_rect = texto.get_rect(center=(ancho_ventana//2, posicion_titulo_y))




nombre_pokemon = "Charmander"

flag = True
while flag == True:         
    
    lista_eventos = pygame.event.get()      
    ventana.fill(color_backgraund)


    for evento in lista_eventos:
        if evento.type == pygame.QUIT:      
            flag = False

    ventana.blit(texto, text_rect)
    ventana.blit(imagen, img_rect)

    pygame.display.update()

#nombre_ingresado = input("Cual es el pokemon")



pygame.quit()
sys.exit()