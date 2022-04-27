import pygame

class Tabuleiro():
    def __init__(self, grid):
        self.matriz = grid
        self.posicao_jogador = self.achar_posicao_jogador()

    def mover_jogador(self, direcao):
        if direcao == 'cima':
            try:
                 


    def achar_posicao_jogador(self):
        for y in range(len(self.matriz)):
            for x in range(len(self.matriz[y])):
                if self.matriz[y][x] == 4:
                    return [y,x]  


