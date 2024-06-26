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
COLOR_BOTON_GEN_1 = VERDE
COLOR_BOTON_GEN_2 = ROJO
COLOR_BOTON_GEN_3 = ROJO
COLOR_CUADRO_IMAGEN = AZUL_CLARO    

FPS = 60

posicion_imagen_y = 450
posicion_imagen_x = ANCHO_VENTANA//2

ancho_cuadro_de_texto =  200
alto_cuadro_de_texto = 50
dimensiones_del_cuadro_de_texto = (ancho_cuadro_de_texto, alto_cuadro_de_texto)

distancia_borde_inferior = 140
posicion_cuadro_de_texto_x = (ANCHO_VENTANA - ancho_cuadro_de_texto)//2
posicion_cuadro_de_texto_y = (ALTO_VENTANA - alto_cuadro_de_texto - distancia_borde_inferior)

ancho_cuadro_imagen = 400
alto_cuadro_imagen = 500
posicion_cuadro_imagen_x = (ANCHO_VENTANA - ancho_cuadro_imagen) // 2
posicion_cuadro_imagen_y = ((ALTO_VENTANA - alto_cuadro_imagen) // 2) -50

ancho_boton = 180
alto_boton = 30

ancho_boton_generaciones = 67
alto_boton_generaciones = 67

posicion_botones_generaciones_x = 5
posicion_botones_generaciones_y = 35

ancho_caja_seleccion_gen = 220
alto_caja_seleccion_gen = 110

posicion_caja_selec_gen_x = 0
posicion_caja_selec_gen_y = 0

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
fuente_boton = pygame.font.SysFont("Consolas", 15)
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
#------------------------Botones-------------------------
cuadro_boton = pygame.Rect(posicion_boton_x, posicion_cuadro_de_texto_y - 40, ancho_boton, alto_boton )
boton_rect.center = (cuadro_boton.center)

cuadro_selec_gen = pygame.Rect(posicion_caja_selec_gen_x, posicion_caja_selec_gen_y, ancho_caja_seleccion_gen, alto_caja_seleccion_gen)

fuente_gen = pygame.font.SysFont("Consolas", 30)
texto_gen = fuente_gen.render("Generaciones", True, NEGRO)
texto_rect_gen = texto_gen.get_rect()

fuente_boton = pygame.font.SysFont("Consolas", 40)
texto_boton_gen_1 = fuente_boton.render("1", True, NEGRO)
texto_rect_gen_1 = texto_boton_gen_1.get_rect()

texto_boton_gen_2 = fuente_boton.render("2", True, NEGRO)
texto_rect_gen_2 = texto_boton_gen_2.get_rect()

texto_boton_gen_3 = fuente_boton.render("3", True, NEGRO)
texto_rect_gen_3 = texto_boton_gen_3.get_rect()

boton_gen_1 = pygame.Rect(posicion_botones_generaciones_x, posicion_botones_generaciones_y,
                        ancho_boton_generaciones, alto_boton_generaciones)
texto_rect_gen_1.center = (boton_gen_1.center)

boton_gen_2 = pygame.Rect(posicion_botones_generaciones_x + ancho_boton_generaciones + 3,
                        posicion_botones_generaciones_y, ancho_boton_generaciones, alto_boton_generaciones)
texto_rect_gen_2.center = (boton_gen_2.center)

boton_gen_3 = pygame.Rect(posicion_botones_generaciones_x + (ancho_boton_generaciones * 2) + 6,
                        posicion_botones_generaciones_y, ancho_boton_generaciones, alto_boton_generaciones)
texto_rect_gen_3.center = (boton_gen_3.center)

desactivar_gen_1 = True
desactivar_gen_2 = False
desactivar_gen_3 = False

#----------------carga de imagen oculta----------------
path = "Packaje_PARCIAL2\\Imagenes_pokemones.json"
with open(path, "r") as archivo:
    json_pokemones = json.load(archivo)

pokemones = []

# Iterar sobre todas las generaciones y Pokémon en el archivo JSON
def cargar_pokemones_en_lista(lista_pokemones: list, pokemones_dicc) -> list:
    for nombre, pokemones in pokemones_dicc.items():
        pokemon = {
            "nombre": nombre,
            "generacion": pokemones["generacion"],
            "imagen_normal": pokemones["imagen_normal"],
            "silueta": pokemones["silueta"]
        }
        lista_pokemones.append(pokemon)
    return lista_pokemones

# Lista de Pokémon
pokemones = cargar_pokemones_en_lista(pokemones, json_pokemones)




pokemones_gen_1 = []
pokemones_gen_2 = []
pokemones_gen_3 = []


def separar_por_gen(lista_pokemones: list):
    lista_gen1 = []
    lista_gen2 = []
    lista_gen3 = []

    for i in range(len(lista_pokemones)):
        generacion_actual = lista_pokemones[i]['generacion']
        if generacion_actual == "1gen":
            lista_gen1.append(lista_pokemones[i]) 
        elif generacion_actual == "2gen":
            lista_gen2.append(lista_pokemones[i])
        else:
            lista_gen2.append(lista_pokemones[i])
    return lista_gen1, lista_gen2, lista_gen3

pokemones_gen_1, pokemones_gen_2, pokemones_gen_3 = separar_por_gen(pokemones)

primera_iteracion = True #cerrar cuando deseleccione la gen 1


def cargar_nuevo_pokemon(pokemones: list, ancho_cuadro_imagen: int, alto_cuadro_imagen: int, primera_iteracion: bool, lista_gen1, lista_gen2, lista_gen3) -> str: #state_gen_1: bool, state_gen_3: bool, state_gen_2: bool
    # Selección aleatoria de un Pokémon solo de la gen 1
    pokemones = []
    if primera_iteracion: 
        pokemones = lista_gen1
    #elif and eneable de cada generacion

    pokemon_actual = random.choice(pokemones)
    ruta_imagen_normal = pokemon_actual['imagen_normal']
    ruta_imagen_silueta = pokemon_actual['silueta']
    nombre_pokemon = pokemon_actual['nombre']
    generacion_pokemon = pokemon_actual['generacion']

    # Cargar imágenes de la silueta y normal del Pokémon inicial
    silueta_aleatoria = pygame.image.load(ruta_imagen_silueta)
    silueta_aleatoria = pygame.transform.scale(silueta_aleatoria, (ancho_cuadro_imagen, alto_cuadro_imagen))

    pokemon_resuleto = pygame.image.load(ruta_imagen_normal)
    pokemon_resuleto = pygame.transform.scale(pokemon_resuleto, (ancho_cuadro_imagen, alto_cuadro_imagen))

    return nombre_pokemon, silueta_aleatoria, pokemon_resuleto, generacion_pokemon

def pantalla_inicial():
    texto_rect = texto.get_rect()
    texto_rect.center = cuadro_de_texto.center
    ventana.blit(texto, texto_rect)  # texto del cuadro de texto

    ventana.blit(titulo, titulo_rect)  # titulo
    ventana.blit(texto_boton, boton_rect)

    ventana.blit(texto_gen, texto_rect_gen)  # titulo generaciones
    ventana.blit(texto_boton_gen_1, texto_rect_gen_1)
    ventana.blit(texto_boton_gen_2, texto_rect_gen_2)
    ventana.blit(texto_boton_gen_3, texto_rect_gen_3)

clock = pygame.time.Clock()

nombre_pokemon, silueta_aleatoria, pokemon_resuleto, generacion_pokemon = cargar_nuevo_pokemon(pokemones, ancho_cuadro_imagen, alto_cuadro_imagen, primera_iteracion, pokemones_gen_1, pokemones_gen_2, pokemones_gen_3)

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
                    COLOR_CUADRO_TEXTO = VERDE
                    coincidencia = True
                    ventana.blit(pokemon_resuleto, (posicion_cuadro_imagen_x, posicion_cuadro_imagen_y))
                    pygame.display.update()
                    pygame.time.wait(2000)
                    COLOR_CUADRO_TEXTO = BLANCO
                    nombre_pokemon, silueta_aleatoria, pokemon_resuleto, generacion_pokemon = cargar_nuevo_pokemon(pokemones, ancho_cuadro_imagen, alto_cuadro_imagen)
                    texto_ingresado = ""

                else:
                    texto_ingresado = ""
                    print("No coincide")
                    COLOR_CUADRO_TEXTO = ROJO
                    pygame.display.update()
            else:
                texto_ingresado += evento.unicode

        elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  #boton izq 
                    # Boton selecionar generacion 1 por defecto activo
                    if boton_gen_1.collidepoint(evento.pos) and desactivar_gen_1:
                        COLOR_BOTON_GEN_1 = ROJO
                        desactivar_gen_1 = False
                    elif boton_gen_1.collidepoint(evento.pos) and desactivar_gen_1 ==  False:
                        COLOR_BOTON_GEN_1 = VERDE
                        desactivar_gen_1 = True
                    
                    # Boton selecionar generacion 2 por defecto desactivado
                    if boton_gen_2.collidepoint(evento.pos) and desactivar_gen_2 == False:
                        COLOR_BOTON_GEN_2 = VERDE 
                        desactivar_gen_2 = True
                    elif boton_gen_2.collidepoint(evento.pos) and desactivar_gen_2:
                        COLOR_BOTON_GEN_2 = ROJO 
                        desactivar_gen_2 = False

                    # Boton selecionar generacion 3 por defecto desactivado
                    if boton_gen_3.collidepoint(evento.pos) and desactivar_gen_3 == False:
                        COLOR_BOTON_GEN_3 = VERDE 
                        desactivar_gen_3 = True
                    elif boton_gen_3.collidepoint(evento.pos) and desactivar_gen_3:
                        COLOR_BOTON_GEN_3 = ROJO 
                        desactivar_gen_3 = False 
                    
                    # Boton escribir nombre
                    if cuadro_de_texto.collidepoint(evento.pos):    #verifico si presione el boton izq del mouse dentro del cuadro de texto. evento.pos devuelve las coordenadas del mouse
                        COLOR_CUADRO_TEXTO = BLANCO
                    else:
                        COLOR_CUADRO_TEXTO = GRIS_CLARO


                    # Boton "Mostrar imagen oculta"
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

                        nombre_pokemon, silueta_aleatoria, pokemon_resuleto, generacion_pokemon = cargar_nuevo_pokemon(pokemones, ancho_cuadro_imagen, alto_cuadro_imagen)
    
                    else:
                        COLOR_BOTON = GRIS_CLARO

    
    ventana.fill(COLOR_FONDO)

    pygame.draw.rect(ventana, COLOR_CUADRO_TEXTO, cuadro_de_texto, border_radius=12)  # relleno del cuadro texto

    pygame.draw.rect(ventana, COLOR_CUADRO_IMAGEN, cuadro_de_imagen)    # relleno del cuadro de imagen principal

    pygame.draw.rect(ventana, COLOR_BOTON, cuadro_boton, border_radius=8)    # relleno del boton

    pygame.draw.rect(ventana, BLANCO, cuadro_selec_gen, border_radius=8)    # relleno caja seleccion de generaciones
    pygame.draw.rect(ventana, COLOR_BOTON_GEN_1, boton_gen_1, border_radius=8)    # relleno del boton
    pygame.draw.rect(ventana, COLOR_BOTON_GEN_2, boton_gen_2, border_radius=8)    # relleno del boton
    pygame.draw.rect(ventana, COLOR_BOTON_GEN_3, boton_gen_3, border_radius=8)    # relleno del boton

    texto = fuente_cuadro_texto.render(texto_ingresado, True, NEGRO)
    ventana.blit(silueta_aleatoria, (posicion_cuadro_imagen_x, posicion_cuadro_imagen_y))
    pantalla_inicial()

    pygame.display.update()

pygame.quit()
sys.exit()
