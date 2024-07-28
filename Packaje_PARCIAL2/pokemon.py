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
# imagen = pygame.transform.scale(imagen, (1000,800))

#------------------Caja de Texto----------------------
cuadro_de_texto = pygame.Rect(cuadro_texto[0][0], cuadro_texto[0][1], cuadro_texto[1][0], cuadro_texto[1][1])
dicc_dibujos =  {
    'cuadro_de_texto': [color_cuadro_texto, cuadro_de_texto, 12]
}
texto_ingresado = ""

#------------------------Boton No lo conozco-------------------------
dicc_boton = crear_texto_rect(dicc_bliteos, "no_lo_se","No lo conozco", fuente_boton, negro)

posicionar_cuadro_boton = crear_dicc_posicionar("center", dicc_boton['texto_rect'], color_boton, 8)
cuadro_boton = crear_rectangulo_objeto(dicc_dibujos, "cuadro_boton", atributos_botones, True, posicionar_cuadro_boton)

#------------------------Botones seleccionar generacion-------------------------
dicc_rec_gen = crear_texto_rect(dicc_bliteos, "generaciones","Generaciones", fuente_gen, negro)

posicionar_cuadro_select_gen = crear_dicc_posicionar("midtop", dicc_rec_gen['texto_rect'], blanco, 12)
cuadro_selec_gen = crear_rectangulo_objeto(dicc_dibujos, "cuadro_selec_gen", atributos_selec_gen, True, posicionar_cuadro_select_gen)

lista_key_btn_gen = ['fuente_gen', 'color_texto', 'ancho_btn_gen', 'alto_btn_gen', 'caja']
lista_val_btn_gen = [fuente_gen, negro, ancho_boton_generaciones, alto_boton_generaciones, cuadro_selec_gen]
dicc_elem_btn_gen = crear_diccionarios(5, lista_key_btn_gen, lista_val_btn_gen)

#------------------------Botones seleccionar dificultad-------------------------
dicc_rect_dificultad = crear_texto_rect(dicc_bliteos, "dificultad", "Dificultad", fuente_gen, negro)

atrib_btn_dif = crear_dicc_posicionar("midtop", dicc_rect_dificultad['texto_rect'], blanco, 8)
cuadro_selec_dif = crear_rectangulo_objeto(dicc_dibujos, "cuadro_selec_dif", atributos_dificultad, True, atrib_btn_dif)

lista_key_btn_dif = ['fuente_gen', 'color_texto', 'ancho_btn_dif', 'alto_btn_dif', 'caja']
lista_val_btn_dif = [fuente_gen, negro, ancho_boton_dificultad, alto_boton_dificultad, cuadro_selec_dif]
dicc_elem_btn_dificultad = crear_diccionarios(5, lista_key_btn_dif, lista_val_btn_dif)

#----------------Tabla de puntos----------------------
contador = 0
incrementar_rachas = lambda contador: contador + 1
racha_csv, nueva_racha = mejorar_racha("Packaje_PARCIAL2/mejor_racha.csv", 0)

dicc_tabla_puntos = crear_texto_rect(dicc_bliteos, "racha","Racha", fuente_gen, negro)

posicionar_cuadro_racha = crear_dicc_posicionar("midtop", dicc_tabla_puntos['texto_rect'], blanco, 12)
cuadro_racha = crear_rectangulo_objeto(dicc_dibujos, "cuadro_racha", atributos_caja_puntaje, True, posicionar_cuadro_racha)

dicc_texto = dicc_atributos_texto(fuente_gen, negro, blanco, ancho_caja_racha_actual, alto_caja_racha_actual, cuadro_racha)
crear_texto_en_caja(dicc_bliteos, "actual", dicc_dibujos, "Actual: " + str(contador), dicc_texto, "center", "midleft")
crear_texto_en_caja(dicc_bliteos, "mejor", dicc_dibujos, "Mejor:  " + str(racha_csv), dicc_texto,"midbottom", "midleft")



#----------------Tabla de tiempos----------------------
dicc_titulo_tabla = crear_texto_rect(dicc_bliteos, "tiempo"," Tiempo: ", fuente_gen, negro)

posicionar_cuadro_tiempo = crear_dicc_posicionar("midleft", dicc_titulo_tabla['texto_rect'], blanco, 12)
cuadro_tiempo = crear_rectangulo_objeto(dicc_dibujos, "cuadro_tiempo", atributos_tiempos, True, posicionar_cuadro_tiempo)


dicc_mejor_tiempo = crear_texto_rect(dicc_bliteos, "mejor_tiempo"," Mejor tiempo: ", fuente_mejores_tiempo, negro)
posicionar_tabla_tiempo = crear_dicc_posicionar("topleft", dicc_mejor_tiempo['texto_rect'], blanco, 12)
tabla_tiempo = crear_rectangulo_objeto(dicc_dibujos, "tabla_tiempo", atributos_tiempos, True, posicionar_tabla_tiempo)

dicc_texto_tiempos = dicc_atributos_texto(fuente_mejores_tiempo, negro, blanco, ancho_caja_racha_actual, alto_caja_racha_actual,tabla_tiempo)
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
dicc_atributos_pokemon = cargar_nuevo_pokemon(pokemones, lista_pokemones_jugados, eneables_generaciones, dimenciones_imagen, facil)

