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

        lista_keys = ['nombre', 'generacion', 'imagen_normal', 'silueta', 'frances', 'italiano', 'aleman']
        lista_valores = [nombre, pokemones["generacion"], pokemones["imagen_normal"], pokemones["silueta"], pokemones["frances"], pokemones["italiano"], pokemones["aleman"]]
        pokemon = crear_diccionarios(lista_keys, lista_valores)

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


def cargar_nuevo_pokemon(lista_pokemones: list, dicc_bools: dict, list_dimenciones_img: list):
    # Inserta en una lista los pokemones y luego elije uno sin repetir los jugados
    #
    #    Argumento:
    #      lista_pokemones [list] -> lista con diccionarios de los pokemones
    #      lista_pokemones_jugados [list] -> lista con los nombre de los pokemones pasados
    #      dicc_bools [dict] -> diccionario con elementos a modificar como las banderas
    #    Retorna:
    #      dicc_atributos_pokemon -> dict con todos los atributos del pokemon seleccionado
    lista_gen1, lista_gen2, lista_gen3 = separar_por_gen(lista_pokemones)
    dos_generaciones = False
    eneables_generaciones = dicc_bools['bool_gen']

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
    while pokemon_actual['nombre'] in dicc_bools['repetidos']:
        pokemon_actual = random.choice(lista_pokemones)
    else:
        if dicc_bools['bool_facil']:
            ruta_imagen_silueta = pokemon_actual['imagen_normal']
        else:
            ruta_imagen_silueta = pokemon_actual['silueta']
        
        ruta_imagen_normal = pokemon_actual['imagen_normal']
        nombre_pokemon = pokemon_actual['nombre']
        generacion_pokemon = pokemon_actual['generacion']
        nombre_frances = pokemon_actual['frances']
        nombre_italiano = pokemon_actual['italiano']
        nombre_aleman = pokemon_actual['aleman']

    dicc_bools['repetidos'].append(pokemon_actual['nombre'])
    #Este se puede hacer en una funcion que carge y escale
    silueta_aleatoria = pygame.image.load(ruta_imagen_silueta)
    silueta_aleatoria = pygame.transform.scale(silueta_aleatoria, (list_dimenciones_img[0], list_dimenciones_img[1]))

    pokemon_resuelto = pygame.image.load(ruta_imagen_normal)
    pokemon_resuelto = pygame.transform.scale(pokemon_resuelto, (list_dimenciones_img[0], list_dimenciones_img[1]))

    lista_keys = ['nombre_pokemon', 'silueta_aleatoria', 'pokemon_resuelto', 'generacion_pokemon', 'nombre_aleman', 'nombre_italiano', 'nombre_frances']
    lista_valores = [nombre_pokemon, silueta_aleatoria, pokemon_resuelto, generacion_pokemon, nombre_aleman, nombre_italiano, nombre_frances]
    dicc_atributos_pokemon = crear_diccionarios(lista_keys, lista_valores)

    return dicc_atributos_pokemon

