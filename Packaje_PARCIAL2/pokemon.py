import pygame
import sys
import json
from valores import *
from funciones import *
import time
pygame.init()

pokemones = []

with open("Packaje_PARCIAL2\Imagenes_pokemones.json", "r") as archivo:
#with open("Packaje_PARCIAL2\\Imagenes_pokemones.json", "r") as archivo:
    json_pokemones = json.load(archivo)
    pokemones = cargar_pokemones_en_lista(pokemones, json_pokemones)

#crear_rectangulo(posicion_caja_selec_gen_x)

#-------------------Ventana Principal-----------------
ventana = pygame.display.set_mode(TAMAÑO_VENTANA)
pygame.display.set_caption("¿Quien es ese Pokémon?") 

#------------------------Icono------------------------
icono = pygame.image.load("Packaje_PARCIAL2\pikachu.png")
pygame.display.set_icon(icono)

#------------------------Fuentes texto----------------------
fuente = pygame.font.SysFont("Consolas", 40)
fuente_cuadro_texto = pygame.font.SysFont("Arial", 20)
fuente_boton = pygame.font.SysFont("Consolas", 15)
fuente_gen = pygame.font.SysFont("Consolas", 25)
fuente_mejores_tiempo = pygame.font.SysFont("Consolas", 20)
fuente_idiomas = pygame.font.SysFont("Arial", 18)


#------------------------Foto Titulo------------------------
imagen_titulo = pygame.image.load("Packaje_PARCIAL2\Imagenes_pokemones\quien.png")
imagen_titulo = pygame.transform.scale(imagen_titulo, (400,180))
#titulo = fuente.render("¿Quién es ese Pokémon?", True, NEGRO)
#titulo_rect = titulo.get_rect()
#imagen_titulo.center = (ANCHO_VENTANA // 2, 60)


#----------------Imagen de Fondo----------------------
fondo_ventana = pygame.image.load(r"Packaje_PARCIAL2\imagenes_fondo\fondo pokemon.jpg")
# imagen = pygame.transform.scale(imagen, (1000,800))

#----------------Rectangulo de Imagen-------------------

cuadro_de_imagen = crear_rectangulo_objeto(posicion_cuadro_imagen_x, posicion_cuadro_imagen_y, ancho_cuadro_imagen, alto_cuadro_imagen, False, None, None)

#------------------Caja de Texto----------------------
cuadro_de_texto = pygame.Rect(posicion_cuadro_de_texto_x, posicion_cuadro_de_texto_y, ancho_cuadro_de_texto, 
                alto_cuadro_de_texto)
texto_ingresado = ""

#------------------------Boton No lo conozco-------------------------
texto_no_lo_se, boton_rect = crear_texto_rect("No lo conozco", fuente_boton, NEGRO)
cuadro_boton = crear_rectangulo_objeto(posicion_boton_x, posicion_cuadro_de_texto_y - 40, ancho_boton, alto_boton, True, "center", boton_rect)


#------------------------Botones seleccionar generacion-------------------------
texto_gen, texto_rect_gen = crear_texto_rect("Generaciones", fuente_gen, NEGRO)
cuadro_selec_gen = crear_rectangulo_objeto(posicion_caja_selec_gen_x, posicion_caja_selec_gen_y, ancho_caja_seleccion_gen, alto_caja_seleccion_gen, True, "midtop", texto_rect_gen)

texto_boton_gen_1, boton_gen_1, texto_rect_gen_1 = crear_texto_en_caja("1", fuente_gen, NEGRO, ancho_boton_generaciones, alto_boton_generaciones,cuadro_selec_gen, "bottomleft", "center")
texto_boton_gen_2, boton_gen_2, texto_rect_gen_2 = crear_texto_en_caja("2", fuente_gen, NEGRO, ancho_boton_generaciones, alto_boton_generaciones,cuadro_selec_gen, "midbottom", "center")
texto_boton_gen_3, boton_gen_3, texto_rect_gen_3 = crear_texto_en_caja("3", fuente_gen, NEGRO, ancho_boton_generaciones, alto_boton_generaciones,cuadro_selec_gen, "bottomright", "center")

