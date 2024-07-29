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
ventana = pygame.display.set_mode(tamanio_ventana)
pygame.display.set_caption("¿Quien es ese Pokémon?") 

#------------------------Icono------------------------
icono = pygame.image.load("Packaje_PARCIAL2/Imagenes_pokemones/pikachu.png")
pygame.display.set_icon(icono)

#------------------------Foto Titulo------------------------
imagen_titulo = pygame.image.load("Packaje_PARCIAL2/Imagenes_pokemones/quien.png")
imagen_titulo = pygame.transform.scale(imagen_titulo, (400,180))
dicc_bliteos =  {
    'imagen_titulo': [imagen_titulo, ((ancho_ventana - 400) / 2, 20)]
}

#----------------Imagen de Fondo----------------------
fondo_ventana = pygame.image.load("Packaje_PARCIAL2/imagenes_fondo/fondo pokemon.jpg")
fondo_ventana = pygame.transform.scale(fondo_ventana, tamanio_ventana)

#------------------Caja de Texto----------------------
cuadro_de_texto = pygame.Rect(cuadro_texto[0][0], cuadro_texto[0][1], cuadro_texto[1][0], cuadro_texto[1][1])
dicc_dibujos =  {
    'cuadro_de_texto': [color_cuadro_texto, cuadro_de_texto, 12]
}
texto_ingresado = ""

#------------------------Boton No lo conozco-------------------------
dicc_boton = crear_texto_rect(dicc_bliteos, "no_lo_se","No lo conozco", fuente_idiomas, negro)

keys_posicionar = ['posicion', 'caja', 'color_boton', 'border_radius']
val_cuadro_boton = ["center", dicc_boton['texto_rect'], color_boton, 8]
posicionar_cuadro_boton = crear_diccionarios(keys_posicionar, val_cuadro_boton)
cuadro_boton = crear_rectangulo_objeto(dicc_dibujos, "cuadro_boton", atributos_botones, True, posicionar_cuadro_boton)

#------------------------Botones seleccionar generacion-------------------------
dicc_rec_gen = crear_texto_rect(dicc_bliteos, "generaciones","Generaciones", fuente_gen, negro)

val_cuadro_selec_gen = ["midtop", dicc_rec_gen['texto_rect'], blanco, 12]
posicionar_cuadro_select_gen = crear_diccionarios(keys_posicionar, val_cuadro_selec_gen)
cuadro_selec_gen = crear_rectangulo_objeto(dicc_dibujos, "cuadro_selec_gen", atributos_selec_gen, True, posicionar_cuadro_select_gen)

lista_key_btn_gen = ['fuente_gen', 'color_texto', 'ancho_btn_gen', 'alto_btn_gen', 'caja']
lista_val_btn_gen = [fuente_gen, negro, ancho_boton_generaciones, alto_boton_generaciones, cuadro_selec_gen]
dicc_elem_btn_gen = crear_diccionarios(lista_key_btn_gen, lista_val_btn_gen)

#------------------------Botones seleccionar dificultad-------------------------
dicc_rect_dificultad = crear_texto_rect(dicc_bliteos, "dificultad", "Dificultad", fuente_gen, negro)

val_btn_dif = ["midtop", dicc_rect_dificultad['texto_rect'], blanco, 8]
atrib_btn_dif = crear_diccionarios(keys_posicionar, val_btn_dif)
cuadro_selec_dif = crear_rectangulo_objeto(dicc_dibujos, "cuadro_selec_dif", atributos_dificultad, True, atrib_btn_dif)

lista_key_btn_dif = ['fuente_gen', 'color_texto', 'ancho_btn_dif', 'alto_btn_dif', 'caja']
lista_val_btn_dif = [fuente_gen, negro, ancho_boton_dificultad, alto_boton_dificultad, cuadro_selec_dif]
dicc_elem_btn_dificultad = crear_diccionarios(lista_key_btn_dif, lista_val_btn_dif)