def crear_matriz_valores(posicion_x, posicion_y, ancho: int, alto: int):
    # Crear una matriz con los atributos de una caja
    #
    #    Argumento:
    #      posicion_x [int] -> valor de la poscion en el eje x
    #      posicion_y [int] -> valor de la poscion en el eje y
    #      ancho [int] -> ancho de la caja
    #      alto [int] -> alto de la caja
    #    Retorna:
    #      matriz_valores -> matriz creada
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
    #      lista_pokemon_a_jugar -> lista con los nombre de los pokemones ya jugados
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
    dicc_bliteos[key] = [texto_mostrar, texto_rect]

    lista_valores = [texto_mostrar, texto_rect]
    lista_keys = ['texto', 'texto_rect']

    elementos_texto = crear_diccionarios(lista_keys, lista_valores)

    return elementos_texto

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
    #      lista_atributos -> Parametro del texto creado
    lista_atributos = []
    dicc_texto_rect = crear_texto_rect(dicc_bliteos, key, texto, dicc_atributos_texto['fuente'], dicc_atributos_texto['color_texto'])
    lista_atributos.append(dicc_texto_rect['texto'])
    lista_keys = ['posicion', 'caja', 'color_boton', 'border_radius']
    lista_valores = ["midtop", dicc_texto_rect['texto_rect'], dicc_atributos_texto['color_fondo'], 8]
    atributos_texto = crear_diccionarios(lista_keys, lista_valores)

    atributos_caja = crear_matriz_valores(0, 0, dicc_atributos_texto['ancho'], dicc_atributos_texto['alto'])
    caja = crear_rectangulo_objeto(dicc_dibujos, key, atributos_caja, False, atributos_texto) #Blanco
    centrar_objeto(posicion_caja, caja, dicc_atributos_texto['caja'])
    centrar_objeto(posicion_texto, dicc_texto_rect['texto_rect'], caja)
    lista_atributos.append(caja)
    lista_atributos.append(dicc_texto_rect['texto_rect'])

    return lista_atributos

def idiomas_pokemon(ventana, dicc_bliteos, dicc_dibujos: dict, atributos_caja, nombres_traducidos):
    # Crea, dibuja y blitea las cajas de los idiomas de los pokemones con sus traducciones
    #
    #    Argumento:
    #      dicc_bliteos [dict] -> Todos los elementos a blitear
    #      dicc_dibujos [dict] -> Todos los elementos a dibujar
    #    Retorna:
    #      nombre_traducidos [list] -> Lista con el nombre del pokemon traducidos
    lista_keys = ['posicion', 'caja', 'color_boton', 'border_radius']

    dicc_tit_fran = crear_texto_rect(dicc_bliteos, "nombre_frances", "FRA: " + str(nombres_traducidos['nombre_frances']), atributos_caja[0], atributos_caja[1])
    dicc_tit_ital = crear_texto_rect(dicc_bliteos, "nombre_italiano", "IT: " + str(nombres_traducidos['nombre_italiano']), atributos_caja[0], atributos_caja[1])
    dicc_tit_ale = crear_texto_rect(dicc_bliteos, "nombre_aleman", "DEU: " + str(nombres_traducidos['nombre_aleman']), atributos_caja[0], atributos_caja[1])

    atributos_frances = crear_matriz_valores(atributos_caja[3][0][0],  atributos_caja[3][0][1],  atributos_caja[3][1][0],  atributos_caja[3][1][1])
    atributos_italiano = crear_matriz_valores(atributos_caja[3][0][0] +  atributos_caja[3][1][0] + 10, atributos_caja[3][0][1],  atributos_caja[3][1][0],  atributos_caja[3][1][1])
    atributos_aleman = crear_matriz_valores(atributos_caja[3][0][0] +  atributos_caja[3][1][0] * 2 + 20, atributos_caja[3][0][1],  atributos_caja[3][1][0],  atributos_caja[3][1][1])

    vla_frances = ["center", dicc_tit_fran['texto_rect'], atributos_caja[2], 8]
    val_italiano = ["center", dicc_tit_ital['texto_rect'], atributos_caja[2], 8]
    val_aleman = ["center", dicc_tit_ale['texto_rect'], atributos_caja[2], 8]

    atributos_texto_fran = crear_diccionarios(lista_keys, vla_frances)
    atributos_texto_ital = crear_diccionarios(lista_keys, val_italiano)
    atributos_texto_ale = crear_diccionarios(lista_keys, val_aleman)

    cuadro_frances = crear_rectangulo_objeto(dicc_dibujos, "cuadro_frances", atributos_frances, True, atributos_texto_fran)
    cuadro_italiano = crear_rectangulo_objeto(dicc_dibujos, "cuadro_italiano", atributos_italiano, True, atributos_texto_ital)
    cuadro_aleman = crear_rectangulo_objeto(dicc_dibujos, "cuadro_aleman", atributos_aleman, True, atributos_texto_ale)    

    pygame.draw.rect(ventana, atributos_caja[2], cuadro_frances, border_radius=8)    # caja frances
    pygame.draw.rect(ventana, atributos_caja[2], cuadro_italiano, border_radius=8)    # caja italiano
    pygame.draw.rect(ventana, atributos_caja[2], cuadro_aleman, border_radius=8)    # caja  aleman

    ventana.blit(dicc_tit_fran['texto'], dicc_tit_fran['texto_rect']) #nombre frances
    ventana.blit(dicc_tit_ital['texto'], dicc_tit_ital['texto_rect']) #nombre italiano
    ventana.blit(dicc_tit_ale['texto'], dicc_tit_ale['texto_rect']) #nombre aleman

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
    ventana.blit(texto, texto_rect)  # texto del cuadro de textox

    for elemento in diccionario_objetos.values():
        ventana.blit(elemento[0], elemento[1])