#------------------------Botones seleccionar dificultad-------------------------
texto_dificultad, texto_rect_dificultad = crear_texto_rect("Dificultad", fuente_gen, NEGRO)
cuadro_selec_dificultad = crear_rectangulo_objeto(posicion_dificultad_x, posicion_dificultad_y, ancho_caja_dificultad, alto_caja_dificultad, True, "midtop", texto_rect_dificultad)

texto_facil, boton_facil, texto_rect_facil = crear_texto_en_caja("Facil", fuente_gen, NEGRO, ancho_boton_dificultad, alto_boton_dificultad, cuadro_selec_dificultad, "center", "center")
texto_dificil, boton_dificil, texto_rect_dificil = crear_texto_en_caja("Dificil", fuente_gen, NEGRO, ancho_boton_dificultad, alto_boton_dificultad, cuadro_selec_dificultad, "midbottom", "center")


#----------------Tabla de puntos----------------------
contador = 0
incrementar_rachas = lambda contador: contador + 1
racha_csv, nueva_racha = mejorar_racha("Packaje_PARCIAL2\mejor_racha.csv", 0)

titulo_tabla_puntos, rect_titulo_tabla_puntos = crear_texto_rect("Racha", fuente_gen, NEGRO)
cuadro_racha = crear_rectangulo_objeto(posicion_caja_puntaje_x, posicion_caja_puntaje_y, ancho_caja_puntaje, alto_caja_puntaje, True, "midtop", rect_titulo_tabla_puntos)

titulo_puntos, cuadro_racha_actual, rect_titulo_puntos = crear_texto_en_caja("Actual: " + str(contador), fuente_gen, NEGRO, ancho_caja_racha_actual, alto_caja_racha_actual,cuadro_racha, "center", "midleft")
titulo_mejor_racha, cuadro_mejor_racha, rect_titulo_mejor_racha = crear_texto_en_caja("Mejor:  " + str(racha_csv), fuente_gen, NEGRO, ancho_caja_racha_actual, alto_caja_racha_actual,cuadro_racha, "midbottom", "midleft")


#----------------Tabla de tiempos----------------------
titulo_tabla_tiempo, rect_titulo_tabla_timepo = crear_texto_rect(" Tiempo: ", fuente_gen, NEGRO)
cuadro_tiempo = crear_rectangulo_objeto(posicion_tiempos_x, posicion_tiempos_y, ancho_caja_tiempos, alto_caja_tiempos, True, "midleft", rect_titulo_tabla_timepo)


titulo_tabla_mejor_tiempo, rect_titulo_tabla_mejor_tiempo = crear_texto_rect(" Mejor tiempo: ", fuente_mejores_tiempo, NEGRO)
tabla_tiempo = crear_rectangulo_objeto(posicion_caja_tiempos_x, posicion_caja_tiempos_y, ancho_tabla_tiempos, alto_tabla_tiempos, True, "topleft", rect_titulo_tabla_mejor_tiempo)

titulo_tiempo_anterior, cuadro_tiempo_anterior, rect_tiempo_anterior = crear_texto_en_caja(" Tiempo anterior: ", fuente_mejores_tiempo, NEGRO, ancho_caja_racha_actual, alto_caja_racha_actual,tabla_tiempo, "midleft", "midleft")
titulo_tiempo_promedio, cuadro_tiempo_promedio, rect_titulo_tiempo_promedio = crear_texto_en_caja(" Promedio tiempo: ", fuente_mejores_tiempo, NEGRO, ancho_caja_racha_actual, alto_caja_racha_actual,tabla_tiempo, "bottomleft", "midleft")


