import pygame
import sys


class Player():
    def __init__(self, position):
        self.position = position
        self.size = 1

    def turn(self, point):
        self.direção = point

    def mover_jogador(self):
        #definindo o que faz o jogo parar (o jogador perde)
        encurralado = False
        while not encurralado:
            #pygame.event.get() cria uma lista de eventos (qualquer clique ou movida de mouse por exemplo)
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    encurralado = True
                    print(event)
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
            pygame.display.update()
           
        



#MOVIMENTOS
CIMA = (0, -1)
BAIXO = (0, 1)
ESQUERDA = (-1, 0)
DIREITA = (1, 0)
     
    