def dibujar_rectangulos(ventana, diccionario_dibujos):
    # Recibe un diccionario con los elementos a dibujar e itera en la cantidad de elementos
    #
    #    Argumento:
    #      diccionario_dibujos -> Todos los rectangulos a dibujar
    for elemento in diccionario_dibujos.values():
        pygame.draw.rect(ventana, elemento[0], elemento[1], border_radius = elemento[2])

def actualizar_elemento(diccionario, clave, nueva_imagen, nueva_posicion):
    # Modifica en el diccionario el objeto que se modifica dentro del bucle
    #
    #    Argumento:
    #      diccionario [dict] -> Todos los elementos a blitear
    #      clave [str] -> identificador del elemento modificado
    #      nueva_imagen -> elemento modificado
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
    #      dicc_tabla [list] -> Atributos crear tabla
    #      lista_elementos_texto [int] -> Elementos crear texto
    #    Retorna:
    #      dicc_resultados -> elementos modificados
    lista_keys = ['posicion', 'caja', 'color_boton', 'border_radius']
    keys_texto = ['fuente', 'color_texto', 'color_fondo', 'ancho', 'alto', 'caja']
    mejor_tiempo = get_mejor_tiempo(lista_elementos_texto[0])
    ancho_caja = 220
    alto_caja = 130

    atrib_mejor_tiempo = crear_texto_rect(dicc_bliteos, "mejor_tiempo"," Mejor tiempo: " + str(mejor_tiempo), dicc_tabla['fuente'], dicc_tabla['color_texto'])
    actualizar_elemento(dicc_bliteos, "mejor_tiempo", atrib_mejor_tiempo['texto'], atrib_mejor_tiempo['texto_rect'])  

    atributos_dimenciones = crear_matriz_valores(lista_elementos_texto[2], lista_elementos_texto[3], ancho_caja, alto_caja)
    val_texto = ["topleft", atrib_mejor_tiempo['texto_rect'], dicc_tabla['color_fondo'], 8]
    atributos_texto = crear_diccionarios(lista_keys, val_texto)

    tabla_tiempo = crear_rectangulo_objeto(dicc_dibujos, "tabla_tiempo", atributos_dimenciones, True, atributos_texto)
    
    val_texto_tiempo = [dicc_tabla['fuente'], dicc_tabla['color_texto'], dicc_tabla['color_fondo'], dicc_tabla['ancho'], dicc_tabla['alto'], tabla_tiempo]
    dicc_texto_tiempos = crear_diccionarios(keys_texto, val_texto_tiempo)

    lista_tiempo_anteriror = crear_texto_en_caja(dicc_bliteos, "tiempo_anterior",dicc_dibujos," T. anterior: " + str(lista_elementos_texto[1]) + "s", dicc_texto_tiempos, "midleft", "midleft")
    actualizar_elemento(dicc_bliteos, "tiempo_anterior", lista_tiempo_anteriror[0], lista_tiempo_anteriror[1])

    promedio = promedio_tiempos(lista_elementos_texto[0])

    lista_tiempo_promedio = crear_texto_en_caja(dicc_bliteos, "tiempo_promedio", dicc_dibujos, " T. promedio: " + str(promedio) + "s", dicc_texto_tiempos, "bottomleft", "midleft")
    actualizar_elemento(dicc_bliteos, "tiempo_promedio", lista_tiempo_promedio[0], lista_tiempo_promedio[1])  

    lista_keys = ['rect_titulo_tabla', 'tiempo_anterior', 'tiempo_promedio']
    lista_valroes = [atrib_mejor_tiempo['texto_rect'], lista_tiempo_anteriror[1], lista_tiempo_promedio[1]]
    dicc_resultados = crear_diccionarios(lista_keys, lista_valroes)

    return dicc_resultados

