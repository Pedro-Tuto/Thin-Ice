import pygame
import sys
from jogador import Controlador

#definindo as dimensões da janela
LARGURA = 700
ALTURA = 700

'''0 = pedra
   1 = água
   2 = gelo
   3 = destino
   4 = jogador'''

#definindo a grid 1
grid1 = [
        [2, 2, 2, 0, 0], 
        [2, 2, 2, 2, 0], 
        [2, 2, 2, 2, 2], 
        [0, 0, 2, 2, 0], 
        [0, 0, 2, 3, 0]
        ] 

#definindo as cores
preto = (0,0,0)
branco = (255,255,255)
vermelho = (200,0,0)
vermelho_claro = (255,0,0)
verde = (0,200,0)
verde_claro = (0,255,0)
azul = (0,0,255)
azul_claro = (0,100,200)
roxo = (221,160,221)

#iniciando o pygame e definindo o clock
pygame.init()
gameDisplay = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('GELO FINO')
clock = pygame.time.Clock()

'''#carregando as imagens
icon = pygame.image.load("")
pygame.display.set_icon(icon)
thrushimg = pygame.image.load("")
def bird(x,y):
    gameDisplay.blit(thrushimg,(x,y))'''

class Interface():
    def __init__(self):
        self.gameEnd = False
        self.controlador = Controlador(grid1)

    def atualizar_tela(self):
        while not self.gameEnd:
            gameDisplay.fill(branco)
            self.mostrar_tabuleiro(self.controlador.tabuleiro1)
            pygame.display.update()
            clock.tick(60)
        
    def mostrar_tabuleiro(self, tabuleiro):
        posicao_x = 0
        posicao_y = 0
        for y in range(5):
            if y == 0:
                posicao_y = 100
            elif y == 1:
                posicao_y = 200
            elif y == 2:
                posicao_y = 300
            elif y == 3:
                posicao_y = 400
            elif y == 4:
                posicao_y = 500

            for x in range(5):
                if x == 0:
                    posicao_x = 100
                elif x == 1:
                    posicao_x = 200
                elif x == 2:
                    posicao_x = 300
                elif x== 3:
                    posicao_x = 400
                elif x== 4:
                    posicao_x = 500

                if tabuleiro.matriz[y][x]==0:
                    pygame.draw.rect(gameDisplay, roxo, (posicao_x,posicao_y,100,100))
                elif tabuleiro.matriz[y][x]==1:
                    pygame.draw.rect(gameDisplay, azul, (posicao_x,posicao_y,100,100))
                elif tabuleiro.matriz[y][x]==2:
                    pygame.draw.rect(gameDisplay, azul_claro, (posicao_x,posicao_y,100,100))
                elif tabuleiro.matriz[y][x]==3:
                    pygame.draw.rect(gameDisplay, verde, (posicao_x,posicao_y,100,100))
                elif tabuleiro.matriz[y][x]==4:
                    pygame.draw.rect(gameDisplay, vermelho, (posicao_x,posicao_y,100,100))

    def mover_jogador(self, ):
        
        
        
        
        keys = pygame.key.get_pressed()
        x_move = 0
        y_move = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #configurando os inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_move = -100
                elif event.key == pygame.K_d:
                    x_move = 100
                elif event.key == pygame.K_w:
                    y_move = 100
                elif event.key == pygame.K_s:
                    y_move = -100
            #configurando o que acontece quando soltamos a tecla
            if event.type == pygame.KEYUP:   
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_move = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y_move = 0
            x += x_move
            y += y_move


        

        