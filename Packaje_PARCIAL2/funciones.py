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


def cargar_nuevo_pokemon(lista_pokemones: list, eneable_gen_1: bool, eneable_gen_2: bool, eneable_gen_3: bool, ancho_imagen: int, alto_imagen: int, is_facil: bool):
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
    if is_facil:
        ruta_imagen_silueta = pokemon_actual['imagen_normal']
    else:
        ruta_imagen_silueta = pokemon_actual['silueta']
    
    ruta_imagen_normal = pokemon_actual['imagen_normal']
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


def crear_texto_rect(dicc_bliteos: dict, key:str, texto: str, fuente, color):
    texto_mostrar = fuente.render(texto, True, color)
    texto_rect = texto_mostrar.get_rect()
    #texto_rect.center = (ANCHO_VENTANA // 2, 60)
    dicc_bliteos[key] = [texto_mostrar, texto_rect]
    return texto_mostrar, texto_rect

def crear_rectangulo_objeto(dicc_dibujos: dict, key: str,posicion_x, posicion_y, ancho, alto, centrar: bool, posicion, objeto_a_centar, color, border_radius):
    rectangulo_objeto = pygame.Rect(posicion_x, posicion_y, ancho, alto)
    if centrar:
        centrar_objeto(posicion, objeto_a_centar, rectangulo_objeto)

    dicc_dibujos[key] = [color, rectangulo_objeto, border_radius]
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


def crear_texto_en_caja(dicc_bliteos: dict, key:str, dicc_dibujos: dict, texto, fuente_texto, color_texto, color_caja,ancho_caja, alto_caja, cuadro_principal, posicion_caja, posicion_texto):
    lista_atributos = []
    texto, texto_rect = crear_texto_rect(dicc_bliteos, key, texto, fuente_texto, color_texto)
    lista_atributos.append(texto)

    caja = crear_rectangulo_objeto(dicc_dibujos, texto, 0, 0, ancho_caja, alto_caja, False, None ,None, color_caja, 12) #Blanco
    centrar_objeto(posicion_caja, caja, cuadro_principal)
    centrar_objeto(posicion_texto, texto_rect, caja)
    lista_atributos.append(caja)
    lista_atributos.append(texto_rect)


    return lista_atributos

def idiomas_pokemon(ventana, dicc_bliteos, dicc_dibujos: dict,fuente, color_texto, color_caja,posicion_x, posicion_y, ancho, alto, nombre_frances, nombre_italiano, nombre_aleman):
    titulo_frances, rect_titulo_frances = crear_texto_rect(dicc_bliteos, "nombre_frances", nombre_frances, fuente, color_texto)
    titulo_italiano, rect_titulo_italiano = crear_texto_rect(dicc_bliteos, "nombre_italiano", nombre_italiano, fuente, color_texto)
    titulo_aleman, rect_titulo_aleman = crear_texto_rect(dicc_bliteos, "nombre_aleman", nombre_aleman, fuente, color_texto)

    cuadro_frances = crear_rectangulo_objeto(dicc_dibujos, "cuadro_frances",posicion_x, posicion_y, ancho, alto, True, "midright", rect_titulo_frances, (255,255,255), 8)
    cuadro_italiano = crear_rectangulo_objeto(dicc_dibujos, "cuadro_italiano",posicion_x + ancho + 10, posicion_y, ancho, alto, True, "midright", rect_titulo_italiano, (255,255,255), 8)
    cuadro_aleman = crear_rectangulo_objeto(dicc_dibujos, "cuadro_aleman",posicion_x + ancho * 2 + 20, posicion_y, ancho, alto, True, "midright", rect_titulo_aleman, (255,255,255), 8)

    pygame.draw.rect(ventana, color_caja, cuadro_frances, border_radius=8)    # caja frances
    pygame.draw.rect(ventana, color_caja, cuadro_italiano, border_radius=8)    # caja italiano
    pygame.draw.rect(ventana, color_caja, cuadro_aleman, border_radius=8)    # caja  aleman

    ventana.blit(titulo_frances, rect_titulo_frances) #nombre frances
    ventana.blit(titulo_italiano, rect_titulo_italiano) #nombre italiano
    ventana.blit(titulo_aleman, rect_titulo_aleman) #nombre aleman

def mejorar_racha(path, racha_actual: int):
    with open(path, "r") as archivo:
        racha_csv = archivo.read()
        racha_csv.strip()
        racha_csv = int(racha_csv)
    nueva_racha = racha_csv

    if racha_actual > racha_csv:
        with open(path, "w") as archivo:
            archivo.write(str(racha_actual) + '\n')
            nueva_racha = racha_actual
    return racha_csv, nueva_racha

def blitear_objetos(ventana, diccionario_objetos, texto, cuadro_texto):
    texto_rect = texto.get_rect()
    texto_rect.center = cuadro_texto.center
    ventana.blit(texto, texto_rect)  # texto del cuadro de texto

    for elemento in diccionario_objetos.values():
        ventana.blit(elemento[0], elemento[1])