#----------------Carga de Pokemones----------------
path = "Packaje_PARCIAL2\Imagenes_pokemones.json"
with open(path, "r") as archivo:
    json_pokemones = json.load(archivo)

pokemones = []
pokemones = cargar_pokemones_en_lista(pokemones, json_pokemones)

eneable_gen_1 = True
eneable_gen_2 = False
eneable_gen_3 = False






clock = pygame.time.Clock()
contador_interaciones = 0

atributos_pokemon = cargar_nuevo_pokemon(pokemones, eneable_gen_1, eneable_gen_2, eneable_gen_3, ancho_cuadro_imagen, alto_cuadro_imagen)

desblitear_pantalla = True

def juego_terminado():
    #----------------Tabla de tiempos----------------------
    ancho_caja_tiempos = 400
    alto_caja_tiempos = 400
    posicion_tiempos_x = (ANCHO_VENTANA - ancho_caja_tiempos) / 2
    posicion_tiempos_y = ((ALTO_VENTANA - alto_caja_tiempos) / 2) + 30

    

    titulo_tabla_tiempo, rect_tabla_final = crear_texto_rect(" Tiempos: ", fuente_gen, NEGRO)
    cuadro_tiempo = crear_rectangulo_objeto(posicion_tiempos_x, posicion_tiempos_y, ancho_caja_tiempos, alto_caja_tiempos, True, "midtop", rect_tabla_final)
    
    texto_jugar_de_nuevo, boton_rect_jugar = crear_texto_rect("Jugar de Nuevo", fuente_boton, NEGRO)
    cuadro_jugar = crear_rectangulo_objeto(posicion_boton_x, posicion_cuadro_de_texto_y, ancho_boton, alto_boton, True, "center", boton_rect_jugar)



    ventana.blit(imagen_titulo, ((ANCHO_VENTANA - 400) / 2, 20)) #imagen titulo
    ventana.blit(titulo_tabla_tiempo, rect_tabla_final)
    ventana.blit(texto_jugar_de_nuevo, boton_rect_jugar)
    #ventana.blit(titulo_tabla_mejor_tiempo, rect_titulo_tabla_mejor_tiempo)

    
    pygame.draw.rect(ventana, BLANCO, cuadro_tiempo, border_radius = 12)
    pygame.draw.rect(ventana, BLANCO, cuadro_jugar, border_radius = 8)

    pygame.display.update()

    return cuadro_jugar