def get_mejor_tiempo(lista_tiempos: list):
    # Obtine el menor tiempo de todos
    #
    #    Argumento:
    #      lista_tiempos [list] -> Todos los tiempos de la partida
    #    Retorna:
    #      mejor_tiempo -> El tiempo menor dentro de la lista
    mejor_tiempo = 99999999999

    for i in range(len(lista_tiempos)):
        if lista_tiempos[i] <= mejor_tiempo:
            mejor_tiempo = lista_tiempos[i]
    
    return mejor_tiempo

def get_tiempo_anterior(lista_tiempos: list):
    # Busca el ultimo tiempo de la lista
    #
    #    Argumento:
    #      lista_tiempos [list] -> Todos los tiempos de la partida
    #    Retorna:
    #      tiempo_anterior -> cantidad de segundo en ascentar el pokemon anterior
    for i in range(len(lista_tiempos)):
        tiempo_anterior = lista_tiempos[len(lista_tiempos) - 1]

    return tiempo_anterior

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

def contar_segundos(dicc_bliteos, dicc_dibujos, tiempo_inicial: int, lista_atributos: list):
    # Cuenta cada 1 segundo y crea los textos en las cajas para mostrarlos en el juego
    #
    #    Argumento:
    #      dicc_bliteos [dict] -> Diccinario con todos los elementos a blitear
    #      dicc_dibujos [dict] -> Diccinario con todos los elementos a dibujar
    #      tiempo_inicial [int] -> Sengundo en el que comenzo el contador
    #    Retorna:
    #      retorna -> Cuadro de las dos cajas creadas
    lista_keys = ['posicion', 'caja', 'color_boton', 'border_radius']
    tiempo_transcurrido = pygame.time.get_ticks() // 1000 - tiempo_inicial
    contador_segundos = tiempo_transcurrido
    dicc_posiciones = lista_atributos[3]
    dicc_tabla = crear_texto_rect(dicc_bliteos, "tiempo"," Tiempo: " + str(contador_segundos) + "s", lista_atributos[0], lista_atributos[2])
    atributos_cuadro = crear_matriz_valores(dicc_posiciones[0][0], dicc_posiciones[0][1], dicc_posiciones[1][0], dicc_posiciones[1][1])

    val_texto = ["midleft", dicc_tabla['texto_rect'], lista_atributos[1], 8]
    atributos_texto = crear_diccionarios(lista_keys, val_texto)
    cuadro_tiempo = crear_rectangulo_objeto(dicc_dibujos, " Tiempo: ", atributos_cuadro, True, atributos_texto)
    actualizar_elemento(dicc_bliteos, "tiempo", dicc_tabla['texto'], dicc_tabla['texto_rect'])
    
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

