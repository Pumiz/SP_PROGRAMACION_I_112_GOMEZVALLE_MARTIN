import pygame
import sys
import json
from valores import *
from funciones import *

pygame.init()

pokemones = []
lista_pokemones_jugados = []


with open("Packaje_PARCIAL2/Imagenes_pokemones.json", "r") as archivo:
    json_pokemones = json.load(archivo)
    pokemones = cargar_pokemones_en_lista(pokemones, json_pokemones)

#-------------------Ventana Principal-----------------
ventana = pygame.display.set_mode(TAMAÑO_VENTANA)
pygame.display.set_caption("¿Quien es ese Pokémon?") 

#------------------------Icono------------------------
icono = pygame.image.load("Packaje_PARCIAL2/pikachu.png")
pygame.display.set_icon(icono)

#------------------------Fuentes texto----------------------
fuente_resultados = pygame.font.SysFont("Consolas", 32)
fuente_cuadro_texto = pygame.font.SysFont("Arial", 20)
fuente_boton = pygame.font.SysFont("Consolas", 15)
fuente_gen = pygame.font.SysFont("Consolas", 25)
fuente_mejores_tiempo = pygame.font.SysFont("Consolas", 20)
fuente_idiomas = pygame.font.SysFont("Arial", 18)

#------------------------Foto Titulo------------------------
imagen_titulo = pygame.image.load("Packaje_PARCIAL2/Imagenes_pokemones/quien.png")
imagen_titulo = pygame.transform.scale(imagen_titulo, (400,180))
dicc_bliteos =  {
    'imagen_titulo': [imagen_titulo, ((ANCHO_VENTANA - 400) / 2, 20)]
}

#----------------Imagen de Fondo----------------------
fondo_ventana = pygame.image.load("Packaje_PARCIAL2/imagenes_fondo/fondo pokemon.jpg")
# imagen = pygame.transform.scale(imagen, (1000,800))

#------------------Caja de Texto----------------------
cuadro_de_texto = pygame.Rect(posicion_cuadro_de_texto_x, posicion_cuadro_de_texto_y, ancho_cuadro_de_texto, 
                alto_cuadro_de_texto)
dicc_dibujos =  {
    'cuadro_de_texto': [COLOR_CUADRO_TEXTO, cuadro_de_texto, 12]
}
texto_ingresado = ""

#------------------------Boton No lo conozco-------------------------
dicc_boton = crear_texto_rect(dicc_bliteos, "no_lo_se","No lo conozco", fuente_boton, NEGRO)

posicionar_cuadro_boton = crear_dicc_posicionar("center", dicc_boton['texto_rect'], COLOR_BOTON, 8)
cuadro_boton = crear_rectangulo_objeto(dicc_dibujos, "cuadro_boton", atributos_botones, True, posicionar_cuadro_boton)

#------------------------Botones seleccionar generacion-------------------------
dicc_rec_gen = crear_texto_rect(dicc_bliteos, "generaciones","Generaciones", fuente_gen, NEGRO)

posicionar_cuadro_select_gen = crear_dicc_posicionar("midtop", dicc_rec_gen['texto_rect'], BLANCO, 12)
cuadro_selec_gen = crear_rectangulo_objeto(dicc_dibujos, "cuadro_selec_gen", atributos_selec_gen, True, posicionar_cuadro_select_gen)

#------------------------Botones seleccionar dificultad-------------------------
dicc_rect_dificultad = crear_texto_rect(dicc_bliteos, "dificultad", "Dificultad", fuente_gen, NEGRO)

posicionar_cuadro_select_dificultad = crear_dicc_posicionar("midtop", dicc_rect_dificultad['texto_rect'], BLANCO, 8)
cuadro_selec_dificultad = crear_rectangulo_objeto(dicc_dibujos, "cuadro_selec_dificultad", atributos_dificultad, True, posicionar_cuadro_select_dificultad)

#----------------Tabla de puntos----------------------
contador = 0
incrementar_rachas = lambda contador: contador + 1
racha_csv, nueva_racha = mejorar_racha("Packaje_PARCIAL2/mejor_racha.csv", 0)

dicc_tabla_puntos = crear_texto_rect(dicc_bliteos, "racha","Racha", fuente_gen, NEGRO)

