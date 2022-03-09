import pygame
import sys


class Player():
    def __init__(self, position):
        self.position = position

    def mover_jogador(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(CIMA)
                elif event.key == pygame.K_DOWN:
                    self.turn(BAIXO)
                elif event.key == pygame.K_LEFT:
                    self.turn(ESQUERDA)
                elif event.key == pygame.K_RIGHT:
                    self.turn(DIREITA)
    



#MOVIMENTOS
CIMA = (0, -1)
BAIXO = (0, 1)
ESQUERDA = (-1, 0)
DIREITA = (1, 0)
     
    