def actualizar_elemento(diccionario, clave, nueva_imagen=None, nueva_posicion=None):
    if clave in diccionario:
        if nueva_imagen:
            diccionario[clave][0] = nueva_imagen
        if nueva_posicion:
            diccionario[clave][1] = nueva_posicion

def dibujar_rectangulos(ventana, diccionario_dibujos):
    for elemento in diccionario_dibujos.values():
        pygame.draw.rect(ventana, elemento[0], elemento[1], border_radius = elemento[2])


def juego_terminado(ventana, dicc_bliteos, dicc_dibujos,color_letras, color_fondo, ancho_ventana, alto_ventana,fuente, list_posicion_boton: list, imagen_titulo):
    #----------------Tabla de tiempos----------------------
    ancho_caja_tiempos = 400
    alto_caja_tiempos = 400
    posicion_tiempos_x = (ancho_ventana - ancho_caja_tiempos) / 2
    posicion_tiempos_y = ((alto_ventana - alto_caja_tiempos) / 2) + 30

    titulo_tabla_tiempo, rect_tabla_final = crear_texto_rect(dicc_bliteos, "tiempo", "Tiempo: ", fuente, color_letras)
    cuadro_tiempo = crear_rectangulo_objeto(dicc_dibujos, "cuadro_tiempo",posicion_tiempos_x, posicion_tiempos_y, ancho_caja_tiempos, alto_caja_tiempos, True, "midtop", rect_tabla_final, (255,255,255), 8)
    
    texto_jugar_de_nuevo, boton_rect_jugar = crear_texto_rect(dicc_bliteos, "jugar_de_nuevo", "Jugar de nuevo",fuente, color_letras,)
    cuadro_jugar = crear_rectangulo_objeto(dicc_dibujos, "cuadro_jugar",list_posicion_boton[0], list_posicion_boton[1], list_posicion_boton[2], list_posicion_boton[3], True, "center", boton_rect_jugar, (255,255,255), 8)

    ventana.blit(imagen_titulo, ((ancho_ventana - 400) / 2, 20)) #imagen titulo
    ventana.blit(titulo_tabla_tiempo, rect_tabla_final)
    ventana.blit(texto_jugar_de_nuevo, boton_rect_jugar)

    pygame.draw.rect(ventana, color_fondo, cuadro_tiempo, border_radius = 12)
    pygame.draw.rect(ventana, color_fondo, cuadro_jugar, border_radius = 8)
    #pygame.display.update()

    return cuadro_jugar

def promedio_tiempos(lista_tiempos: list) -> float:
    suma_tiempos = 0

    try:
        if len(lista_tiempos) == 3: # cambiar a 10
            for tiempo in lista_tiempos:
                suma_tiempos += tiempo
            promedio = suma_tiempos / 3 #cambiar a 10
        else:
            promedio = 0
    except:
        promedio = 0
    promedio = float("{:.2f}".format(promedio))
    return promedio


def contar_segundos(dicc_bliteos, dicc_dibujos, tiempo_inicial: int, fuente_texto_segundos, color_texto_segundos, posicion_tiempos_x: int , posicion_tiempos_y: int, ancho_caja_tiempos: int, alto_caja_tiempos: int):
    # _descripcion_
    #
    #    Argumento:
    #      dicc_bliteos [tipoDeDato] -> _description_
    #      tiempo_transcurrido [tipoDeDato] -> _description_
    #      fuente_texto_segundos [tipoDeDato] -> _description_
    #      color_texto_segundos [tipoDeDato] -> _description_
    #      posicion_tiempos_x [tipoDeDato] -> _description_
    #      posicion_tiempos_y [tipoDeDato] -> _description_
    #      ancho_caja_tiempos [tipoDeDato] -> _description_
    #      alto_caja_tiempos [tipoDeDato] -> _description_
    #    Retorna:
    #      cuadro_tiempo -> _description_
    tiempo_transcurrido = pygame.time.get_ticks() // 1000 - tiempo_inicial
    contador_segundos = tiempo_transcurrido
    titulo_tabla_tiempo, rect_titulo_tabla_timepo = crear_texto_rect(dicc_bliteos, "tiempo"," Tiempo: " + str(contador_segundos) + "s", fuente_texto_segundos, color_texto_segundos)
    cuadro_tiempo = crear_rectangulo_objeto(dicc_dibujos, " Tiempo: ",posicion_tiempos_x, posicion_tiempos_y, ancho_caja_tiempos, alto_caja_tiempos, True, "midleft", rect_titulo_tabla_timepo, (255,255,255), 8)
    actualizar_elemento(dicc_bliteos, "tiempo", titulo_tabla_tiempo, rect_titulo_tabla_timepo)
    
    return cuadro_tiempo, contador_segundos

def no_lo_conozco(ventana, lista_pokemon, posicion_cuadro_imagen_x, posicion_cuadro_imagen_y, cuadro_de_texto,fuente, color):
    # _descripcion_
    #
    #    Argumento:
    #      parametro [tipoDeDato] -> _description_
    #    Retorna:
    #      retorna -> _description_
    print("no lo se")
    ventana.blit(lista_pokemon[2], (posicion_cuadro_imagen_x, posicion_cuadro_imagen_y))
    texto = fuente.render(lista_pokemon[0], True, color)
    texto_rect = texto.get_rect()
    texto_rect.center = cuadro_de_texto.center
    ventana.blit(texto, texto_rect)  # texto del cuadro de texto

    pygame.display.update()
    pygame.time.wait(2000)

