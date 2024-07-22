import pygame
import random

def cargar_pokemones_en_lista(lista_pokemones: list, pokemones_dicc: dict):
    # Separa todos los pokemones en diccionarios
    #
    #    Argumento:
    #      lista_pokemones [list] -> lista vacia de pokemones
    #      pokemones_dicc [list] -> diccionario con todos los pokemones
    #    Retorna:
    #      lista_pokemones -> lista con los diccionarios de todos los pokemones
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
    # Separa los pokemones por generaiones
    #
    #    Argumento:
    #      lista_pokemones [list] -> lista con diccionarios de los pokemones
    #    Retorna:
    #      retorna -> las tres listas de generaciones
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


def cargar_nuevo_pokemon(lista_pokemones: list, lista_pokemones_jugados: list, eneables_generaciones: list, ancho_imagen: int, alto_imagen: int, is_facil: bool):
    # Inserta en una lista los pokemones y luego elije uno sin repetir los jugados
    #
    #    Argumento:
    #      lista_pokemones [list] -> lista con diccionarios de los pokemones
    #      lista_pokemones_jugados [list] -> lista con los nombre de los pokemones pasados
    #      eneables_generaciones[0] [list] -> list para saber si esta seleccionda esa generacion
    #      eneables_generaciones[1] [list] -> list para saber si esta seleccionda esa generacion
    #      eneables_generaciones[2] [list] -> list para saber si esta seleccionda esa generacion
    #      is_facil [bool] -> bool para saber que dificultad esta seleccionada
    #    Retorna:
    #      lista_atributos_pokemon -> lista con todos los atributos del pokemon seleccionado
    lista_gen1, lista_gen2, lista_gen3 = separar_por_gen(lista_pokemones)
    dos_generaciones = False

    if eneables_generaciones[0]:
        if eneables_generaciones[1] and eneables_generaciones[2]:
            lista_pokemones = lista_gen1 + lista_gen2 + lista_gen3
            print("Se cargaron las 3 generaciones")
        elif eneables_generaciones[1]:
            lista_pokemones = lista_gen1 + lista_gen2
            print("Se cargaron la gen 1 y 2")
            dos_generaciones = True
        elif eneables_generaciones[2]:
            lista_pokemones = lista_gen1 + lista_gen3
            dos_generaciones = True
            print("Se cargaron la gen 1 y 3")
        else:
            lista_pokemones = lista_gen1
            print("Se cargo la gen 1")
    
    if eneables_generaciones[1] and dos_generaciones == False:
        if eneables_generaciones[2]:
            lista_pokemones = lista_gen2 + lista_gen3
            dos_generaciones = True
            print("Se cargaron la gen 2 y 3")
        else:
            lista_pokemones = lista_gen2
            print("Se cargo la gen 2")
    
    if eneables_generaciones[2] and dos_generaciones == False:
        lista_pokemones = lista_gen3
        print("Se cargo la gen 3")

    pokemon_actual = random.choice(lista_pokemones)
    while pokemon_actual['nombre'] in lista_pokemones_jugados:
        pokemon_actual = random.choice(lista_pokemones)
    else:
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

    lista_pokemones_jugados.append(pokemon_actual['nombre'])
    #Este se puede hacer en una funcion que carge y escale
    silueta_aleatoria = pygame.image.load(ruta_imagen_silueta)
    silueta_aleatoria = pygame.transform.scale(silueta_aleatoria, (ancho_imagen, alto_imagen))

    pokemon_resuelto = pygame.image.load(ruta_imagen_normal)
    pokemon_resuelto = pygame.transform.scale(pokemon_resuelto, (ancho_imagen, alto_imagen))

    dicc_atributos_pokemon = {
        'nombre_pokemon': nombre_pokemon, 
        'silueta_aleatoria': silueta_aleatoria, 
        'pokemon_resuelto': pokemon_resuelto,
        'generacion_pokemon': generacion_pokemon,
        'nombre_frances': nombre_frances, 
        'nombre_italiano': nombre_italiano, 
        'nombre_aleman': nombre_aleman
    }
    return dicc_atributos_pokemon

