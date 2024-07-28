from funciones import *
import pygame
import sys

pygame.init()
#------------------------COLORES-------------------------
negro = (0,0,0)    
rojo = (255,0,0)
azul = (0,0,255)
verde = (0,255,0)
azul_claro = (0,150,255)
blanco = (255,255,255)
gris_claro = (200,200,200)
rojo_claro = (255, 128, 128)
verde_claro = (144, 238, 144)

fuente_resultados = pygame.font.SysFont("Consolas", 32)
fuente_cuadro_texto = pygame.font.SysFont("Arial", 20)
fuente_boton = pygame.font.SysFont("Consolas", 15)
fuente_gen = pygame.font.SysFont("Consolas", 25)
fuente_mejores_tiempo = pygame.font.SysFont("Consolas", 20)
fuente_idiomas = pygame.font.SysFont("Arial", 18)

lista_keys_colores = ['NEGRO', 'ROJO', 'VERDE', 'BLANCO', 'GRIS_CLARO']
lista_valores_colores = [negro, rojo, verde, blanco, gris_claro]
dicc_colores = crear_diccionarios(5, lista_keys_colores, lista_valores_colores)

color_fondo = (azul_claro)
color_cuadro_texto = gris_claro
color_boton = blanco
color_boton_gen_1 = verde
color_boton_gen_2 = rojo
color_boton_gen_3 = rojo
color_cuadro_imagen = azul_claro    
color_facil = verde
color_dificil = rojo

keys_color_botones = ['color_fondo', 'color_cuadro_texto', 'color_boton','color_boton_gen_1', 'color_boton_gen_2', 'color_boton_gen_3', 'color_cuadro_imagen', 'color_facil', 'color_dificil']
valores_color_botones = [color_fondo, color_cuadro_texto, color_boton,color_boton_gen_1, color_boton_gen_2, color_boton_gen_3, color_cuadro_imagen, color_facil, color_dificil]
dicc_color_botones = crear_diccionarios(9, keys_color_botones, valores_color_botones)
#------------------------VENTANA-------------------------
ancho_ventana = 1300
alto_ventana = 750
tamanio_ventana = (ancho_ventana, alto_ventana)

TAMAÑO_TEXTO = 32
FPS = 60

#------------------------Atributos imagen pokemon-------------------------
posicion_imagen_y = 450
posicion_imagen_x = ancho_ventana//2

ancho_cuadro_de_texto =  200
alto_cuadro_de_texto = 50
dimensiones_del_cuadro_de_texto = (ancho_cuadro_de_texto, alto_cuadro_de_texto)

distancia_borde_inferior = 70
posicion_cuadro_de_texto_x = (ancho_ventana - ancho_cuadro_de_texto)//2
posicion_cuadro_de_texto_y = (alto_ventana - alto_cuadro_de_texto - distancia_borde_inferior)

cuadro_texto = crear_matriz_valores(posicion_cuadro_de_texto_x, posicion_cuadro_de_texto_y, ancho_cuadro_de_texto, alto_cuadro_de_texto)

ancho_cuadro_imagen = 300
alto_cuadro_imagen = 400
dimenciones_imagen = [ancho_cuadro_imagen, alto_cuadro_imagen]
posicion_cuadro_imagen_x = (ancho_ventana - ancho_cuadro_imagen) // 2
posicion_cuadro_imagen_y = 180

#------------------------Atributos boton de generaciones-------------------------
ancho_boton = 180
alto_boton = 30

ancho_boton_generaciones = 67
alto_boton_generaciones = 67

posicion_botones_generaciones_x = 45
posicion_botones_generaciones_y = 140

ancho_caja_seleccion_gen = 220
alto_caja_seleccion_gen = 100

posicion_caja_selec_gen_x = 40
posicion_caja_selec_gen_y = 200

atributos_selec_gen = crear_matriz_valores(posicion_caja_selec_gen_x, posicion_caja_selec_gen_y, ancho_caja_seleccion_gen, alto_caja_seleccion_gen)
#------------------------Atributos tabla de rachas-------------------------
ancho_caja_puntaje = 220
alto_caja_puntaje = 160

posicion_caja_puntaje_x = ancho_ventana - ancho_caja_puntaje - 40
posicion_caja_puntaje_y = 100

atributos_caja_puntaje = crear_matriz_valores(posicion_caja_puntaje_x, posicion_caja_puntaje_y, ancho_caja_puntaje, alto_caja_puntaje)

ancho_caja_racha_actual = 180
alto_caja_racha_actual = 50

posicion_caja_racha_actual_x = ancho_ventana - (ancho_caja_racha_actual + 20)
posicion_caja_racha_actual_y = 40

posicion_caja_mejor_racha_x = ancho_ventana - (ancho_caja_racha_actual + 20)
posicion_caja_mejor_racha_y = 40 + alto_caja_racha_actual + 20

#------------------------Atributos cajas idiomas-------------------------
cantidad_idiomas = 3
ancho_caja_idiomas = 115
alto_caja_idiomas = 35

posicion_caja_idiomas_x = (ancho_ventana - (ancho_caja_idiomas * cantidad_idiomas)) /2
posicion_caja_idiomas_y = 700

atributos_caja_idiomas = crear_matriz_valores(posicion_caja_idiomas_x, posicion_caja_idiomas_y, ancho_caja_idiomas, alto_caja_idiomas)
elementos_caja_idiomas = [fuente_idiomas, negro, blanco, atributos_caja_idiomas]

posicion_boton_x = (ancho_ventana - ancho_boton) // 2



atributos_botones = crear_matriz_valores(posicion_boton_x, posicion_cuadro_de_texto_y - 40, ancho_boton, alto_boton)

lista_de_imagenes = []

#------------------------Atributos cajas dificultad-------------------------
ancho_caja_dificultad = 220
alto_caja_dificultad = 120

ancho_boton_dificultad = 200
alto_boton_dificultad = 30

posicion_dificultad_x = 40
posicion_dificultad_y = 350

atributos_dificultad = crear_matriz_valores(posicion_dificultad_x, posicion_dificultad_y, ancho_caja_dificultad, alto_caja_dificultad)
#------------------------Atributos cajas tiempo-------------------------
#---------Actual-------
ancho_caja_tiempos = 220
alto_caja_tiempos = 50

posicion_tiempos_x = ancho_ventana - (ancho_caja_tiempos + 40)
posicion_tiempos_y = 300

atributos_tiempos = crear_matriz_valores(posicion_tiempos_x, posicion_tiempos_y, ancho_caja_dificultad, alto_caja_dificultad)
#---------Tabla-------
ancho_tabla_tiempos = 220
alto_tabla_tiempos = 130

posicion_caja_tiempos_x = ancho_ventana - (ancho_tabla_tiempos + 40)
posicion_caja_tiempos_y = 380