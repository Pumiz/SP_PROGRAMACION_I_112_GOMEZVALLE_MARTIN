import pygame
"""
# Inicializar Pygame
pygame.init()

# Colores
COLOR_INACTIVO = pygame.Color('lightskyblue3')
COLOR_ACTIVO = pygame.Color('dodgerblue2')
COLOR_TEXTO = pygame.Color('black')
COLOR_FONDO = pygame.Color('white')

# Tamaño de la pantalla
ANCHO = 800
ALTO = 600
TAMANIO_TEXTO = 32

# Crear la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Cuadro de Texto Pygame")

# Fuente
fuente = pygame.font.Font(None, TAMANIO_TEXTO)

class CuadroDeTexto:
    def __init__(self, x, y, w, h, texto=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVO
        self.texto = texto
        self.txt_surface = fuente.render(texto, True, COLOR_TEXTO)
        self.activo = False

    def manejar_evento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            # Si el usuario hace clic en el cuadro de texto
            if self.rect.collidepoint(evento.pos):
                self.activo = not self.activo
            else:
                self.activo = False
            self.color = COLOR_ACTIVO if self.activo else COLOR_INACTIVO
        if evento.type == pygame.KEYDOWN:
            if self.activo:
                if evento.key == pygame.K_RETURN:
                    print(self.texto)
                    self.texto = ''
                elif evento.key == pygame.K_BACKSPACE:
                    self.texto = self.texto[:-1]
                else:
                    self.texto += evento.unicode
                self.txt_surface = fuente.render(self.texto, True, COLOR_TEXTO)

    def actualizar(self):
        # Aumentar el tamaño del cuadro de texto si es necesario
        ancho = max(200, self.txt_surface.get_width()+10)
        self.rect.w = ancho

    def dibujar(self, pantalla):
        # Dibujar el texto
        pantalla.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Dibujar el cuadro de texto
        pygame.draw.rect(pantalla, self.color, self.rect, 2)

def main():
    clock = pygame.time.Clock()
    cuadro_de_texto = CuadroDeTexto(100, 100, 140, TAMANIO_TEXTO+10)
    hecho = False

    while not hecho:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                hecho = True
            cuadro_de_texto.manejar_evento(evento)

        cuadro_de_texto.actualizar()

        pantalla.fill(COLOR_FONDO)
        cuadro_de_texto.dibujar(pantalla)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()

"""

#sin POO

import pygame

# Inicializar Pygame
pygame.init()

# Colores
COLOR_INACTIVO = pygame.Color('lightskyblue3')
COLOR_ACTIVO = pygame.Color('dodgerblue2')
COLOR_TEXTO = pygame.Color('black')
COLOR_FONDO = pygame.Color('white')

# Tamaño de la pantalla
ANCHO = 800
ALTO = 600
TAMANIO_TEXTO = 32

# Crear la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Cuadro de Texto Pygame")

# Fuente
fuente = pygame.font.Font(None, TAMANIO_TEXTO)

# Variables del cuadro de texto
rect_texto = pygame.Rect(100, 100, 140, TAMANIO_TEXTO + 10)
color_texto = COLOR_INACTIVO
texto = ''
txt_surface = fuente.render(texto, True, COLOR_TEXTO)
activo = False

def manejar_evento(evento):
    global activo, texto, txt_surface, color_texto
    if evento.type == pygame.MOUSEBUTTONDOWN:
        # Si el usuario hace clic en el cuadro de texto
        if rect_texto.collidepoint(evento.pos):
            activo = not activo
        else:
            activo = False
        color_texto = COLOR_ACTIVO if activo else COLOR_INACTIVO
    if evento.type == pygame.KEYDOWN:
        if activo:
            if evento.key == pygame.K_RETURN:
                print(texto)
                texto = ''
            elif evento.key == pygame.K_BACKSPACE:
                texto = texto[:-1]
            else:
                texto += evento.unicode
            txt_surface = fuente.render(texto, True, COLOR_TEXTO)

def actualizar():
    global rect_texto
    # Aumentar el tamaño del cuadro de texto si es necesario
    ancho = max(200, txt_surface.get_width() + 10)
    rect_texto.w = ancho

def dibujar(pantalla):
    pantalla.fill(COLOR_FONDO)
    # Dibujar el texto
    pantalla.blit(txt_surface, (rect_texto.x + 5, rect_texto.y + 5))
    # Dibujar el cuadro de texto
    pygame.draw.rect(pantalla, color_texto, rect_texto, 2)

def main():
    clock = pygame.time.Clock()
    hecho = False

    while not hecho:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                hecho = True
            manejar_evento(evento)

        actualizar()

        dibujar(pantalla)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