def crear_matriz_valores(posicion_x, posicion_y, ancho: int, alto: int):
    # _descripcion_
    #
    #    Argumento:
    #      posicion_x [tipoDeDato] -> _description_
    #    Retorna:
    #      retorna -> _description_
    matriz_valores = [
        [posicion_x, posicion_y],
        [ancho, alto]
    ]

    return matriz_valores

def pokemon_ya_jugado(lista_pokemon_a_jugar: list, lista_pokemones_jugados: list, json_pokemones):
    # En caso del que el pokemon elejido por el choice ya se haya jugado lo vuelvo a elegir hasta que sea uno diferente
    #
    #    Argumento:
    #      lista_pokemon_a_jugar [list] -> atributos del pokemon elegido
    #      lista_pokemones_jugados [list] -> lista con los nombre de los pokemones ya jugados
    #      json_pokemones -> Archivo jsonn donde estan todos los pokemones
    #    Retorna:
    #      retorna -> _description_
    while lista_pokemon_a_jugar[0] in lista_pokemones_jugados:
        for i in range(len(lista_pokemones_jugados)):
            if lista_pokemon_a_jugar[0] == lista_pokemones_jugados[i]:
                ya_jugado = True
            else:
                ya_jugado = False

        if ya_jugado:
            lista_pokemon_a_jugar = cargar_pokemones_en_lista(lista_pokemon_a_jugar, json_pokemones)
    return lista_pokemon_a_jugar


def crear_texto_rect(dicc_bliteos: dict, key:str, texto: str, fuente, color):
    # Crear un texto y retorna el texto con la caja del mismo
    #
    #    Argumento:
    #      dicc_bliteos [dict] -> Todos los elementos a blitear
    #      key [str] -> Identificador del texto a crear
    #    Retorna:
    #      retorna -> Texto creado con su rectangulo
    texto_mostrar = fuente.render(texto, True, color)
    texto_rect = texto_mostrar.get_rect()
    #texto_rect.center = (ANCHO_VENTANA // 2, 60)
    dicc_bliteos[key] = [texto_mostrar, texto_rect]

    elementos_texto = {
        'texto': texto_mostrar,
        'texto_rect': texto_rect
    }

    return elementos_texto

def crear_dicc_posicionar(posicion: str, caja, color_boton, border_radius: int):
    # _descripcion_
    #
    #    Argumento:
    #      posicion [str] -> _description_
    #    Retorna:
    #      retorna -> _description_
    posicionar_cuadro_boton = {
        'posicion': posicion,
        'caja': caja,
        'color_boton': color_boton,
        'border_radius': border_radius
    }
    return posicionar_cuadro_boton

def dicc_atributos_texto(fuente, color_texto, color_fondo, ancho: int, alto: int, caja):
    # _descripcion_
    #
    #    Argumento:
    #      posicion [str] -> _description_
    #    Retorna:
    #      retorna -> _description_
    dicc_atributos_crear_caja = {
        'fuente': fuente,
        'color_texto': color_texto,
        'color_fondo': color_fondo,
        'ancho': ancho,
        'alto': alto,
        'caja': caja
    }
    return dicc_atributos_crear_caja

def crear_rectangulo_objeto(dicc_dibujos: dict, key: str, atributos_boton, centrar: bool, atributos_posicionar):
    # Crear un rectangulo de un objeto y lo coloca en el metodo ingresado
    #
    #    Argumento:
    #      dicc_dibujos [dict] -> Todos los elementos a dibujar
    #      key [str] -> Identificador del texto a crear
    #      centrar [bool] -> habilitador para posicionar el elemento en otra caja
    #    Retorna:
    #      rectangulo_objeto -> Rectangulo del objeto creado
    rectangulo_objeto = pygame.Rect(atributos_boton[0][0], atributos_boton[0][1], atributos_boton[1][0], atributos_boton[1][1])
    if centrar:
        centrar_objeto(atributos_posicionar['posicion'], atributos_posicionar['caja'], rectangulo_objeto)

    dicc_dibujos[key] = [atributos_posicionar['color_boton'], rectangulo_objeto, atributos_posicionar['border_radius']]
    return rectangulo_objeto

def centrar_objeto(posicion: str, objeto_a_centar, rectangulo_objeto):
    # Posiciona un rectangulo dentro de una caja
    #
    #    Argumento:
    #      posicion [str] -> metodo a utilizar
    #      objeto_a_centar -> Objero que se quiere posicionar
    #      rectangulo_objeto -> Caja en donde se posicionar el objeto
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