def crear_botones_selec_gen(dicc_bliteos, dicc_dibujos, dicc_color_botones, elementos_texto: dict):
    # Crea los botonoes para selecicionar generacion
    #
    #    Argumento:
    #      dicc_color_botones [dict] -> colores de los botonoes por default
    #      elementos_texto [dict] -> elementos para crear los botones
    #    Retorna:
    #      dicc_botones -> Dict con los 3 botonoes creados
    keys_texto = ['fuente', 'color_texto', 'color_fondo', 'ancho', 'alto', 'caja']
    val_btn_1 = [elementos_texto['fuente_gen'], elementos_texto['color_texto'], dicc_color_botones['color_boton_gen_1'], elementos_texto['ancho_btn_gen'], elementos_texto['alto_btn_gen'], elementos_texto['caja']]
    val_btn_2 = [elementos_texto['fuente_gen'], elementos_texto['color_texto'], dicc_color_botones['color_boton_gen_2'], elementos_texto['ancho_btn_gen'], elementos_texto['alto_btn_gen'], elementos_texto['caja']]
    val_btn_3 = [elementos_texto['fuente_gen'], elementos_texto['color_texto'], dicc_color_botones['color_boton_gen_3'], elementos_texto['ancho_btn_gen'], elementos_texto['alto_btn_gen'], elementos_texto['caja']]

    atributos_boton_gen1 = crear_diccionarios(keys_texto, val_btn_1)
    atributos_boton_gen2 = crear_diccionarios(keys_texto, val_btn_2)
    atributos_boton_gen3 = crear_diccionarios(keys_texto, val_btn_3)

    lista_boton_gen_1 = crear_texto_en_caja(dicc_bliteos, "boton_gen_1", dicc_dibujos, "1", atributos_boton_gen1, "bottomleft", "center")
    lista_boton_gen_2 = crear_texto_en_caja(dicc_bliteos, "boton_gen_2", dicc_dibujos, "2", atributos_boton_gen2, "midbottom", "center")
    lista_boton_gen_3 = crear_texto_en_caja(dicc_bliteos, "boton_gen_3", dicc_dibujos, "3", atributos_boton_gen3, "bottomright", "center")

    lista_key_botones = ['boton_gen_1', 'boton_gen_2', 'boton_gen_3']
    lista_val_botones = [lista_boton_gen_1, lista_boton_gen_2, lista_boton_gen_3]
    dicc_botones = crear_diccionarios(lista_key_botones, lista_val_botones)

    return dicc_botones

def crear_botones_selec_dicicultad(dicc_bliteos, dicc_dibujos, dicc_color_botones, elementos_texto: dict):
    # Crea los botonoes para seleccionar la dificultad
    #
    #    Argumento:
    #      dicc_color_botones [dict] -> colores de los botonoes por default
    #      elementos_texto [dict] -> elementos para crear los botones
    #    Retorna:
    #      dicc_botones -> Dict con los 3 botonoes creados
    keys_texto = ['fuente', 'color_texto', 'color_fondo', 'ancho', 'alto', 'caja']

    val_btn_facil = [elementos_texto['fuente_gen'], elementos_texto['color_texto'], dicc_color_botones['color_facil'], elementos_texto['ancho_btn_dif'], elementos_texto['alto_btn_dif'], elementos_texto['caja']]
    val_btn_dificil = [elementos_texto['fuente_gen'], elementos_texto['color_texto'], dicc_color_botones['color_dificil'], elementos_texto['ancho_btn_dif'], elementos_texto['alto_btn_dif'], elementos_texto['caja']]
    atributos_boton_facil = crear_diccionarios(keys_texto, val_btn_facil)
    atributos_boton_dificil = crear_diccionarios(keys_texto, val_btn_dificil)

    lista_boton_facil = crear_texto_en_caja(dicc_bliteos, "facil", dicc_dibujos, "Facil", atributos_boton_facil, "center", "center")
    lista_boton_dificil= crear_texto_en_caja(dicc_bliteos, "dificil", dicc_dibujos, "Dificil", atributos_boton_dificil, "midbottom", "center")

    lista_key_botones = ['boton_facil', 'boton_dificil']
    lista_val_botones = [lista_boton_facil, lista_boton_dificil]
    dicc_botones = crear_diccionarios(lista_key_botones, lista_val_botones)

    return dicc_botones

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

#Funcion lambda incrementa racha acutual
incrementar_rachas = lambda contador: contador + 1