#----------------Tabla de puntos----------------------
contador = 0
racha_csv, nueva_racha = mejorar_racha("Packaje_PARCIAL2/mejor_racha.csv", 0)

dicc_tabla_puntos = crear_texto_rect(dicc_bliteos, "racha","Racha", fuente_gen, negro)

val_cuadro_racha = ["midtop", dicc_tabla_puntos['texto_rect'], blanco, 12]
posicionar_cuadro_racha = crear_diccionarios(keys_posicionar, val_cuadro_racha)
cuadro_racha = crear_rectangulo_objeto(dicc_dibujos, "cuadro_racha", atributos_caja_puntaje, True, posicionar_cuadro_racha)
val_tabla_tiempos.append(cuadro_racha)
val_tabla_actual.append(cuadro_racha)

keys_texto = ['fuente', 'color_texto', 'color_fondo', 'ancho', 'alto', 'caja']
val_texto = [fuente_gen, negro, blanco, ancho_caja_racha_actual, alto_caja_racha_actual, cuadro_racha]
dicc_texto = crear_diccionarios(keys_texto, val_texto)
crear_texto_en_caja(dicc_bliteos, "actual", dicc_dibujos, "Actual: " + str(contador), dicc_texto, "center", "midleft")
crear_texto_en_caja(dicc_bliteos, "mejor", dicc_dibujos, "Mejor:  " + str(racha_csv), dicc_texto,"midbottom", "midleft")

#----------------Tabla de tiempos----------------------
dicc_titulo_tabla = crear_texto_rect(dicc_bliteos, "tiempo"," Tiempo: ", fuente_gen, negro)

val_cuadro_tiempo = ["midleft", dicc_titulo_tabla['texto_rect'], blanco, 12]
posicionar_cuadro_tiempo = crear_diccionarios(keys_posicionar, val_cuadro_tiempo)
cuadro_tiempo = crear_rectangulo_objeto(dicc_dibujos, "cuadro_tiempo", atributos_tiempos, True, posicionar_cuadro_tiempo)

clock = pygame.time.Clock()
contador_interaciones = 0

eneable_gen_1 = True
eneable_gen_2 = False
eneable_gen_3 = False
eneables_generaciones = [eneable_gen_1, eneable_gen_2, eneable_gen_3]

facil = True
contador_segundos = 0
contando = False
bandera_juego_terminado = False
tiempo_inicial = 0
lista_tiempos = []

keys_banderas = ['contador', 'bool_contando', 'tiempo_inicial', 'bool_gen', 'bool_facil', 'repetidos', 'lista_tiempos']
valo_banderas = [contador, contando, tiempo_inicial, eneables_generaciones, facil, lista_pokemones_jugados, lista_tiempos]
dicc_bools = crear_diccionarios(keys_banderas, valo_banderas)

dicc_atributos_pokemon = cargar_nuevo_pokemon(pokemones, dicc_bools, dimenciones_imagen)

