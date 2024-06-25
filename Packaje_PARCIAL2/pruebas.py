import pygame
import sys
import random
import json

pygame.init()

# Definición de colores
NEGRO = (0, 0, 0)
AZUL_CLARO = (0, 150, 255)
BLANCO = (255, 255, 255)
GRIS_CLARO = (200, 200, 200)
VERDE = (0, 255, 0)

ANCHO_VENTANA = 1000
ALTO_VENTANA = 900
TAMAÑO_VENTANA = (ANCHO_VENTANA, ALTO_VENTANA)
FPS = 60

# Posiciones y tamaños
posicion_imagen_y = 450
posicion_imagen_x = ANCHO_VENTANA // 2
ancho_cuadro_de_texto = 200
alto_cuadro_de_texto = 50
distancia_borde_inferior = 100
posicion_cuadro_de_texto_x = (ANCHO_VENTANA - ancho_cuadro_de_texto) // 2
posicion_cuadro_de_texto_y = (ALTO_VENTANA - alto_cuadro_de_texto - distancia_borde_inferior)
ancho_cuadro_imagen = 400
alto_cuadro_imagen = 500
posicion_cuadro_imagen_x = (ANCHO_VENTANA - ancho_cuadro_imagen) // 2
posicion_cuadro_imagen_y = ((ALTO_VENTANA - alto_cuadro_imagen) // 2) - 50
ancho_boton = 160
alto_boton = 20
posicion_boton_x = (ANCHO_VENTANA - ancho_boton) // 2

# Inicialización de la ventana
ventana = pygame.display.set_mode(TAMAÑO_VENTANA)
pygame.display.set_caption("¿Quién es ese Pokémon?")

# Icono de la ventana
icono = pygame.image.load("Packaje_PARCIAL2/pikachu.png")
pygame.display.set_icon(icono)

# Fuentes
fuente = pygame.font.SysFont("Consolas", 40)
titulo = fuente.render("¿Quién es ese Pokémon?", True, BLANCO)
titulo_rect = titulo.get_rect()
titulo_rect.center = (ANCHO_VENTANA // 2, 60)
fuente_cuadro_texto = pygame.font.SysFont("Arial", 20)
fuente_boton = pygame.font.SysFont("Consolas", 12)
texto_boton = fuente_boton.render("Mostrar imagen oculta", True, NEGRO)
boton_rect = texto_boton.get_rect()

# Rectángulos
cuadro_de_imagen = pygame.Rect(posicion_cuadro_imagen_x, posicion_cuadro_imagen_y, ancho_cuadro_imagen, alto_cuadro_imagen)
cuadro_de_texto = pygame.Rect(posicion_cuadro_de_texto_x, posicion_cuadro_de_texto_y, ancho_cuadro_de_texto, alto_cuadro_de_texto)
cuadro_boton = pygame.Rect(posicion_boton_x, posicion_cuadro_de_texto_y - 40, ancho_boton, alto_boton)
boton_rect.center = cuadro_boton.center

# Variables
texto_ingresado = ""
mostrar_imagen_normal = False

# Carga de imagenes desde JSON
with open("Packaje_PARCIAL2/Imagenes_pokemones.json", "r") as archivo:
    imagenes = json.load(archivo)

# Lista de Pokémon
pokemones = []
for generacion in imagenes.values():
    for pokemon in generacion.values():
        pokemones.append({
            "imagen_normal": pokemon["imagen_normal"],
            "silueta": pokemon["silueta"]
        })

# Selección aleatoria de un Pokémon
pokemon_actual = random.choice(pokemones)
ruta_imagen_silueta = pokemon_actual["silueta"]
ruta_imagen_normal = pokemon_actual["imagen_normal"]

# Cargar imágenes del Pokémon
silueta_aleatoria = pygame.image.load(ruta_imagen_silueta)
imagen_normal = pygame.image.load(ruta_imagen_normal)
silueta_aleatoria = pygame.transform.scale(silueta_aleatoria, (ancho_cuadro_imagen, alto_cuadro_imagen))
imagen_normal = pygame.transform.scale(imagen_normal, (ancho_cuadro_imagen, alto_cuadro_imagen))

# Obtener el nombre del Pokémon desde la ruta de la imagen normal
nombre_pokemon = ruta_imagen_normal.split("\\")[-1].split(".")[0]

# Reloj para controlar FPS
clock = pygame.time.Clock()

# Bucle principal
flag = True
while flag:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            flag = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if cuadro_de_texto.collidepoint(evento.pos):
                    COLOR_CUADRO_TEXTO = VERDE
                else:
                    COLOR_CUADRO_TEXTO = GRIS_CLARO
                if cuadro_boton.collidepoint(evento.pos):
                    COLOR_BOTON = BLANCO
                    mostrar_imagen_normal = True
                else:
                    COLOR_BOTON = GRIS_CLARO
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_BACKSPACE:
                texto_ingresado = texto_ingresado[:-1]
            elif evento.key == pygame.K_RETURN:
                if texto_ingresado.lower() == nombre_pokemon.lower():
                    mostrar_imagen_normal = True
                texto_ingresado = ""
            else:
                texto_ingresado += evento.unicode

    ventana.fill(AZUL_CLARO)

    pygame.draw.rect(ventana, COLOR_CUADRO_TEXTO, cuadro_de_texto)
    pygame.draw.rect(ventana, NEGRO, cuadro_de_texto, 3)
    pygame.draw.rect(ventana, NEGRO, cuadro_de_imagen, 2)
    pygame.draw.rect(ventana, GRIS_CLARO, cuadro_de_imagen)
    pygame.draw.rect(ventana, NEGRO, cuadro_boton, 1)
    pygame.draw.rect(ventana, COLOR_BOTON, cuadro_boton)

    texto = fuente_cuadro_texto.render(texto_ingresado, True, NEGRO)
    texto_rect = texto.get_rect()
    texto_rect.center = cuadro_de_texto.center
    ventana.blit(texto, texto_rect)
    ventana.blit(titulo, titulo_rect)
    ventana.blit(texto_boton, boton_rect)

    if mostrar_imagen_normal:
        ventana.blit(imagen_normal, (posicion_cuadro_imagen_x, posicion_cuadro_imagen_y))
    else:
        ventana.blit(silueta_aleatoria, (posicion_cuadro_imagen_x, posicion_cuadro_imagen_y))

    pygame.display.update()

pygame.quit()
sys.exit()
