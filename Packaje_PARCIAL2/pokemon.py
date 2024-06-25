import pygame
import sys
import random
import json

pygame.init()

NEGRO = (0,0,0)    
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)
BLANCO = (255,255,255)
GRIS_CLARO = (200,200,200)
ROJO_CLARO = (255, 128, 128)
VERDE_CLARO = (144, 238, 144)

ANCHO_VENTANA = 1000
ALTO_VENTANA = 900
TAMAÑO_VENTANA = (ANCHO_VENTANA, ALTO_VENTANA)

TAMAÑO_TEXTO = 32

COLOR_FONDO = (AZUL_CLARO)
COLOR_CUADRO_TEXTO = GRIS_CLARO
COLOR_BOTON = BLANCO
COLOR_CUADRO_IMAGEN = GRIS_CLARO

FPS = 60

posicion_imagen_y = 450
posicion_imagen_x = ANCHO_VENTANA//2

ancho_cuadro_de_texto =  200
alto_cuadro_de_texto = 50
dimensiones_del_cuadro_de_texto = (ancho_cuadro_de_texto, alto_cuadro_de_texto)

distancia_borde_inferior = 100
posicion_cuadro_de_texto_x = (ANCHO_VENTANA - ancho_cuadro_de_texto)//2
posicion_cuadro_de_texto_y = (ALTO_VENTANA - alto_cuadro_de_texto - distancia_borde_inferior)