def coincidencia_pokemon(elem_coincidencia: dict, dicc_atributos_pokemon, val_tabla_tiempos, val_tabla_actual, dicc_bools: dict):
    # Parametros a modificar cuadno hay una coincidencia
    #
    #    Argumento:
    #      parametro [tipoDeDato] -> _description_
    #    Retorna:
    #      retorna -> _description_
    dicc_bools['contador'] = incrementar_rachas(dicc_bools['contador'])
    keys_texto = ['fuente', 'color_texto', 'color_fondo', 'ancho', 'alto', 'caja']
    elem_coincidencia['ventana'].blit(dicc_atributos_pokemon['pokemon_resuelto'], (elem_coincidencia['posicion_img_x'], elem_coincidencia['posicion_img_y']))
    dicc_bools['contando'] = False

    lista_tiempos = elem_coincidencia['elementos_tiempo']
    mejor_racha, racha = mejorar_racha("Packaje_PARCIAL2/mejor_racha.csv", dicc_bools['contador'])

    idiomas_pokemon(elem_coincidencia['ventana'], elem_coincidencia['bliteos'], elem_coincidencia['dibujos'], elem_coincidencia['elementos_idiomas'], dicc_atributos_pokemon)
    desblitear_idiomas(elem_coincidencia['bliteos'], elem_coincidencia['dibujos'])

    # Actualizar el texto del contador actual
    dicc_tabla_tiempos = crear_diccionarios(keys_texto, val_tabla_tiempos)
    dicc_tabla_actual = crear_diccionarios(keys_texto, val_tabla_actual)
    dicc_tiempo_actualizado = actualizar_tiempos(elem_coincidencia['bliteos'],elem_coincidencia['dibujos'], dicc_tabla_tiempos, lista_tiempos) 
    cuadro_racha_actual, cuadro_mejor_racha = actualizar_tabla(elem_coincidencia['bliteos'], elem_coincidencia['dibujos'], dicc_bools['contador'], racha, dicc_tabla_actual)

    pygame.display.update()
    pygame.time.wait(2000)

    dicc_bools['contando'] = True
    dicc_bools['tiempo_inicial'] = pygame.time.get_ticks() // 1000

    return dicc_bools

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
    lista_keys = ['posicion', 'caja', 'color_boton', 'border_radius']

    dicc_juego_terminado = crear_texto_rect(dicc_bliteos, "tiempos","Juego Terminado", fuente_resultado, color_letras)

    atributos_dimenciones = crear_matriz_valores(posicion_tiempos_x, posicion_tiempos_y, ancho_caja_tiempos, alto_caja_tiempos)
    val_texto = ["midtop", dicc_juego_terminado['texto_rect'], color_fondo_objetos, 8]
    atributos_texto = crear_diccionarios(lista_keys, val_texto)

    cuadro_tiempo = crear_rectangulo_objeto(dicc_dibujos, "cuadro_tiempo", atributos_dimenciones, True, atributos_texto)

    atrib_mejor_tiempo = crear_texto_rect(dicc_bliteos, "mejor_tiempo", " Mejor tiempo: " + str(mejor_tiempo) + "s", fuente_resultado, color_letras)
    dimen_mejor_tiempo = crear_matriz_valores(ancho_ventana / 2, 300, 0, 0)
    val_mejor_tiempo = ["midtop", atrib_mejor_tiempo['texto_rect'], color_fondo_objetos, 8]
    atributos_mejor_tiempo = crear_diccionarios(lista_keys, val_mejor_tiempo)
    cuadro_mejor_tiempo = crear_rectangulo_objeto(dicc_dibujos, "cuadro_mejor_tiempo", dimen_mejor_tiempo, True, atributos_mejor_tiempo)
    
    atrib_tiempo_ant = crear_texto_rect(dicc_bliteos, "tiempo_anterior", " Tiempo anterior: " + str(mejor_tiempo) + "s", fuente_resultado, color_letras)
    dimen_tiempo_anterior = crear_matriz_valores(ancho_ventana / 2, 400, 0, 0)
    val_tiempo_anterior = ["midtop", atrib_tiempo_ant['texto_rect'], color_fondo_objetos, 8]
    atributos_tiempo_ante = crear_diccionarios(lista_keys, val_tiempo_anterior)
    cuadro_tiempo_anterior = crear_rectangulo_objeto(dicc_dibujos, "cuadro_mejor_tiempo", dimen_tiempo_anterior, True, atributos_tiempo_ante)
    
    dicc_tiempo_prom = crear_texto_rect(dicc_bliteos, "tiempo_promedio", " Tiempo promedio: " + str(tiempo_promedio) + "s", fuente_resultado, color_letras)
    val_tiempo_prom = ["midtop", dicc_tiempo_prom['texto_rect'], color_fondo_objetos, 8]
    atrib_tiempo_prom = crear_diccionarios(lista_keys, val_tiempo_prom)
    dimen_tiempo_prom = crear_matriz_valores(ancho_ventana / 2, 500, 0, 0)
    cuadro_tiempo_promedio = crear_rectangulo_objeto(dicc_dibujos, "cuadro_tiempo_promedio", dimen_tiempo_prom, True, atrib_tiempo_prom)

    pygame.draw.rect(ventana, color_fondo_objetos, cuadro_tiempo, border_radius = 12)
    pygame.draw.rect(ventana, color_fondo_objetos, cuadro_mejor_tiempo, border_radius = 8)
    pygame.draw.rect(ventana, color_fondo_objetos, cuadro_tiempo_anterior, border_radius = 8)
    pygame.draw.rect(ventana, color_fondo_objetos, cuadro_tiempo_promedio, border_radius = 8)

    ventana.blit(dicc_juego_terminado['texto'], dicc_juego_terminado['texto_rect'])
    ventana.blit(atrib_mejor_tiempo['texto'], atrib_mejor_tiempo['texto_rect'])
    ventana.blit(atrib_tiempo_ant['texto'], atrib_tiempo_ant['texto_rect'])
    ventana.blit(dicc_tiempo_prom['texto'], dicc_tiempo_prom['texto_rect'])