def crear_texto_en_caja(dicc_bliteos: dict, key:str, dicc_dibujos: dict, texto, dicc_atributos_texto, posicion_caja, posicion_texto):
    # Crear un rectangulo de un objeto y lo coloca en el metodo ingresado
    #
    #    Argumento:
    #      dicc_bliteos [dict] -> Todos los elementos a blitear
    #      key [str] -> Identificador del texto a crear
    #      centrar [bool] -> habilitador para posicionar el elemento en otra caja
    #    Retorna:
    #      rectangulo_objeto -> Rectangulo del objeto creado
    lista_atributos = []
    dicc_texto_rect = crear_texto_rect(dicc_bliteos, key, texto, dicc_atributos_texto['fuente'], dicc_atributos_texto['color_texto'])
    lista_atributos.append(texto)

    atributos_texto = crear_dicc_posicionar("midtop", dicc_texto_rect['texto_rect'], (255,255,255), 8)
    
    atributos_caja = crear_matriz_valores(0, 0, dicc_atributos_texto['ancho'], dicc_atributos_texto['alto'])
    caja = crear_rectangulo_objeto(dicc_dibujos, key, atributos_caja, False, atributos_texto) #Blanco
    centrar_objeto(posicion_caja, caja, dicc_atributos_texto['caja'])
    centrar_objeto(posicion_texto, dicc_texto_rect['texto_rect'], caja)
    lista_atributos.append(caja)
    lista_atributos.append(dicc_texto_rect['texto_rect'])


    return lista_atributos

def idiomas_pokemon(ventana, dicc_bliteos, dicc_dibujos: dict,fuente, color_texto, color_caja,posicion_x, posicion_y, ancho, alto, nombre_frances, nombre_italiano, nombre_aleman):
    # Crea, dibuja y blitea las cajas de los idiomas de los pokemones con sus traducciones
    #
    #    Argumento:
    #      dicc_bliteos [dict] -> Todos los elementos a blitear
    #      dicc_dibujos [dict] -> Todos los elementos a dibujar
    #      nombre_aleman [str] -> nombre del pokemon traducido
    #      nombre_italiano [str] -> nombre del pokemon traducido
    #      nombre_frances [str] -> nombre del pokemon traducido
    rect_titulo_frances = crear_texto_rect(dicc_bliteos, "nombre_frances", nombre_frances, fuente, color_texto)
    rect_titulo_italiano = crear_texto_rect(dicc_bliteos, "nombre_italiano", nombre_italiano, fuente, color_texto)
    rect_titulo_aleman = crear_texto_rect(dicc_bliteos, "nombre_aleman", nombre_aleman, fuente, color_texto)

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
    # Lee del CSV cual es la mejor racha
    #
    #    Argumento:
    #      path -> Ruta del archivo CSV
    #      racha_actual -> Racha en la que se esta jugando
    #    Retorna:
    #      Retorna -> Racha del csv
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
    # Recibe un diccionarios con los elementos a blitear e itera en la cantidad de elementos
    #
    #    Argumento:
    #      diccionario_objetos -> Todos los elementos a blitear
    #      texto -> Texto ingresado por el usuario
    #      cuadro_texto -> nombre del pokemon traducido
    texto_rect = texto.get_rect()
    texto_rect.center = cuadro_texto.center
    ventana.blit(texto, texto_rect)  # texto del cuadro de texto

    for elemento in diccionario_objetos.values():
        ventana.blit(elemento[0], elemento[1])

def dibujar_rectangulos(ventana, diccionario_dibujos):
    # Recibe un diccionario con los elementos a dibujar e itera en la cantidad de elementos
    #
    #    Argumento:
    #      diccionario_dibujos -> Todos los rectangulos a dibujar
    for elemento in diccionario_dibujos.values():
        pygame.draw.rect(ventana, elemento[0], elemento[1], border_radius = elemento[2])