flag = True
while flag == True:
    clock.tick(FPS)
    boton_gen = crear_botones_selec_gen(dicc_bliteos, dicc_dibujos, dicc_color_botones, dicc_elem_btn_gen)
    btn_dificultad = crear_botones_selec_dicicultad(dicc_bliteos, dicc_dibujos, dicc_color_botones, dicc_elem_btn_dificultad)

    if dicc_bools['bool_contando']:
        atributos_caja_tiempo = [fuente_gen, blanco, negro, atributos_tiempos]
        cuadro_tiempo, contador_segundos = contar_segundos(dicc_bliteos, dicc_dibujos, dicc_bools['tiempo_inicial'], atributos_caja_tiempo)

    lista_eventos = pygame.event.get()      
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:      
            flag = False

        elif evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_BACKSPACE:
                texto_ingresado = texto_ingresado[:-1]

            elif evento.key == pygame.K_RETURN:
            
                if texto_ingresado.lower() == dicc_atributos_pokemon['nombre_pokemon'].lower():
                    
                    dicc_bools['lista_tiempos'].append(contador_segundos)
                    tiempo_anterior = get_tiempo_anterior(dicc_bools['lista_tiempos'])
                    
                    elementos_tiempo = [dicc_bools['lista_tiempos'], tiempo_anterior, posicion_caja_tiempos_x, posicion_caja_tiempos_y]
                    keys_coincidencia = ['ventana', 'bliteos', 'dibujos', 'posicion_img_x', 'posicion_img_y', 'elementos_tiempo', 'elementos_idiomas']
                    val_coincidencia = [ventana, dicc_bliteos, dicc_dibujos, posicion_cuadro_imagen_x, posicion_cuadro_imagen_y, elementos_tiempo, elementos_caja_idiomas]
                    elementos_coincidencia = crear_diccionarios(keys_coincidencia, val_coincidencia)
                    dicc_bools = coincidencia_pokemon(elementos_coincidencia, dicc_atributos_pokemon, val_tabla_tiempos, val_tabla_actual, dicc_bools)

                    dicc_atributos_pokemon = cargar_nuevo_pokemon(pokemones, dicc_bools, dimenciones_imagen)
                    texto_ingresado = ""

                else:
                    texto_ingresado = ""
                    pygame.display.update()
            else:
                texto_ingresado += evento.unicode

        elif evento.type == pygame.MOUSEBUTTONDOWN:

            lista_botones = [btn_dificultad, boton_gen, cuadro_de_texto]
            lista_keys = ['color_facil', 'color_dificil', 'color_boton_1', 'color_boton_2', 'color_boton_3', 'color_cuadro_texto', 'eneables_generaciones']
            lista_valores = [color_facil, color_dificil, color_boton_gen_1, color_boton_gen_2, color_boton_gen_3, dicc_color_botones['color_cuadro_texto'], eneables_generaciones]
            dicc_elementos = crear_diccionarios(lista_keys, lista_valores)
            dicc_color_botones, dicc_bools = seleccionar_evento(dicc_color_botones, evento, lista_botones, dicc_bools, dicc_elementos, dicc_colores)
            
            # Boton "Mostrar imagen oculta"
            if cuadro_boton.collidepoint(evento.pos):
                elementos_keys = ['ventana', 'dicc_bliteos', 'dicc_dibujos', 'caja_idiomas', 'atrib_pokemon', 'cuadro_imagen_x', 'cuadro_imagen_y', 
                                'cuadro_de_texto', 'fuente_cuadro_texto', 'color_texto', 'dicc_texto']
                elementos_valores = [ventana, dicc_bliteos, dicc_dibujos, elementos_caja_idiomas, dicc_atributos_pokemon, posicion_cuadro_imagen_x, 
                                    posicion_cuadro_imagen_y, cuadro_de_texto, fuente_cuadro_texto, negro, dicc_texto]
                elementos_no_lo_se = crear_diccionarios(elementos_keys, elementos_valores)
                dicc_bools = mostrar_imagen_oculta(elementos_no_lo_se, dicc_bools)

                dicc_atributos_pokemon = cargar_nuevo_pokemon(pokemones, dicc_bools, dimenciones_imagen)

    if dicc_bools['contador'] == 10:
        bandera_juego_terminado = True
        mostrar_cuadro_final_partida(ventana, dicc_bliteos, dicc_dibujos, ancho_ventana, alto_ventana, fuente_resultados, dicc_bools['lista_tiempos'])
        pygame.display.update()

    ventana.blit(fondo_ventana, (0, 0))
    ventana.blit(dicc_atributos_pokemon['silueta_aleatoria'], (posicion_cuadro_imagen_x, posicion_cuadro_imagen_y))
    
    texto = fuente_cuadro_texto.render(texto_ingresado, True, negro)
    
    if bandera_juego_terminado == False: 
        dibujar_rectangulos(ventana, dicc_dibujos)
        blitear_objetos(ventana, dicc_bliteos, texto, cuadro_de_texto)
        pygame.display.update()

pygame.quit()
sys.exit()