ancho_cuadro_imagen = 400
alto_cuadro_imagen = 500
posicion_cuadro_imagen_x = (ANCHO_VENTANA - ancho_cuadro_imagen) // 2
posicion_cuadro_imagen_y = ((ALTO_VENTANA - alto_cuadro_imagen) // 2) -50

ancho_boton = 160
alto_boton = 20
posicion_boton_x = (ANCHO_VENTANA - ancho_boton) // 2

lista_de_imagenes = []

#-------------------Ventana Principal-----------------
ventana = pygame.display.set_mode(TAMAÑO_VENTANA)
pygame.display.set_caption("¿Quien es ese Pokemon?") 

#------------------------Icono------------------------
icono = pygame.image.load("Packaje_PARCIAL2\pikachu.png")
pygame.display.set_icon(icono)

#------------------------Fuentes----------------------
#titulo
fuente = pygame.font.SysFont("Consolas", 40)
titulo = fuente.render("¿Quien es ese Pokemón?", True, BLANCO)
titulo_rect = titulo.get_rect()
titulo_rect.center = (ANCHO_VENTANA // 2, 60)

#cuadro de texto
fuente_cuadro_texto = pygame.font.SysFont("Arial", 20)

#boton
fuente_boton = pygame.font.SysFont("Consolas", 12)
texto_boton = fuente_boton.render("Mostrar imagen oculta", True, NEGRO)
boton_rect = texto_boton.get_rect()

#----------------Imagen de Fondo----------------------
# imagen = pygame.image.load(r"Packaje_PARCIAL2\fondo_pokemon.jpg")
# imagen = pygame.transform.scale(imagen, (1000,800))

#----------------Rectangulo de Imagen-------------------
cuadro_de_imagen = pygame.Rect(posicion_cuadro_imagen_x, posicion_cuadro_imagen_y, ancho_cuadro_imagen, alto_cuadro_imagen)

#------------------Caja de Texto----------------------
cuadro_de_texto = pygame.Rect(posicion_cuadro_de_texto_x, posicion_cuadro_de_texto_y, ancho_cuadro_de_texto, 
                alto_cuadro_de_texto)
texto_ingresado = ""
#------------------------Boton-------------------------
cuadro_boton = pygame.Rect(posicion_boton_x, posicion_cuadro_de_texto_y - 40, ancho_boton, alto_boton )
boton_rect.center = (cuadro_boton.center)

#----------------carga de imagen oculta----------------
path = "Packaje_PARCIAL2\\Imagenes_pokemones.json"
with open(path, "r") as archivo:
    imagenes = json.load(archivo)

# Lista de Pokémon
pokemones = []

# Iterar sobre todas las generaciones y Pokémon en el archivo JSON
for generacion in imagenes.values():
    for pokemon in generacion.values():
        pokemones.append({
            "imagen_normal": pokemon["imagen_normal"],
            "silueta": pokemon["silueta"]
        })

def cargar_nuevo_pokemon(pokemones: list, ancho_cuadro_imagen: int, alto_cuadro_imagen: int) -> str:
    # Selección aleatoria de un Pokémon inicial
    pokemon_actual = random.choice(pokemones)
    ruta_imagen_silueta = pokemon_actual["silueta"]
    ruta_imagen_normal = pokemon_actual["imagen_normal"]

    # Cargar imágenes de la silueta y normal del Pokémon inicial
    silueta_aleatoria = pygame.image.load(ruta_imagen_silueta)
    silueta_aleatoria = pygame.transform.scale(silueta_aleatoria, (ancho_cuadro_imagen, alto_cuadro_imagen))

    pokemon_resuleto = pygame.image.load(ruta_imagen_normal)
    pokemon_resuleto = pygame.transform.scale(pokemon_resuleto, (ancho_cuadro_imagen, alto_cuadro_imagen))

    nombre_pokemon = ruta_imagen_normal.split("\\")[-1].split(".")[0]

    return nombre_pokemon, silueta_aleatoria, pokemon_resuleto

def pantalla_inicial():
    texto_rect = texto.get_rect()
    texto_rect.center = cuadro_de_texto.center
    ventana.blit(texto, texto_rect)  # texto del cuadro de texto

    ventana.blit(titulo, titulo_rect)  # titulo
    ventana.blit(texto_boton, boton_rect)


clock = pygame.time.Clock()


nombre_pokemon, silueta_aleatoria, pokemon_resuleto = cargar_nuevo_pokemon(pokemones, ancho_cuadro_imagen, alto_cuadro_imagen)

flag = True
while flag == True:
    clock.tick(FPS)         
    no_lo_se = False
    coincidencia = False

    lista_eventos = pygame.event.get()      
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:      
            flag = False

        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_BACKSPACE:
                texto_ingresado = texto_ingresado[:-1]

            elif evento.key == pygame.K_RETURN:
                # Verificar si el nombre ingresado coincide con el nombre del Pokémon
                if texto_ingresado.lower() == nombre_pokemon.lower():
                    print("coincidencia")
                    coincidencia = True
                    ventana.blit(pokemon_resuleto, (posicion_cuadro_imagen_x, posicion_cuadro_imagen_y))
                    pygame.display.update()
                    pygame.time.wait(2000)
                    nombre_pokemon, silueta_aleatoria, pokemon_resuleto = cargar_nuevo_pokemon(pokemones, ancho_cuadro_imagen, alto_cuadro_imagen)
                    texto_ingresado = ""

                else:
                    texto_ingresado = ""
                        
            else:
                texto_ingresado += evento.unicode

        elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  #boton izq 
                    if cuadro_de_texto.collidepoint(evento.pos):    #verifico si presione el boton izq del mouse dentro del cuadro de texto. evento.pos devuelve las coordenadas del mouse
                        COLOR_CUADRO_TEXTO = VERDE
                    else:
                        COLOR_CUADRO_TEXTO = GRIS_CLARO

                    if cuadro_boton.collidepoint(evento.pos):
                        print("no lo se")
                        COLOR_BOTON = BLANCO
                        no_lo_se = True
                        ventana.blit(pokemon_resuleto, (posicion_cuadro_imagen_x, posicion_cuadro_imagen_y))

                        #Muestra el nombre del pokemon desconocido
                        texto = fuente_cuadro_texto.render(nombre_pokemon, True, NEGRO)
                        texto_rect = texto.get_rect()
                        texto_rect.center = cuadro_de_texto.center
                        ventana.blit(texto, texto_rect)  # texto del cuadro de texto

                        pygame.display.update()
                        pygame.time.wait(2000)

                        nombre_pokemon, silueta_aleatoria, pokemon_resuleto = cargar_nuevo_pokemon(pokemones, ancho_cuadro_imagen, alto_cuadro_imagen)
    
                    else:
                        COLOR_BOTON = GRIS_CLARO
    
    ventana.fill(COLOR_FONDO)

    pygame.draw.rect(ventana, NEGRO, cuadro_de_texto, 3)    # borde del cuadro texto
    pygame.draw.rect(ventana, COLOR_CUADRO_TEXTO, cuadro_de_texto)  # relleno del cuadro texto

    pygame.draw.rect(ventana, NEGRO, cuadro_de_imagen, 2)      # dibujo borde del cuadro de imagen principal
    pygame.draw.rect(ventana, COLOR_CUADRO_IMAGEN, cuadro_de_imagen)    # relleno del cuadro de imagen principal

    pygame.draw.rect(ventana, NEGRO, cuadro_boton, 1)       # dibujo borde del boton
    pygame.draw.rect(ventana, COLOR_BOTON, cuadro_boton)    # relleno del boton

    texto = fuente_cuadro_texto.render(texto_ingresado, True, NEGRO)
    ventana.blit(silueta_aleatoria, (posicion_cuadro_imagen_x, posicion_cuadro_imagen_y))
    pantalla_inicial()

    pygame.display.update()

pygame.quit()
sys.exit()