flag = True
while flag == True:
    clock.tick(FPS)
    coincidencia = False
    matriz_bliteos = [
        [imagen_titulo, ((ANCHO_VENTANA - 400) / 2, 20)],
        [texto_no_lo_se, boton_rect],
        [texto_gen, texto_rect_gen],
        [texto_boton_gen_1, texto_rect_gen_1],
        [texto_boton_gen_2, texto_rect_gen_2],
        [texto_boton_gen_3, texto_rect_gen_3],
        [texto_dificultad, texto_rect_dificultad],
        [texto_facil, texto_rect_facil],
        [texto_dificil, texto_rect_dificil],
        [titulo_tabla_puntos, rect_titulo_tabla_puntos],
        [titulo_puntos, rect_titulo_puntos],
        [titulo_mejor_racha, rect_titulo_mejor_racha],
        [titulo_tabla_tiempo, rect_titulo_tabla_timepo],
        [titulo_tabla_mejor_tiempo, rect_titulo_tabla_mejor_tiempo],
        [titulo_tiempo_anterior, rect_tiempo_anterior],
        [titulo_tiempo_promedio, rect_titulo_tiempo_promedio],
    ]

    if contador >= 2:
        desblitear_pantalla = False
        cuadro_jugar = juego_terminado()

    lista_eventos = pygame.event.get()      
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:      
            flag = False

        elif evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_BACKSPACE:
                texto_ingresado = texto_ingresado[:-1]

            elif evento.key == pygame.K_RETURN:
            
                if texto_ingresado.lower() == atributos_pokemon[0].lower():
                    contador = incrementar_rachas(contador)
                    print("coincidencia")
                    print(contador)
                    mejor_racha, racha = mejorar_racha("Packaje_PARCIAL2\mejor_racha.csv", contador)
                    # Actualizar el texto del contador actual
                    titulo_puntos, cuadro_racha_actual, rect_titulo_puntos = crear_texto_en_caja("Actual: " + str(contador), fuente_gen, NEGRO, ancho_caja_racha_actual, alto_caja_racha_actual, cuadro_racha, "center", "midleft")
                    titulo_mejor_racha, cuadro_mejor_racha, rect_titulo_mejor_racha = crear_texto_en_caja("Mejor:  " + str(racha), fuente_gen, NEGRO, ancho_caja_racha_actual, alto_caja_racha_actual,cuadro_racha, "midbottom", "midleft")
                    
                    #COLOR_CUADRO_TEXTO = VERDE
                    coincidencia = True
                    ventana.blit(atributos_pokemon[2], (posicion_cuadro_imagen_x, posicion_cuadro_imagen_y))
                    idiomas_pokemon(ventana, fuente_idiomas, NEGRO, BLANCO, posicion_caja_idiomas_x, posicion_caja_idiomas_y, ancho_caja_idiomas, alto_caja_idiomas, atributos_pokemon[4], atributos_pokemon[5], atributos_pokemon[6])
                    pygame.display.update()
                    pygame.time.wait(2000)
                    atributos_pokemon = cargar_nuevo_pokemon(pokemones, eneable_gen_1, eneable_gen_2, eneable_gen_3, ancho_cuadro_imagen, alto_cuadro_imagen)
                    texto_ingresado = ""


                else:
                    print("No coincide")
                    texto_ingresado = ""
                    #COLOR_CUADRO_TEXTO = ROJO
                    pygame.display.update()
            else:
                texto_ingresado += evento.unicode


        elif evento.type == pygame.MOUSEBUTTONDOWN:

                if evento.button == 1:  # Boton izq 
                    if desblitear_pantalla == False:
                        if cuadro_jugar.collidepoint(evento.pos):
                            desblitear_pantalla = True
                            contador = 0
                    # Boton dificultad facil por defecto activo
                    if boton_facil.collidepoint(evento.pos):
                        COLOR_FACIL = VERDE
                        COLOR_DIFICIL = ROJO
                        facil = True

                    # Boton dificultad facil por defecto desactivado
                    elif boton_dificil.collidepoint(evento.pos):
                        COLOR_FACIL = ROJO
                        COLOR_DIFICIL = VERDE
                        facil = False

                    # Boton selecionar generacion 1 por defecto activo
                    if boton_gen_1.collidepoint(evento.pos) and eneable_gen_1:
                        COLOR_BOTON_GEN_1 = ROJO
                        eneable_gen_1 = False
                    elif boton_gen_1.collidepoint(evento.pos) and eneable_gen_1 ==  False:
                        COLOR_BOTON_GEN_1 = VERDE
                        eneable_gen_1 = True
                    
                    # Boton selecionar generacion 2 por defecto desactivado
                    if boton_gen_2.collidepoint(evento.pos) and eneable_gen_2 == False:
                        COLOR_BOTON_GEN_2 = VERDE 
                        eneable_gen_2 = True
                    elif boton_gen_2.collidepoint(evento.pos) and eneable_gen_2:
                        COLOR_BOTON_GEN_2 = ROJO 
                        eneable_gen_2 = False

                    # Boton selecionar generacion 3 por defecto desactivado
                    if boton_gen_3.collidepoint(evento.pos) and eneable_gen_3 == False:
                        COLOR_BOTON_GEN_3 = VERDE 
                        eneable_gen_3 = True
                    elif boton_gen_3.collidepoint(evento.pos) and eneable_gen_3:
                        COLOR_BOTON_GEN_3 = ROJO 
                        eneable_gen_3 = False 
                    
                    # Boton escribir nombre
                    if cuadro_de_texto.collidepoint(evento.pos):    #verifico si presione el boton izq del mouse dentro del cuadro de texto. evento.pos devuelve las coordenadas del mouse
                        COLOR_CUADRO_TEXTO = BLANCO
                    else:
                        COLOR_CUADRO_TEXTO = GRIS_CLARO


                    # Boton "Mostrar imagen oculta"
                    if cuadro_boton.collidepoint(evento.pos):
                        print("no lo se")
                        contador = 0
                        COLOR_BOTON = BLANCO
                        ventana.blit(atributos_pokemon[2], (posicion_cuadro_imagen_x, posicion_cuadro_imagen_y))
                        idiomas_pokemon(ventana, fuente_idiomas, NEGRO, BLANCO, posicion_caja_idiomas_x, posicion_caja_idiomas_y, ancho_caja_idiomas, alto_caja_idiomas, atributos_pokemon[4], atributos_pokemon[5], atributos_pokemon[6])
                        titulo_puntos, cuadro_racha_actual, rect_titulo_puntos = crear_texto_en_caja("Actual: " + str(contador), fuente_gen, NEGRO, ancho_caja_racha_actual, alto_caja_racha_actual, cuadro_racha, "center", "midleft")
                        
                        #Muestra el nombre del pokemon desconocido
                        texto = fuente_cuadro_texto.render(atributos_pokemon[0], True, NEGRO)
                        texto_rect = texto.get_rect()
                        texto_rect.center = cuadro_de_texto.center
                        ventana.blit(texto, texto_rect)  # texto del cuadro de texto

                        pygame.display.update()
                        pygame.time.wait(2000)

                        atributos_pokemon = cargar_nuevo_pokemon(pokemones, eneable_gen_1, eneable_gen_2, eneable_gen_3, ancho_cuadro_imagen, alto_cuadro_imagen)
                    






    
    #ventana.fill(COLOR_FONDO)
    ventana.blit(fondo_ventana, (0, 0))
    fondo_ventana = pygame.transform.scale(fondo_ventana, TAMAÑO_VENTANA)

    matriz_draws = [
        [COLOR_CUADRO_TEXTO, cuadro_de_texto, 12],
        [BLANCO, cuadro_racha, 12],
        [BLANCO, cuadro_racha_actual, 8],
        [BLANCO, cuadro_mejor_racha, 8],
        [COLOR_CUADRO_IMAGEN, cuadro_de_imagen, 8],
        [COLOR_BOTON, cuadro_boton, 8],
        [BLANCO, cuadro_selec_gen, 8],
        [COLOR_BOTON_GEN_1, boton_gen_1, 8],
        [COLOR_BOTON_GEN_2, boton_gen_2, 8],
        [COLOR_BOTON_GEN_3, boton_gen_3, 8],
        [BLANCO, cuadro_selec_dificultad, 8],
        [COLOR_FACIL, boton_facil, 8],
        [COLOR_DIFICIL, boton_dificil, 8],
        [BLANCO, cuadro_tiempo, 12],
        [BLANCO, tabla_tiempo, 12],
        [BLANCO, cuadro_tiempo_anterior, 8],
        [BLANCO, cuadro_tiempo_promedio, 8],
    ]

    if desblitear_pantalla:
        dibujar_rectangulos(ventana, matriz_draws)

        texto = fuente_cuadro_texto.render(texto_ingresado, True, NEGRO)
        ventana.blit(atributos_pokemon[1], (posicion_cuadro_imagen_x, posicion_cuadro_imagen_y))

        blitear_objetos(ventana, matriz_bliteos, texto, cuadro_de_texto)


        pygame.display.update()

pygame.quit()
sys.exit()