def seleccionar_evento(dicc_color_botones, evento, lista_botones: list, dicc_bools: dict, dicc_elementos: dict, dicc_colores):
    # Segun que boton se haya apretado se modifican banderas y colores de botones
    #
    #    Argumento:
    #      parametro [tipoDeDato] -> _description_
    #    Retorna:
    #      retorna -> _description_
    # Boton dificultad facil por defecto activo
    btn_dificultad = lista_botones[0]
    btn_gen = lista_botones [1]

    eneables_generaciones = [dicc_elementos['eneables_generaciones']][0]

    if btn_dificultad['boton_facil'][1].collidepoint(evento.pos):
        dicc_bools['contador'] = 0
        dicc_color_botones['color_facil'] = dicc_colores['VERDE']
        dicc_color_botones['color_dificil'] = dicc_colores['ROJO']
        dicc_bools['bool_facil'] = True

    # Boton dificultad facil por defecto desactivado
    if btn_dificultad['boton_dificil'][1].collidepoint(evento.pos):
        dicc_bools['contador'] = 0
        dicc_color_botones['color_facil'] = dicc_colores['ROJO']
        dicc_color_botones['color_dificil'] = dicc_colores['VERDE']
        dicc_bools['bool_facil'] = False

    if btn_gen['boton_gen_1'][1].collidepoint(evento.pos) and eneables_generaciones[0]:
        dicc_color_botones['color_boton_gen_1'] = dicc_colores['ROJO']
        eneables_generaciones[0] = False
    elif btn_gen['boton_gen_1'][1].collidepoint(evento.pos) and eneables_generaciones[0] ==  False:
        dicc_color_botones['color_boton_gen_1'] = dicc_colores['VERDE']
        eneables_generaciones[0] = True

    # Boton selecionar generacion 2 por defecto desactivado
    if btn_gen['boton_gen_2'][1].collidepoint(evento.pos) and eneables_generaciones[1] == False:
        dicc_color_botones['color_boton_gen_2'] = dicc_colores['VERDE'] 
        eneables_generaciones[1] = True
    elif btn_gen['boton_gen_2'][1].collidepoint(evento.pos) and eneables_generaciones[1]:
        dicc_color_botones['color_boton_gen_2'] = dicc_colores['ROJO'] 
        eneables_generaciones[1] = False

    # Boton selecionar generacion 3 por defecto desactivado
    if btn_gen['boton_gen_3'][1].collidepoint(evento.pos) and eneables_generaciones[2] == False:
        dicc_color_botones['color_boton_gen_3'] = dicc_colores['VERDE']  
        eneables_generaciones[2] = True
    elif btn_gen['boton_gen_3'][1].collidepoint(evento.pos) and eneables_generaciones[2]:
        dicc_color_botones['color_boton_gen_3'] = dicc_colores['ROJO']  
        eneables_generaciones[2] = False 

    # Boton escribir nombre
    if lista_botones[2].collidepoint(evento.pos):    #verifico si presione el boton izq del mouse dentro del cuadro de texto. evento.pos devuelve las coordenadas del mouse
        dicc_color_botones['color_cuadro'] = dicc_colores['BLANCO']  
        dicc_bools['bool_contando'] = True
        dicc_bools['tiempo_inicial'] = pygame.time.get_ticks() // 1000
    else:
        dicc_color_botones['color_cuadro'] = dicc_colores['GRIS_CLARO'] 
        dicc_bools['bool_contando'] = False


    return dicc_color_botones, dicc_bools