def actualizar_tabla(dicc_bliteos: dict, dicc_dibujos: dict,contador: int, racha: int,fuente, color_texto, ancho, alto, cuadro_racha):
    # _descripcion_
    #
    #    Argumento:
    #      parametro [tipoDeDato] -> _description_
    #    Retorna:
    #      retorna -> _description_
    lista_caja_actual = crear_texto_en_caja(dicc_bliteos, "actual",dicc_dibujos, "Actual: " + str(contador), fuente, color_texto, (255,255,255),ancho, alto, cuadro_racha, "center", "midleft")
    actualizar_elemento(dicc_bliteos, "actual", lista_caja_actual[0], lista_caja_actual[2])

    lista_caja_mejor_racha = crear_texto_en_caja(dicc_bliteos, "mejor",dicc_dibujos,"Mejor:  " + str(racha), fuente, color_texto, (255,255,255),ancho, alto, cuadro_racha, "midbottom", "midleft")
    actualizar_elemento(dicc_bliteos, "titulo_mejor_racha", lista_caja_mejor_racha[0], lista_caja_mejor_racha[2])

    return lista_caja_actual[1], lista_caja_mejor_racha[1]

def actualizar_tiempos(dicc_bliteos: dict, dicc_dibujos,lista_tiempos: list, tiempo_anterior, fuente, color, posicion_x, posicion_y,ancho, alto): #posicion_x, posicion_y distinta posicion para mejor tiempo
    # _descripcion_
    #
    #    Argumento:
    #      dicc_bliteos [dict] -> _description_
    #    Retorna:
    #      retorna -> _description_
    mejor_tiempo = get_mejor_tiempo(lista_tiempos)
    ancho_caja = 220
    alto_caja = 130

    titulo_tabla_mejor_tiempo, rect_titulo_tabla_mejor_tiempo = crear_texto_rect(dicc_bliteos, "mejor_tiempo"," Mejor tiempo: " + str(mejor_tiempo), fuente, color)
    actualizar_elemento(dicc_bliteos, "mejor_tiempo", titulo_tabla_mejor_tiempo, rect_titulo_tabla_mejor_tiempo)  
    tabla_tiempo = crear_rectangulo_objeto(dicc_dibujos,"tabla_tiempo",posicion_x, posicion_y, ancho_caja, alto_caja, True, "topleft", rect_titulo_tabla_mejor_tiempo, (255,255,255), 8)
    
    
    lista_tiempo_anteriror = crear_texto_en_caja(dicc_bliteos, "tiempo_anterior",dicc_dibujos," Tiempo anterior: " + str(tiempo_anterior) + "s", fuente, color, (255,255,255),ancho, alto, tabla_tiempo, "midleft", "midleft")
    actualizar_elemento(dicc_bliteos, "tiempo_anterior", lista_tiempo_anteriror[0], lista_tiempo_anteriror[2])

    promedio = promedio_tiempos(lista_tiempos)

    lista_tiempo_promedio = crear_texto_en_caja(dicc_bliteos, "tiempo_promedio",dicc_dibujos, " Tiempo promedio: " + str(promedio) + "s", fuente, color, (255,255,255),ancho, alto, tabla_tiempo, "bottomleft", "midleft")
    actualizar_elemento(dicc_bliteos, "tiempo_promedio", lista_tiempo_promedio[0], lista_tiempo_promedio[2])  

    return lista_tiempo_anteriror[1], lista_tiempo_promedio[1], rect_titulo_tabla_mejor_tiempo

def get_mejor_tiempo(lista_tiempos: list):
    # _descripcion_
    #
    #    Argumento:
    #      lista_tiempos [list] -> _description_
    #    Retorna:
    #      mejor_tiempo -> _description_
    mejor_tiempo = 99999999999

    for i in range(len(lista_tiempos)):
        if lista_tiempos[i] < mejor_tiempo:
            mejor_tiempo = lista_tiempos[i]
    
    return mejor_tiempo

def desbliterar_elementos(dicc_bliteos: dict, dicc_dibujos: dict):
    # _descripcion_
    #
    #    Argumento:
    #      dicc_bliteos [dict] -> _description_
    #    Retorna:
    #      retorna -> _description_
    dicc_dibujos.pop('cuadro_frances')
    dicc_dibujos.pop('cuadro_italiano')
    dicc_dibujos.pop('cuadro_aleman')
    dicc_bliteos.pop('nombre_frances')
    dicc_bliteos.pop('nombre_italiano')
    dicc_bliteos.pop('nombre_aleman')

def deblitear_todo(diccionario: dict):
    # _descripcion_
    #
    #    Argumento:
    #      diccionario [dict] -> _description_
    #    Retorna:
    #      retorna -> _description_
    
    diccionario.clear()