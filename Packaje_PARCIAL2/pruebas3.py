import pygame
import csv
import os

# Configuración inicial de Pygame
pygame.init()
screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Juego de Frutas')

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fuente
font = pygame.font.Font(None, 36)

# Lista de frutas
frutas = ['manzana', 'banana', 'naranja', 'pera', 'uva', 'sandía']

# Función para mostrar texto en la pantalla
def mostrar_texto(texto, x, y, color=WHITE):
    texto_surface = font.render(texto, True, color)
    screen.blit(texto_surface, (x, y))

# Función para mostrar un botón
def mostrar_boton(texto, x, y, w, h, color_normal, color_hover, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, color_hover, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, color_normal, (x, y, w, h))

    mostrar_texto(texto, x + 10, y + 10)

# Función principal del juego
def juego_frutas():
    puntaje = 0
    intentos = 5

    while intentos > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                guardar_puntaje_csv(puntaje)  # Guardar puntaje antes de salir
                pygame.quit()
                quit()

        # Mostrar ventana con contador regresivo y botón "Empezar"
        screen.fill(BLACK)
        mostrar_texto(f'Tiempo restante: {intentos}', 50, 50)

        def iniciar_juego():
            nonlocal intentos
            intentos = 0

        mostrar_boton('Empezar', 250, 150, 100, 50, WHITE, (200, 200, 200), iniciar_juego)

        pygame.display.flip()

        # Contador regresivo
        pygame.time.wait(1000)  # Esperar un segundo
        intentos -= 1

    # Ventana para ingresar frutas
    ingresar_frutas(puntaje)

# Función para ingresar y validar el nombre de la fruta
def ingresar_frutas(puntaje):
    screen.fill(BLACK)
    mostrar_texto('Escribe el nombre de una fruta:', 50, 50)

    input_activo = True
    nombre_ingresado = ''
    tiempo_limite = 10 * 1000  # 10 segundos en milisegundos
    tiempo_inicio = pygame.time.get_ticks()

    while input_activo:
        tiempo_actual = pygame.time.get_ticks() - tiempo_inicio
        tiempo_restante = max(tiempo_limite - tiempo_actual, 0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                guardar_puntaje_csv(puntaje)  # Guardar puntaje antes de salir
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_activo = False  # Terminar la entrada al presionar Enter
                elif event.key == pygame.K_BACKSPACE:
                    nombre_ingresado = nombre_ingresado[:-1]
                else:
                    nombre_ingresado += event.unicode

        # Mostrar el tiempo restante y el nombre ingresado
        screen.fill(BLACK)
        mostrar_texto(f'Tiempo restante: {tiempo_restante // 1000}', 50, 50)
        mostrar_texto(f'Fruta: {nombre_ingresado}', 50, 100)

        pygame.display.flip()

        # Verificar si se superó el tiempo límite
        if tiempo_actual >= tiempo_limite:
            input_activo = False

    # Validar el nombre de la fruta ingresado
    if nombre_ingresado.lower() in frutas:
        puntaje += 10
        mostrar_ventana_puntaje(puntaje)
    else:
        mostrar_texto('Incorrecto o tiempo agotado.', 50, 150)
        pygame.display.flip()
        pygame.time.wait(2000)  # Esperar 2 segundos antes de continuar
        juego_frutas()  # Reiniciar el juego

# Función para mostrar la ventana de puntaje
def mostrar_ventana_puntaje(puntaje):
    screen.fill(BLACK)
    mostrar_texto(f'Puntaje: {puntaje}', 50, 50)

    guardar_puntaje_csv(puntaje)  # Guardar puntaje actualizado

    pygame.display.flip()

    # Esperar a que el usuario cierre la ventana
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

# Función para guardar el puntaje en un archivo CSV
def guardar_puntaje_csv(puntaje):
    csv_filename = 'puntajes.csv'

    # Crear o actualizar el archivo CSV
    if not os.path.exists(csv_filename):
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Puntaje'])

    # Leer el puntaje almacenado (si existe)
    puntaje_guardado = 0
    try:
        with open(csv_filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Saltar la cabecera
            for row in reader:
                puntaje_guardado = int(row[0])
    except FileNotFoundError:
        puntaje_guardado = 0

    # Actualizar el puntaje si es mayor al puntaje guardado anteriormente
    if puntaje > puntaje_guardado:
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Puntaje'])
            writer.writerow([puntaje])
    else:
        with open(csv_filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([puntaje])

# Función principal del programa
def main():
    juego_frutas()

if __name__ == '__main__':
    main()
