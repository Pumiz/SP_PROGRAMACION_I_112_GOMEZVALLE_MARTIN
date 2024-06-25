import json
from pathlib import Path

# Ruta base de la carpeta que contiene las subcarpetas por generación
ruta_base = Path('Packaje_PARCIAL2\Imagenes_pokemones')  # Reemplaza con la ruta adecuada

# Diccionario para almacenar los datos por generación
datos_por_generacion = {}

# Iterar sobre cada subcarpeta por generación (1gen, 2gen, 3gen)
for subcarpeta in ruta_base.iterdir():
    if subcarpeta.is_dir():  # Verificar que sea una carpeta
        generacion = subcarpeta.name
        datos_por_generacion[generacion] = {}

        # Iterar sobre cada archivo dentro de la subcarpeta actual
        for archivo in subcarpeta.iterdir():
            if archivo.is_file() and archivo.suffix == '.png':
                nombre_pokemon = archivo.stem  # Obtener el nombre del Pokémon
                if archivo.stem.endswith('_black'):  # Si es la silueta, obtiene el nombre del Pokemon sin "_black"
                    nombre_pokemon = archivo.stem.replace('_black', '')

                # Construir la ruta de la silueta
                ruta_silueta = subcarpeta / (nombre_pokemon + '_black.png')

                # Agregar al diccionario de datos por generación
                if nombre_pokemon not in datos_por_generacion[generacion]:
                    datos_por_generacion[generacion][nombre_pokemon] = {
                        'imagen_normal': '',
                        'silueta': ''
                    }

                # Asignar la ruta correspondiente según sea la imagen normal o la silueta
                if '_black' in archivo.stem:
                    datos_por_generacion[generacion][nombre_pokemon]['silueta'] = str(archivo)
                else:
                    datos_por_generacion[generacion][nombre_pokemon]['imagen_normal'] = str(archivo)

# Ruta y nombre del archivo JSON de salida
ruta_salida_json = Path('Packaje_PARCIAL2\Imagenes_pokemones.json')  # Reemplaza con la ruta y nombre deseado

# Escribir los datos en el archivo JSON
try:
    with open(ruta_salida_json, 'w') as archivo_json:
        json.dump(datos_por_generacion, archivo_json, indent=4)
    print(f"Se ha creado el archivo JSON en: {ruta_salida_json}")
except Exception as e:
    print(f"Error al escribir el archivo JSON: {e}")


"""
import pygame

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Traducción de Texto")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fuente
font = pygame.font.SysFont(None, 36)

# Texto original y traducciones predefinidas
original_text = "Hola, ¿cómo estás?"
translations = {
    "Chino": "你好，你好吗？",
    "Japonés": "こんにちは、お元気ですか？",
    "Alemán": "Hallo, wie geht's dir?",
    "Francés": "Bonjour, comment ça va?"
}

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dibujar en la pantalla
    screen.fill(WHITE)
    
    y_offset = 50
    original_render = font.render(f"Original: {original_text}", True, BLACK)
    screen.blit(original_render, (50, y_offset))
    y_offset += 60

    for lang, translation in translations.items():
        lang_text = font.render(f"{lang}: {translation}", True, BLACK)
        screen.blit(lang_text, (50, y_offset))
        y_offset += 60

    pygame.display.flip()

pygame.quit()
"""