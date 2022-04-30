import pygame
import sys
from tabuleiro import Tabuleiro

#definindo as dimensões da janela
LARGURA = 700
ALTURA = 700

'''0 = pedra
   1 = água
   2 = gelo
   3 = destino
   4 = jogador'''


#definindo as grids
grid1 = [
        [4, 2, 2, 0, 0], 
        [2, 2, 2, 2, 0], 
        [2, 2, 2, 2, 2], 
        [2, 2, 2, 2, 2], 
        [0, 0, 2, 3, 0]
        ] 
grid2 = [
        [0, 2, 2, 4, 0], 
        [2, 2, 2, 2, 0], 
        [3, 2, 2, 2, 2], 
        [2, 2, 2, 2, 2], 
        [0, 2, 2, 0, 0]
        ]
grid3 = [
        [4, 2, 2, 0, 0], 
        [2, 2, 2, 2, 0], 
        [2, 2, 2, 2, 2], 
        [2, 2, 2, 2, 2], 
        [0, 0, 2, 3, 0]
        ]
grid4 = [
        [4, 2, 2, 0, 0], 
        [2, 2, 2, 2, 0], 
        [2, 2, 2, 2, 2], 
        [2, 2, 2, 2, 2], 
        [0, 0, 2, 3, 0]
        ]
grid5 = [
        [4, 2, 2, 0, 0, 0], 
        [2, 2, 2, 2, 0, 0], 
        [2, 2, 2, 2, 2, 2], 
        [2, 2, 2, 2, 2, 2], 
        [0, 0, 2, 2, 0, 0],
        [0, 0, 2, 3, 0, 0]
        ]

#definindo a lista de grids
lista_grids = [grid1, grid2, grid3, grid4, grid5]

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
        self.tabuleiro1 = Tabuleiro(lista_grids.pop(0))

    def atualizar_tela(self):
        while not self.gameEnd:
            gameDisplay.fill(branco)
            self.mostrar_tabuleiro()
            self.mover_jogador()
            chegou = self.tabuleiro1.get_venceu()
            if chegou:
                try:
                    self.tabuleiro1 = Tabuleiro(lista_grids.pop(0))
                except:
                    print("Você chegou ao final!")
                    break
            pygame.display.update()
            clock.tick(60)
        
    def mostrar_tabuleiro(self):
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

                if self.tabuleiro1.matriz[y][x]==0:
                    pygame.draw.rect(gameDisplay, roxo, (posicao_x,posicao_y,100,100))
                elif self.tabuleiro1.matriz[y][x]==1:
                    pygame.draw.rect(gameDisplay, azul, (posicao_x,posicao_y,100,100))
                elif self.tabuleiro1.matriz[y][x]==2:
                    pygame.draw.rect(gameDisplay, azul_claro, (posicao_x,posicao_y,100,100))
                elif self.tabuleiro1.matriz[y][x]==3:
                    pygame.draw.rect(gameDisplay, verde, (posicao_x,posicao_y,100,100))
                elif self.tabuleiro1.matriz[y][x]==4:
                    pygame.draw.rect(gameDisplay, vermelho, (posicao_x,posicao_y,100,100))

    def mover_jogador(self, ):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #configurando os inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print("Movimento para ESQUERDA")
                    self.tabuleiro1.mover_jogador('esquerda')
                elif event.key == pygame.K_d:
                    self.tabuleiro1.mover_jogador('direita')
                    print("Movimento para DIREITA")
                elif event.key == pygame.K_w:
                    self.tabuleiro1.mover_jogador('cima')
                    print("Movimento para CIMA")
                elif event.key == pygame.K_s:
                    self.tabuleiro1.mover_jogador('baixo')
                    print("Movimento para BAIXO")


        

        