import pygame
import random

def cargar_pokemones_en_lista(lista_pokemones: list, pokemones_dicc: dict):
    for nombre, pokemones in pokemones_dicc.items():
        pokemon = {
            "nombre": nombre,
            "generacion": pokemones["generacion"],
            "imagen_normal": pokemones["imagen_normal"],
            "silueta": pokemones["silueta"],
            "frances": pokemones["frances"],
            "italiano": pokemones["italiano"],
            "aleman": pokemones["aleman"]
        }
        lista_pokemones.append(pokemon)
    return lista_pokemones

def separar_por_gen(lista_pokemones):
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
            lista_gen3.append(lista_pokemones[i])
    return lista_gen1, lista_gen2, lista_gen3


def cargar_nuevo_pokemon(lista_pokemones: list, eneable_gen_1: bool, eneable_gen_2: bool, eneable_gen_3: bool, ancho_imagen: int, alto_imagen: int):
    lista_gen1, lista_gen2, lista_gen3 = separar_por_gen(lista_pokemones)
    dos_generaciones = False

    if eneable_gen_1:
        if eneable_gen_2 and eneable_gen_3:
            lista_pokemones = lista_gen1 + lista_gen2 + lista_gen3
            print("Se cargaron las 3 generaciones")
        elif eneable_gen_2:
            lista_pokemones = lista_gen1 + lista_gen2
            print("Se cargaron la gen 1 y 2")
            dos_generaciones = True
        elif eneable_gen_3:
            lista_pokemones = lista_gen1 + lista_gen3
            dos_generaciones = True
            print("Se cargaron la gen 1 y 3")
        else:
            lista_pokemones = lista_gen1
            print("Se cargo la gen 1")
    
    if eneable_gen_2 and dos_generaciones == False:
        if eneable_gen_3:
            lista_pokemones = lista_gen2 + lista_gen3
            dos_generaciones = True
            print("Se cargaron la gen 2 y 3")
        else:
            lista_pokemones = lista_gen2
            print("Se cargo la gen 2")
    
    if eneable_gen_3 and dos_generaciones == False:
        lista_pokemones = lista_gen3
        print("Se cargo la gen 3")
    
    lista_atributos_pokemon = []

    pokemon_actual = random.choice(lista_pokemones)
    ruta_imagen_normal = pokemon_actual['imagen_normal']
    ruta_imagen_silueta = pokemon_actual['silueta']
    nombre_pokemon = pokemon_actual['nombre']
    generacion_pokemon = pokemon_actual['generacion']
    nombre_frances = pokemon_actual['frances']
    nombre_italiano = pokemon_actual['italiano']
    nombre_aleman = pokemon_actual['aleman']



    #Este se puede hacer en una funcion que carge y escale
    silueta_aleatoria = pygame.image.load(ruta_imagen_silueta)
    silueta_aleatoria = pygame.transform.scale(silueta_aleatoria, (ancho_imagen, alto_imagen))

    pokemon_resuelto = pygame.image.load(ruta_imagen_normal)
    pokemon_resuelto = pygame.transform.scale(pokemon_resuelto, (ancho_imagen, alto_imagen))

    lista_atributos_pokemon = [nombre_pokemon, silueta_aleatoria, pokemon_resuelto, generacion_pokemon, nombre_frances, nombre_italiano, nombre_aleman]
    return lista_atributos_pokemon


def crear_texto_rect(texto: str, fuente, color):
    texto_mostrar = fuente.render(texto, True, color)
    texto_rect = texto_mostrar.get_rect()
    #texto_rect.center = (ANCHO_VENTANA // 2, 60)
    return texto_mostrar, texto_rect

def crear_rectangulo_objeto(posicion_x, posicion_y, ancho, alto, centrar: bool, posicion, objeto_a_centar):
    rectangulo_objeto = pygame.Rect(posicion_x, posicion_y, ancho, alto)
    if centrar:
        centrar_objeto(posicion, objeto_a_centar, rectangulo_objeto)
    return rectangulo_objeto