posicionar_cuadro_racha = crear_dicc_posicionar("midtop", dicc_tabla_puntos['texto_rect'], BLANCO, 12)
cuadro_racha = crear_rectangulo_objeto(dicc_dibujos, "cuadro_racha", atributos_caja_puntaje, True, posicionar_cuadro_racha)

dicc_texto = dicc_atributos_texto(fuente_gen, NEGRO, BLANCO, ancho_caja_racha_actual, alto_caja_racha_actual, cuadro_racha)
crear_texto_en_caja(dicc_bliteos, "actual", dicc_dibujos, "Actual: " + str(contador), dicc_texto, "center", "midleft")
crear_texto_en_caja(dicc_bliteos, "mejor", dicc_dibujos, "Mejor:  " + str(racha_csv), dicc_texto,"midbottom", "midleft")



#----------------Tabla de tiempos----------------------
dicc_titulo_tabla = crear_texto_rect(dicc_bliteos, "tiempo"," Tiempo: ", fuente_gen, NEGRO)

posicionar_cuadro_tiempo = crear_dicc_posicionar("midleft", dicc_titulo_tabla['texto_rect'], BLANCO, 12)
cuadro_tiempo = crear_rectangulo_objeto(dicc_dibujos, "cuadro_tiempo", atributos_tiempos, True, posicionar_cuadro_tiempo)


dicc_mejor_tiempo = crear_texto_rect(dicc_bliteos, "mejor_tiempo"," Mejor tiempo: ", fuente_mejores_tiempo, NEGRO)
posicionar_tabla_tiempo = crear_dicc_posicionar("topleft", dicc_mejor_tiempo['texto_rect'], BLANCO, 12)
tabla_tiempo = crear_rectangulo_objeto(dicc_dibujos, "tabla_tiempo", atributos_tiempos, True, posicionar_tabla_tiempo)

dicc_texto_tiempos = dicc_atributos_texto(fuente_mejores_tiempo, NEGRO, BLANCO, ancho_caja_racha_actual, alto_caja_racha_actual,tabla_tiempo)
crear_texto_en_caja(dicc_bliteos, "tiempo_anterior",dicc_dibujos," Tiempo anterior: ", dicc_texto_tiempos, "midleft", "midleft")
crear_texto_en_caja(dicc_bliteos, "tiempo_promedio",dicc_dibujos," Tiempo promedio: ", dicc_texto_tiempos, "bottomleft", "midleft")

eneable_gen_1 = True
eneable_gen_2 = False
eneable_gen_3 = False
eneables_generaciones = [eneable_gen_1, eneable_gen_2, eneable_gen_3]

clock = pygame.time.Clock()
contador_interaciones = 0

facil = True
contador_segundos = 0
contando = False
bandera_juego_terminado = False
tiempo_inicial = 0
lista_tiempos = []
dicc_atributos_pokemon = cargar_nuevo_pokemon(pokemones, lista_pokemones_jugados, eneables_generaciones, ancho_cuadro_imagen, alto_cuadro_imagen, facil)

