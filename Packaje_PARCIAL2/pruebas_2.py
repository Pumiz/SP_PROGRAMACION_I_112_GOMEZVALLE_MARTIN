import pygame
import sys

def countdown_timer(duration):
    pygame.init()

    # Configuración de la pantalla
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Countdown Timer')

    # Configuración de fuentes y colores
    font = pygame.font.Font(None, 74)
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Definir el evento de temporizador
    TIMER_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(TIMER_EVENT, 1000)  # Evento cada 1000 ms (1 segundo)

    # Tiempo inicial
    remaining_time = duration

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == TIMER_EVENT:
                # Reducir el tiempo restante en 1 segundo
                remaining_time -= 1

        # Limpiar la pantalla
        screen.fill(black)

        # Renderizar el texto del contador en el costado derecho
        text = font.render(str(remaining_time), True, white)
        text_rect = text.get_rect(midright=(380, 150))  # Posición en el costado derecho
        screen.blit(text, text_rect)

        # Actualizar la pantalla
        pygame.display.flip()

        # Salir si el tiempo ha terminado
        if remaining_time <= 0:
            pygame.time.wait(2000)
            running = False

    pygame.quit()

# Llamada a la función con una duración de 10 segundos
countdown_timer(10)