def crear_diccionarios(list_claves: list, lista_valores: list):
    # Crea un diccionario con las claves y valores recibidos
    #
    #    Argumento:
    #      list_claves [list] -> String con las claves del dict
    #      lista_valores [list] -> Valores de cada clave
    #    Retorna:
    #      diccionario -> Dict creado
    diccionario = {}
    cant_elementos = len(list_claves)

    for i in range(cant_elementos):
        clave = list_claves[i]
        valor = lista_valores[i]
        diccionario[clave] = valor
    return diccionario

def mostrar_imagen_oculta(elementos: dict, dicc_bools: dict):
    # Parametros a modificar cuando se apreta el boton de "no lo se"
    #
    #    Argumento:
    #      elementos [dict] -> Varios elementos para funciones
    #      dicc_bools [dict] -> Dict con banderas y colores de botonoes
    #    Retorna:
    #      dicc_bools -> Dict con los valores modificados
    idiomas_pokemon(elementos['ventana'], elementos['dicc_bliteos'], elementos['dicc_dibujos'], elementos['caja_idiomas'], elementos['atrib_pokemon'])
    desblitear_idiomas(elementos['dicc_bliteos'], elementos['dicc_dibujos'])
    no_lo_conozco(elementos['ventana'], elementos['atrib_pokemon'], elementos['cuadro_imagen_x'], elementos['cuadro_imagen_y'], elementos['cuadro_de_texto'], elementos['fuente_cuadro_texto'], elementos['color_texto'])

    dicc_bools['contador'] = 0
    lista_racha_actual = crear_texto_en_caja(elementos['dicc_bliteos'], "actual", elementos['dicc_dibujos'], "Actual: " + str(dicc_bools['contador']), elementos['dicc_texto'], "center", "midleft")
    actualizar_elemento(elementos['dicc_bliteos'], "titulo_puntos", lista_racha_actual[0], lista_racha_actual[1])

    dicc_bools['tiempo_inicial'] = pygame.time.get_ticks() // 1000
    dicc_bools['bool_contando'] = True
    dicc_bools['lista_tiempos'] = []
    dicc_bools['repetidos'] = []

    return dicc_bools