flag = True
while flag == True:
    clock.tick(FPS)
    boton_gen = crear_botones_selec_gen(dicc_bliteos, dicc_dibujos, dicc_color_botones, dicc_elem_btn_gen)
    btn_dificultad = crear_botones_selec_dicicultad(dicc_bliteos, dicc_dibujos, dicc_color_botones, dicc_elem_btn_dificultad)


    if contando:
        atributos_caja_tiempo = [fuente_gen, blanco, negro, atributos_tiempos]
        cuadro_tiempo, contador_segundos = contar_segundos(dicc_bliteos, dicc_dibujos, tiempo_inicial, atributos_caja_tiempo)

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
                    tiempo_anterior = get_tiempo_anterior(lista_tiempos)

                    elementos_tiempo = [lista_tiempos, tiempo_anterior, posicion_caja_tiempos_x, posicion_caja_tiempos_y]
                    keys_coincidencia = ['ventana', 'bliteos', 'dibujos', 'posicion_img_x', 'posicion_img_y', 'elementos_tiempo', 'elementos_idiomas']
                    val_coincidencia = [ventana, dicc_bliteos, dicc_dibujos, posicion_cuadro_imagen_x, posicion_cuadro_imagen_y, elementos_tiempo, elementos_caja_idiomas]
                    elem_coinci = crear_diccionarios(7, keys_coincidencia, val_coincidencia)

                    # Actualizar el texto del contador actual
                    dicc_tabla_actual = dicc_atributos_texto(fuente_gen, negro, blanco,ancho_caja_racha_actual, alto_caja_racha_actual, cuadro_racha)
                    cuadro_racha_actual, cuadro_mejor_racha = actualizar_tabla(dicc_bliteos, dicc_dibujos,contador, racha, dicc_tabla_actual)
                    coincidencia_pokemon(elem_coinci, dicc_atributos_pokemon, dicc_tabla_actual)
                    pygame.display.update()
                    pygame.time.wait(2000)

                    dicc_atributos_pokemon = cargar_nuevo_pokemon(pokemones, lista_pokemones_jugados, eneables_generaciones, dimenciones_imagen, facil)
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

            lista_botones = [btn_dificultad['boton_facil'][1], btn_dificultad['boton_dificil'][1], 
                            boton_gen['boton_gen_1'][1], boton_gen['boton_gen_2'][1], boton_gen['boton_gen_3'][1], cuadro_de_texto]
            lista_keys = ['bool_facil', 'color_facil', 'color_dificil', 'color_boton_1', 'color_boton_2', 'color_boton_3', 'color_cuadro_texto', 'eneables_generaciones']
            lista_valores = [facil, color_facil, color_dificil, color_boton_gen_1, color_boton_gen_2, color_boton_gen_3, dicc_color_botones['color_cuadro_texto'], eneables_generaciones]
            dicc_elementos = crear_diccionarios(8, lista_keys, lista_valores)
            dicc_color_botones, dicc_nuevos_estados = seleccionar_evento(dicc_color_botones, evento, lista_botones, contador, dicc_elementos, dicc_colores)

            facil = dicc_nuevos_estados['facil']
            eneables_generaciones = dicc_nuevos_estados['eneables_generaciones']
            eneable_gen_1 = eneables_generaciones[0]
            eneable_gen_2 = eneables_generaciones[1]
            eneable_gen_3 = eneables_generaciones[2]
            
            # Boton "Mostrar imagen oculta"
            if cuadro_boton.collidepoint(evento.pos):
                
                elementos_keys = ['ventana', 'dicc_bliteos', 'dicc_dibujos', 'caja_idiomas', 'atrib_pokemon', 'cuadro_imagen_x', 'cuadro_imagen_y', 
                                'cuadro_de_texto', 'fuente_cuadro_texto', 'color_texto', 'dicc_texto']
                elementos_valores = [ventana, dicc_bliteos, dicc_dibujos, elementos_caja_idiomas, dicc_atributos_pokemon, posicion_cuadro_imagen_x, 
                                    posicion_cuadro_imagen_y, cuadro_de_texto, fuente_cuadro_texto, negro, dicc_texto]
                elementos_no_lo_se = crear_diccionarios(11, elementos_keys, elementos_valores)
                dicc_img_oculta = mostrar_imagen_oculta(elementos_no_lo_se)

                contador = dicc_img_oculta['contador']
                tiempo_inicial = pygame.time.get_ticks() // 1000

                list_eneables = [eneable_gen_1, eneable_gen_2, eneable_gen_3]
                dicc_atributos_pokemon = cargar_nuevo_pokemon(pokemones, lista_pokemones_jugados, list_eneables, dimenciones_imagen, facil)

    if contador == 10:
        bandera_juego_terminado = True
        mostrar_cuadro_final_partida(ventana, dicc_bliteos, dicc_dibujos, ancho_ventana, alto_ventana, fuente_resultados, lista_tiempos)
        pygame.display.update()

    ventana.blit(fondo_ventana, (0, 0))
    fondo_ventana = pygame.transform.scale(fondo_ventana, tamanio_ventana)
    
    texto = fuente_cuadro_texto.render(texto_ingresado, True, negro)
    ventana.blit(dicc_atributos_pokemon['silueta_aleatoria'], (posicion_cuadro_imagen_x, posicion_cuadro_imagen_y))
    
    if bandera_juego_terminado == False: 
        dibujar_rectangulos(ventana, dicc_dibujos)
        blitear_objetos(ventana, dicc_bliteos, texto, cuadro_de_texto)
        pygame.display.update()

pygame.quit()
sys.exit()
