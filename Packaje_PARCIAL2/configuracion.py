import json

# Definición de colores
colores = {
    "NEGRO": (0, 0, 0),
    "ROJO": (255, 0, 0),
    "AZUL": (0, 0, 255),
    "VERDE": (0, 255, 0),
    "AZUL_CLARO": (0, 150, 255),
    "BLANCO": (255, 255, 255),
    "GRIS_CLARO": (200, 200, 200),
    "ROJO_CLARO": (255, 128, 128),
    "VERDE_CLARO": (144, 238, 144)
}

# Definición de otras configuraciones
configuracion = {
    "ANCHO_VENTANA": 1000,
    "ALTO_VENTANA": 900,
    "FPS": 60,
    "TAMAÑO_TEXTO": 32,
    "COLOR_FONDO": colores["AZUL_CLARO"],
    "COLOR_CUADRO_TEXTO": colores["GRIS_CLARO"],
    "COLOR_BOTON": colores["BLANCO"],
    "COLOR_BOTON_GEN_1": colores["VERDE"],
    "COLOR_BOTON_GEN_2": colores["ROJO"],
    "COLOR_BOTON_GEN_3": colores["ROJO"],
    "COLOR_CUADRO_IMAGEN": colores["AZUL_CLARO"],
    "posicion_imagen_y": 450,
    "posicion_imagen_x": 1000 // 2,
    "dimensiones_del_cuadro_de_texto": (200, 50),
    "distancia_borde_inferior": 140,
    "posicion_cuadro_de_texto_x": (1000 - 200) // 2,
    "posicion_cuadro_de_texto_y": (900 - 50 - 140),
    "ancho_cuadro_imagen": 400,
    "alto_cuadro_imagen": 500,
    "posicion_cuadro_imagen_x": (1000 - 400) // 2,
    "posicion_cuadro_imagen_y": ((900 - 500) // 2) - 50,
    "ancho_boton": 180,
    "alto_boton": 30,
    "ancho_boton_generaciones": 67,
    "alto_boton_generaciones": 67,
    "posicion_botones_generaciones_x": 5,
    "posicion_botones_generaciones_y": 35,
    "ancho_caja_seleccion_gen": 220,
    "alto_caja_seleccion_gen": 110,
    "posicion_caja_selec_gen_x": 0,
    "posicion_caja_selec_gen_y": 0,
    "ancho_caja_puntaje": 220,
    "alto_caja_puntaje": 220,
    "posicion_caja_puntaje_x": 1000 - 220,
    "posicion_caja_puntaje_y": 0,
    "ancho_caja_racha_actual": 180,
    "alto_caja_racha_actual": 65,
    "posicion_caja_racha_actual_x": 1000 - (180 + 20),
    "posicion_caja_racha_actual_y": 40,
    "posicion_caja_mejor_racha_x": 1000 - (180 + 20),
    "posicion_caja_mejor_racha_y": 40 + 65 + 20,
    "posicion_boton_x": (1000 - 180) // 2,
    "lista_de_imagenes": []
}

# # Guardar como JSON
# with open('configuracion.json', 'w') as f:
#     json.dump(configuracion, f, indent=4)

# print("Archivo JSON creado correctamente.")

# Cargar el archivo JSON
with open(r"SP_PROGRAMACION_I_112_GRUPO_6_GOMEZVALLE_MARTIN_CRISTIAN_PENTITO\Packaje_PARCIAL2\configuracion.json", 'r') as f:
    configuracion = json.load(f)

# Acceder a la posición deseada
posicion_caja_racha_actual_x = configuracion["posicion_caja_racha_actual_x"]

print("Posición de la caja de la racha actual en X:", posicion_caja_racha_actual_x)
