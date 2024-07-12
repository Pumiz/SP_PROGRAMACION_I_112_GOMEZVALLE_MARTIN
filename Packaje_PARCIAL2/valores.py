#------------------------COLORES-------------------------
NEGRO = (0,0,0)    
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)
BLANCO = (255,255,255)
GRIS_CLARO = (200,200,200)
ROJO_CLARO = (255, 128, 128)
VERDE_CLARO = (144, 238, 144)

COLOR_FONDO = (AZUL_CLARO)
COLOR_CUADRO_TEXTO = GRIS_CLARO
COLOR_BOTON = BLANCO
COLOR_BOTON_GEN_1 = VERDE
COLOR_BOTON_GEN_2 = ROJO
COLOR_BOTON_GEN_3 = ROJO
COLOR_CUADRO_IMAGEN = AZUL_CLARO    
COLOR_FACIL = VERDE
COLOR_DIFICIL = ROJO
#------------------------VENTANA-------------------------
ANCHO_VENTANA = 1300
ALTO_VENTANA = 750
TAMAÑO_VENTANA = (ANCHO_VENTANA, ALTO_VENTANA)

TAMAÑO_TEXTO = 32
FPS = 60

#------------------------Atributos imagen pokemon-------------------------
posicion_imagen_y = 450
posicion_imagen_x = ANCHO_VENTANA//2

ancho_cuadro_de_texto =  200
alto_cuadro_de_texto = 50
dimensiones_del_cuadro_de_texto = (ancho_cuadro_de_texto, alto_cuadro_de_texto)

distancia_borde_inferior = 70
posicion_cuadro_de_texto_x = (ANCHO_VENTANA - ancho_cuadro_de_texto)//2
posicion_cuadro_de_texto_y = (ALTO_VENTANA - alto_cuadro_de_texto - distancia_borde_inferior)

ancho_cuadro_imagen = 300
alto_cuadro_imagen = 400
posicion_cuadro_imagen_x = (ANCHO_VENTANA - ancho_cuadro_imagen) // 2
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

#------------------------Atributos tabla de rachas-------------------------
ancho_caja_puntaje = 220
alto_caja_puntaje = 160

posicion_caja_puntaje_x = ANCHO_VENTANA - ancho_caja_puntaje - 40
posicion_caja_puntaje_y = 100

ancho_caja_racha_actual = 180
alto_caja_racha_actual = 50

posicion_caja_racha_actual_x = ANCHO_VENTANA - (ancho_caja_racha_actual + 20)
posicion_caja_racha_actual_y = 40

posicion_caja_mejor_racha_x = ANCHO_VENTANA - (ancho_caja_racha_actual + 20)
posicion_caja_mejor_racha_y = 40 + alto_caja_racha_actual + 20

#------------------------Atributos cajas idiomas-------------------------
cantidad_idiomas = 3
ancho_caja_idiomas = 115
alto_caja_idiomas = 35

posicion_caja_idiomas_x = (ANCHO_VENTANA - (ancho_caja_idiomas * cantidad_idiomas)) /2
posicion_caja_idiomas_y = 700

posicion_boton_x = (ANCHO_VENTANA - ancho_boton) // 2

matriz_posiciones_boton = [
    [posicion_boton_x, posicion_cuadro_de_texto_y + 70],
    [ancho_boton, alto_boton]
]

lista_de_imagenes = []

#------------------------Atributos cajas dificultad-------------------------
ancho_caja_dificultad = 220
alto_caja_dificultad = 120

ancho_boton_dificultad = 200
alto_boton_dificultad = 30

posicion_dificultad_x = 40
posicion_dificultad_y = 350

#------------------------Atributos cajas tiempo-------------------------
#---------Actual-------
ancho_caja_tiempos = 220
alto_caja_tiempos = 50

posicion_tiempos_x = ANCHO_VENTANA - (ancho_caja_tiempos + 40)
posicion_tiempos_y = 300

#---------Tabla-------
ancho_tabla_tiempos = 220
alto_tabla_tiempos = 130

posicion_caja_tiempos_x = ANCHO_VENTANA - (ancho_tabla_tiempos + 40)
posicion_caja_tiempos_y = 380