def actualizar_elemento(diccionario, clave, nueva_imagen=None, nueva_posicion=None):
    # Modifica en el diccionario el objeto que se modifica dentro del bucle
    #
    #    Argumento:
    #      diccionario [dict] -> Todos los elementos a blitear
    #      clave [str] -> identificador del elemento modificado
    #      nueva_imagen -> texto modificado
    #      nueva_posicion -> rectangulo del elemento modificado
    if clave in diccionario:
        if nueva_imagen:
            diccionario[clave][0] = nueva_imagen
        if nueva_posicion:
            diccionario[clave][1] = nueva_posicion

def actualizar_tabla(dicc_bliteos: dict, dicc_dibujos: dict,contador: int, racha: int, dicc_atributos_texto: dict):
    # Actualiza el valor de racha actual
    #
    #    Argumento:
    #      dicc_bliteos [dict] -> diccionario con los elementos a blitear
    #      dicc_dibujos [dict] -> diccionario con los elementos a dibujar
    #      contador [int] -> Cantidad de veces que se ascerto el pokemon
    #      racha [int] -> Numero de rachas del jugador
    #    Retorna:
    #      retorna -> Rectangulo de las cajas creadas
    lista_caja_actual = crear_texto_en_caja(dicc_bliteos, "actual",dicc_dibujos, "Actual: " + str(contador), dicc_atributos_texto, "center", "midleft")
    actualizar_elemento(dicc_bliteos, "actual", lista_caja_actual[0], lista_caja_actual[2])

    lista_caja_mejor_racha = crear_texto_en_caja(dicc_bliteos, "mejor",dicc_dibujos,"Mejor:  " + str(racha), dicc_atributos_texto, "midbottom", "midleft")
    actualizar_elemento(dicc_bliteos, "titulo_mejor_racha", lista_caja_mejor_racha[0], lista_caja_mejor_racha[2])

    return lista_caja_actual[1], lista_caja_mejor_racha[1]

def actualizar_tiempos(dicc_bliteos: dict, dicc_dibujos: dict, dicc_tabla: dict, lista_elementos_texto: list): #posicion_x, posicion_y distinta posicion para mejor tiempo
    # Actualiza todos los valores de la tabla de tiempos
    #
    #    Argumento:
    #      dicc_bliteos [dict] -> diccionario con los elementos a blitear
    #      dicc_dibujos [dict] -> diccionario con los elementos a dibujar
    #      lista_tiempos [list] -> Todos los tiempor de las partidas
    #      tiempo_anterior [int] -> Tiempo anterior
    #    Retorna:
    #      retorna -> Las cajas de los tres tiempos
    mejor_tiempo = get_mejor_tiempo(lista_elementos_texto[0])
    ancho_caja = 220
    alto_caja = 130

    titulo_tabla_mejor_tiempo, rect_titulo_tabla_mejor_tiempo = crear_texto_rect(dicc_bliteos, "mejor_tiempo"," Mejor tiempo: " + str(mejor_tiempo), dicc_tabla['fuente'], dicc_tabla['color_texto'])
    actualizar_elemento(dicc_bliteos, "mejor_tiempo", titulo_tabla_mejor_tiempo, rect_titulo_tabla_mejor_tiempo)  
    tabla_tiempo = crear_rectangulo_objeto(dicc_dibujos,"tabla_tiempo",lista_elementos_texto[2], lista_elementos_texto[3], ancho_caja, alto_caja, True, "topleft", rect_titulo_tabla_mejor_tiempo, dicc_tabla['color_fondo'], 8)
    
    dicc_texto_tiempos = dicc_atributos_texto(dicc_tabla['fuente'], dicc_tabla['color_texto'], dicc_tabla['color_fondo'], dicc_tabla['ancho'], dicc_tabla['alto'], tabla_tiempo)
    lista_tiempo_anteriror = crear_texto_en_caja(dicc_bliteos, "tiempo_anterior",dicc_dibujos," Tiempo anterior: " + str(lista_elementos_texto[1]) + "s", dicc_texto_tiempos, "midleft", "midleft")
    actualizar_elemento(dicc_bliteos, "tiempo_anterior", lista_tiempo_anteriror[0], lista_tiempo_anteriror[2])

    promedio = promedio_tiempos(lista_elementos_texto[0])

    lista_tiempo_promedio = crear_texto_en_caja(dicc_bliteos, "tiempo_promedio",dicc_dibujos, " Tiempo promedio: " + str(promedio) + "s", dicc_texto_tiempos, "bottomleft", "midleft")
    actualizar_elemento(dicc_bliteos, "tiempo_promedio", lista_tiempo_promedio[0], lista_tiempo_promedio[2])  

    dicc_resultados = {
        'tiempo_anterior': lista_tiempo_anteriror[1],
        'tiempo_promedio': lista_tiempo_promedio[1],
        'rect_titulo_tabla': rect_titulo_tabla_mejor_tiempo
    }

    return dicc_resultados