def centrar_objeto(posicion, objeto_a_centar, rectangulo_objeto):
    match (posicion):
        case "center":
            objeto_a_centar.center = rectangulo_objeto.center
        case "midtop":
            objeto_a_centar.midtop = rectangulo_objeto.midtop
        case "midbottom":
            objeto_a_centar.midbottom = rectangulo_objeto.midbottom
        case "midleft":
            objeto_a_centar.midleft = rectangulo_objeto.midleft
        case "midright":
            objeto_a_centar.midright = rectangulo_objeto.midright
        case "topleft":
            objeto_a_centar.topleft = rectangulo_objeto.topleft
        case "topright":
            objeto_a_centar.topright = rectangulo_objeto.topright
        case "bottomleft":
            objeto_a_centar.bottomleft = rectangulo_objeto.bottomleft
        case "bottomright":
            objeto_a_centar.bottomright = rectangulo_objeto.bottomright
        case None:
            pass


def crear_texto_en_caja(texto, fuente_texto, color_texto, ancho_caja, alto_caja,cuadro_principal, posicion_caja, posicion_texto):
    texto, texto_rect = crear_texto_rect(texto, fuente_texto, color_texto)

    caja = crear_rectangulo_objeto(0, 0, ancho_caja, alto_caja, False, None ,None)
    centrar_objeto(posicion_caja, caja, cuadro_principal)
    centrar_objeto(posicion_texto, texto_rect, caja)
    return texto, caja, texto_rect


def idiomas_pokemon(ventana, fuente, color_texto, color_caja,posicion_x, posicion_y, ancho, alto, nombre_frances, nombre_italiano, nombre_aleman):
    titulo_frances, rect_titulo_frances = crear_texto_rect(nombre_frances, fuente, color_texto)
    titulo_italiano, rect_titulo_italiano = crear_texto_rect(nombre_italiano, fuente, color_texto)
    titulo_aleman, rect_titulo_aleman = crear_texto_rect(nombre_aleman, fuente, color_texto)

    cuadro_frances = crear_rectangulo_objeto(posicion_x, posicion_y, ancho, alto, True, "midright", rect_titulo_frances)
    cuadro_italiano = crear_rectangulo_objeto(posicion_x + ancho + 10, posicion_y, ancho, alto, True, "midright", rect_titulo_italiano)
    cuadro_aleman = crear_rectangulo_objeto(posicion_x + ancho * 2 + 20, posicion_y, ancho, alto, True, "midright", rect_titulo_aleman)

    pygame.draw.rect(ventana, color_caja, cuadro_frances, border_radius=8)    # caja frances
    pygame.draw.rect(ventana, color_caja, cuadro_italiano, border_radius=8)    # caja italiano
    pygame.draw.rect(ventana, color_caja, cuadro_aleman, border_radius=8)    # caja  aleman

    ventana.blit(titulo_frances, rect_titulo_frances) #nombre frances
    ventana.blit(titulo_italiano, rect_titulo_italiano) #nombre italiano
    ventana.blit(titulo_aleman, rect_titulo_aleman) #nombre aleman

"""
def blitear_objeto(nombre_ventana, texto, rectangulo):
    nombre_ventana.blit(texto, rectangulo) # no lo conozco


def pantalla_inicial(nombre_ventana, ):
    #Se puede hacer con una matriz para no recibir todo por parametro
    texto_rect = texto.get_rect()
    texto_rect.center = cuadro_de_texto.center
    nombre_ventana.blit(texto, texto_rect)  # texto del cuadro de texto

    nombre_ventana.blit(titulo, titulo_rect)  # titulo
    nombre_ventana.blit(texto_boton, boton_rect) # no lo conozco

    nombre_ventana.blit(texto_gen, texto_rect_gen)  # titulo generaciones
    nombre_ventana.blit(texto_boton_gen_1, texto_rect_gen_1)
    nombre_ventana.blit(texto_boton_gen_2, texto_rect_gen_2)
    nombre_ventana.blit(texto_boton_gen_3, texto_rect_gen_3)

    nombre_ventana.blit(titulo_tabla_puntos, rect_titulo_tabla_puntos) #Titulo tabla puntos
    nombre_ventana.blit(titulo_puntos, rect_titulo_puntos) #Titulo racha actual
    nombre_ventana.blit(titulo_mejor_racha, rect_titulo_mejor_racha) #Titulo mejor racha
    
    nombre_ventana.blit(titulo_frances, rect_titulo_frances) #nombre frances
    nombre_ventana.blit(titulo_italiano, rect_titulo_italiano) #nombre italiano
    nombre_ventana.blit(titulo_aleman, rect_titulo_aleman) #nombre aleman
"""