flag = True
while flag == True:
    clock.tick(FPS)
    
    #Esto puede estar en una funcion que retorna una lista con cada una de las lista de los botones
    atributos_boton_gen1 = dicc_atributos_texto(fuente_gen, NEGRO, COLOR_BOTON_GEN_1, ancho_boton_generaciones, alto_boton_generaciones, cuadro_selec_gen)
    atributos_boton_gen2 = dicc_atributos_texto(fuente_gen, NEGRO, COLOR_BOTON_GEN_2, ancho_boton_generaciones, alto_boton_generaciones, cuadro_selec_gen)
    atributos_boton_gen3 = dicc_atributos_texto(fuente_gen, NEGRO, COLOR_BOTON_GEN_3, ancho_boton_generaciones, alto_boton_generaciones, cuadro_selec_gen)
    lista_boton_gen_1 = crear_texto_en_caja(dicc_bliteos, "boton_gen_1", dicc_dibujos, "1", atributos_boton_gen1, "bottomleft", "center")
    lista_boton_gen_2 = crear_texto_en_caja(dicc_bliteos, "boton_gen_2", dicc_dibujos, "2", atributos_boton_gen2, "midbottom", "center")
    lista_boton_gen_3 = crear_texto_en_caja(dicc_bliteos, "boton_gen_3", dicc_dibujos, "3", atributos_boton_gen3, "bottomright", "center")

    atributos_boton_facil = dicc_atributos_texto(fuente_gen, NEGRO, COLOR_FACIL, ancho_boton_dificultad, alto_boton_dificultad, cuadro_selec_dificultad)
    atributos_boton_dificil = dicc_atributos_texto(fuente_gen, NEGRO, COLOR_DIFICIL, ancho_boton_dificultad, alto_boton_dificultad, cuadro_selec_dificultad)
    lista_boton_facil = crear_texto_en_caja(dicc_bliteos, "facil",dicc_dibujos,"Facil", atributos_boton_facil, "center", "center")
    lista_boton_dificil = crear_texto_en_caja(dicc_bliteos, "dificil",dicc_dibujos,"Dificil", atributos_boton_dificil, "midbottom", "center")

    if contando:
        cuadro_tiempo, contador_segundos = contar_segundos(dicc_bliteos, dicc_dibujos,tiempo_inicial, fuente_gen, NEGRO, posicion_tiempos_x, posicion_tiempos_y, ancho_caja_tiempos, alto_caja_tiempos)

    lista_eventos = pygame.event.get()      
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:      
            flag = False

        elif evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_BACKSPACE:
                texto_ingresado = texto_ingresado[:-1]

            elif evento.key == pygame.K_RETURN:
            
                if texto_ingresado.lower() == dicc_atributos_pokemon['nombre_pokemon'].lower():
                    contador = incrementar_rachas(contador)
                    contando = False
                    lista_tiempos.append(contador_segundos)
                    mejor_racha, racha = mejorar_racha("Packaje_PARCIAL2/mejor_racha.csv", contador)

                    ventana.blit(dicc_atributos_pokemon['pokemon_resuelto'], (posicion_cuadro_imagen_x, posicion_cuadro_imagen_y))
                    
                    for i in range(len(lista_tiempos)):
                        tiempo_anterior = lista_tiempos[len(lista_tiempos) - 1]
                    # Actualizar el texto del contador actual
                    dicc_tabla_actual = dicc_atributos_texto(fuente_gen, NEGRO, BLANCO,ancho_caja_racha_actual, alto_caja_racha_actual, cuadro_racha)
                    cuadro_racha_actual, cuadro_mejor_racha = actualizar_tabla(dicc_bliteos, dicc_dibujos,contador, racha, dicc_tabla_actual)
                    # Actualizar el tiempos del contador
                    lista_elementos_tiempo = [lista_tiempos, tiempo_anterior, posicion_caja_tiempos_x, posicion_caja_tiempos_y]
                    dicc_tiempo_actualizado = actualizar_tiempos(dicc_bliteos, dicc_dibujos, dicc_tabla_actual, lista_elementos_tiempo)

                    idiomas_pokemon(ventana, dicc_bliteos, dicc_dibujos, fuente_idiomas, NEGRO, BLANCO, posicion_caja_idiomas_x, posicion_caja_idiomas_y, ancho_caja_idiomas, alto_caja_idiomas, dicc_atributos_pokemon['nombre_frances'], dicc_atributos_pokemon['nombre_italiano'], dicc_atributos_pokemon['nombre_aleman'])
                    desblitear_idiomas(dicc_bliteos, dicc_dibujos)
                    
                    pygame.display.update()
                    pygame.time.wait(2000)

                    dicc_atributos_pokemon = cargar_nuevo_pokemon(pokemones, lista_pokemones_jugados,eneable_gen_1, eneable_gen_2, eneable_gen_3, ancho_cuadro_imagen, alto_cuadro_imagen, facil)
                    texto_ingresado = ""
                    tiempo_inicial = pygame.time.get_ticks() // 1000
                    contando = True

                else:
                    texto_ingresado = ""
                    #COLOR_CUADRO_TEXTO = ROJO
                    pygame.display.update()
            else:
                texto_ingresado += evento.unicode

        elif evento.type == pygame.MOUSEBUTTONDOWN:

                    # Boton dificultad facil por defecto activo
                    if lista_boton_facil[1].collidepoint(evento.pos):
                        COLOR_FACIL = VERDE
                        COLOR_DIFICIL = ROJO
                        facil = True

                    # Boton dificultad facil por defecto desactivado
                    elif lista_boton_dificil[1].collidepoint(evento.pos):
                        COLOR_FACIL = ROJO
                        COLOR_DIFICIL = VERDE
                        facil = False

                    # Boton selecionar generacion 1 por defecto activo
                    if lista_boton_gen_1[1].collidepoint(evento.pos) and eneable_gen_1:
                        COLOR_BOTON_GEN_1 = ROJO
                        eneable_gen_1 = False
                    elif lista_boton_gen_1[1].collidepoint(evento.pos) and eneable_gen_1 ==  False:
                        COLOR_BOTON_GEN_1 = VERDE
                        eneable_gen_1 = True
                    
                    # Boton selecionar generacion 2 por defecto desactivado
                    if lista_boton_gen_2[1].collidepoint(evento.pos) and eneable_gen_2 == False:
                        COLOR_BOTON_GEN_2 = VERDE 
                        eneable_gen_2 = True
                    elif lista_boton_gen_2[1].collidepoint(evento.pos) and eneable_gen_2:
                        COLOR_BOTON_GEN_2 = ROJO 
                        eneable_gen_2 = False

                    # Boton selecionar generacion 3 por defecto desactivado
                    if lista_boton_gen_3[1].collidepoint(evento.pos) and eneable_gen_3 == False:
                        COLOR_BOTON_GEN_3 = VERDE 
                        eneable_gen_3 = True
                    elif lista_boton_gen_3[1].collidepoint(evento.pos) and eneable_gen_3:
                        COLOR_BOTON_GEN_3 = ROJO 
                        eneable_gen_3 = False 
                    
                    # Boton escribir nombre
                    if cuadro_de_texto.collidepoint(evento.pos):    #verifico si presione el boton izq del mouse dentro del cuadro de texto. evento.pos devuelve las coordenadas del mouse
                        COLOR_CUADRO_TEXTO = BLANCO
                        contando = True
                        tiempo_inicial = pygame.time.get_ticks() // 1000
                    else:
                        COLOR_CUADRO_TEXTO = GRIS_CLARO

                    
                    # Boton "Mostrar imagen oculta"
                    if cuadro_boton.collidepoint(evento.pos):
                        idiomas_pokemon(ventana, dicc_bliteos, dicc_dibujos,fuente_idiomas, NEGRO, BLANCO, posicion_caja_idiomas_x, posicion_caja_idiomas_y, ancho_caja_idiomas, alto_caja_idiomas, dicc_atributos_pokemon['nombre_frances'], dicc_atributos_pokemon['nombre_italiano'], dicc_atributos_pokemon['nombre_aleman'])
                        desblitear_idiomas(dicc_bliteos, dicc_dibujos)
                        no_lo_conozco(ventana, dicc_atributos_pokemon, posicion_cuadro_imagen_x, posicion_cuadro_imagen_y, cuadro_de_texto, fuente_cuadro_texto, NEGRO)
                        contador = 0
                        tiempo_inicial = pygame.time.get_ticks() // 1000
                        titulo_puntos, cuadro_racha_actual, rect_titulo_puntos = crear_texto_en_caja(dicc_bliteos, "actual", dicc_dibujos,"Actual: " + str(contador), dicc_texto, "center", "midleft")
                        actualizar_elemento(dicc_bliteos, "titulo_puntos", titulo_puntos, rect_titulo_puntos)

                        dicc_atributos_pokemon = cargar_nuevo_pokemon(pokemones, lista_pokemones_jugados, eneable_gen_1, eneable_gen_2, eneable_gen_3, ancho_cuadro_imagen, alto_cuadro_imagen, facil)

    if contador == 10:
        bandera_juego_terminado = True
        mostrar_cuadro_final_partida(ventana, dicc_bliteos, dicc_dibujos, ANCHO_VENTANA, ALTO_VENTANA, fuente_resultados, lista_tiempos)
        pygame.display.update()

    ventana.blit(fondo_ventana, (0, 0))
    fondo_ventana = pygame.transform.scale(fondo_ventana, TAMAÑO_VENTANA)
    
    texto = fuente_cuadro_texto.render(texto_ingresado, True, NEGRO)
    ventana.blit(dicc_atributos_pokemon['silueta_aleatoria'], (posicion_cuadro_imagen_x, posicion_cuadro_imagen_y))
    
    if bandera_juego_terminado == False: 
        dibujar_rectangulos(ventana, dicc_dibujos)
        blitear_objetos(ventana, dicc_bliteos, texto, cuadro_de_texto)
        pygame.display.update()

pygame.quit()
sys.exit()