def promedio_tiempos(lista_tiempos: list) -> float:
    # Realiza un promedio de todos los tiempos guardados en la partida
    #
    #    Argumento:
    #      lista_tiempos [list] -> Todos los tiempos de respuesta
    #    Retorna:
    #      promedio -> numero del promedio de tiempo
    suma_tiempos = 0

    for tiempo in lista_tiempos:
        suma_tiempos += tiempo
    promedio = suma_tiempos / len(lista_tiempos)

    promedio = float("{:.2f}".format(promedio)) # Corta a al segundo decimal
    return promedio


def contar_segundos(dicc_bliteos, dicc_dibujos, tiempo_inicial: int, fuente_texto_segundos, color_texto_segundos, posicion_tiempos_x: int , posicion_tiempos_y: int, ancho_caja_tiempos: int, alto_caja_tiempos: int):
    # Cuenta cada 1 segundo y crea los textos en las cajas para mostrarlos en el juego
    #
    #    Argumento:
    #      dicc_bliteos [dict] -> Diccinario con todos los elementos a blitear
    #      dicc_dibujos [dict] -> Diccinario con todos los elementos a dibujar
    #      tiempo_inicial [int] -> Sengundo en el que comenzo el contador
    #    Retorna:
    #      retorna -> Cuadro de las dos cajas creadas
    tiempo_transcurrido = pygame.time.get_ticks() // 1000 - tiempo_inicial
    contador_segundos = tiempo_transcurrido
    titulo_tabla_tiempo, rect_titulo_tabla_timepo = crear_texto_rect(dicc_bliteos, "tiempo"," Tiempo: " + str(contador_segundos) + "s", fuente_texto_segundos, color_texto_segundos)
    cuadro_tiempo = crear_rectangulo_objeto(dicc_dibujos, " Tiempo: ",posicion_tiempos_x, posicion_tiempos_y, ancho_caja_tiempos, alto_caja_tiempos, True, "midleft", rect_titulo_tabla_timepo, (255,255,255), 8)
    actualizar_elemento(dicc_bliteos, "tiempo", titulo_tabla_tiempo, rect_titulo_tabla_timepo)
    
    return cuadro_tiempo, contador_segundos

def no_lo_conozco(ventana, dicc_pokemon, posicion_cuadro_imagen_x, posicion_cuadro_imagen_y, cuadro_de_texto,fuente, color):
    # Elementos a mostrar cuando se pulsa el boton de no conocer el pokemon
    print("no lo se")
    ventana.blit(dicc_pokemon['pokemon_resuelto'], (posicion_cuadro_imagen_x, posicion_cuadro_imagen_y))
    texto = fuente.render(dicc_pokemon['nombre_pokemon'], True, color)
    texto_rect = texto.get_rect()
    texto_rect.center = cuadro_de_texto.center
    ventana.blit(texto, texto_rect)  # texto del cuadro de texto

    pygame.display.update()
    pygame.time.wait(2000)


def get_mejor_tiempo(lista_tiempos: list):
    # Obtine el menor tiempo de todos
    #
    #    Argumento:
    #      lista_tiempos [list] -> Todos los tiempos de la partida
    #    Retorna:
    #      mejor_tiempo -> El tiempo menor dentro de la lista
    mejor_tiempo = 99999999999

    for i in range(len(lista_tiempos)):
        if lista_tiempos[i] < mejor_tiempo:
            mejor_tiempo = lista_tiempos[i]
    
    return mejor_tiempo

