
import pygame

def manejar_evento(evento, rect_texto):
    texto = ''
    if evento.type == pygame.MOUSEBUTTONDOWN and rect_texto.collidepoint(evento.pos):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                print(texto)
            elif evento.key == pygame.K_BACKSPACE:
                texto = texto[:-1]
            else:
                texto += evento.unicode
        return texto

def dibujar(pantalla, rect_texto, color_texto, texto):
    

    # Dibujar el texto
    rect_caja = (rect_texto.x + 5, rect_texto.y + 5)
    pantalla.blit(texto, rect_caja)
    # Dibujar el cuadro de texto
    pygame.draw.rect(texto, color_texto, rect_texto, 2)