def desblitear_idiomas(dicc_bliteos: dict, dicc_dibujos: dict):
    # Elimina los cuadros de los idiomas luego del muestreo
    #
    #    Argumento:
    #      dicc_bliteos [dict] -> Diccinario con todos los elementos a blitear
    #      dicc_dibujos [dict] -> Diccinario con todos los elementos a dibujar
    dicc_dibujos.pop('cuadro_frances')
    dicc_dibujos.pop('cuadro_italiano')
    dicc_dibujos.pop('cuadro_aleman')
    dicc_bliteos.pop('nombre_frances')
    dicc_bliteos.pop('nombre_italiano')
    dicc_bliteos.pop('nombre_aleman')

def mostrar_cuadro_final_partida(ventana, dicc_bliteos, dicc_dibujos, ancho_ventana, alto_ventana, fuente_resultado, lista_tiempos):
    # Muestra los resultado de los tiempo de la partida una vez terminada
    #
    #    Argumento:
    #      dicc_bliteos [dict] -> Diccinario con todos los elementos a blitear
    #      dicc_dibujos [dict] -> Diccinario con todos los elementos a dibujar
    # Fondo del cuadro de fin de partida
    ancho_caja_tiempos = 450
    alto_caja_tiempos = 450
    posicion_tiempos_x = (ancho_ventana - ancho_caja_tiempos) / 2
    posicion_tiempos_y = ((alto_ventana - alto_caja_tiempos) / 2) + 30
    color_letras = (0,0,0)
    color_fondo_objetos = (255,255,255)
    mejor_tiempo = get_mejor_tiempo(lista_tiempos)
    tiempo_promedio = promedio_tiempos(lista_tiempos)

    titulo_tabla_tiempo, rect_tabla_final = crear_texto_rect(dicc_bliteos, "tiempos","Juego Terminado", fuente_resultado, color_letras)
    cuadro_tiempo = crear_rectangulo_objeto(dicc_dibujos, "cuadro_tiempo", posicion_tiempos_x, posicion_tiempos_y, ancho_caja_tiempos, alto_caja_tiempos, True, "midtop", rect_tabla_final, color_fondo_objetos, 8)

    titulo_mejor_tiempo, rect_mejor_tiempo = crear_texto_rect(dicc_bliteos, "mejor_tiempo", " Mejor tiempo: " + str(mejor_tiempo) + "s", fuente_resultado, color_letras)
    cuadro_mejor_tiempo = crear_rectangulo_objeto(dicc_dibujos, "cuadro_mejor_tiempo", ancho_ventana / 2, 300, 0, 0, True, "midtop", rect_mejor_tiempo, color_fondo_objetos, 8)
    

    titulo_tiempo_anterior, rect_tiempo_anterior = crear_texto_rect(dicc_bliteos, "tiempo_anterior", " Mejor tiempo: " + str(mejor_tiempo) + "s", fuente_resultado, color_letras)
    cuadro_tiempo_anterior = crear_rectangulo_objeto(dicc_dibujos, "cuadro_mejor_tiempo", ancho_ventana / 2, 400, 0, 0, True, "midtop", rect_tiempo_anterior, color_fondo_objetos, 8)
    

    titulo_tiempo_promedio, rect_tiempo_promedio = crear_texto_rect(dicc_bliteos, "tiempo_promedio", " Tiempo promedio: " + str(tiempo_promedio) + "s", fuente_resultado, color_letras)
    cuadro_tiempo_promedio = crear_rectangulo_objeto(dicc_dibujos, "cuadro_mejor_tiempo", ancho_ventana / 2, 500, 0, 0, True, "midtop", rect_tiempo_promedio, color_fondo_objetos, 8)

    pygame.draw.rect(ventana, color_fondo_objetos, cuadro_tiempo, border_radius = 12)
    pygame.draw.rect(ventana, color_fondo_objetos, cuadro_mejor_tiempo, border_radius = 8)
    pygame.draw.rect(ventana, color_fondo_objetos, cuadro_tiempo_anterior, border_radius = 8)
    pygame.draw.rect(ventana, color_fondo_objetos, cuadro_tiempo_promedio, border_radius = 8)

    ventana.blit(titulo_tabla_tiempo, rect_tabla_final)
    ventana.blit(titulo_mejor_tiempo, rect_mejor_tiempo)
    ventana.blit(titulo_tiempo_anterior, rect_tiempo_anterior)
    ventana.blit(titulo_tiempo_promedio, rect_tiempo_promedio)
