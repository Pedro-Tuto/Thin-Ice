class Tabuleiro():
    def __init__(self, grid):
        self.matriz = grid
        self.posicao_jogador = self.achar_posicao_jogador()
        self.venceu = False

    def get_venceu(self):
        return self.venceu

    def mover_jogador(self, direcao):
        y, x = self.posicao_jogador
        novo_y, novo_x = y, x
        if direcao == 'cima':
            novo_y = y-1
        elif direcao == 'direita':
            novo_x = x+1
        elif direcao == 'esquerda':
            novo_x = x-1
        elif direcao == 'baixo':
            novo_y = y+1

        if novo_x not in [-1, len(self.matriz[y])] and novo_y not in [-1, len(self.matriz)]: 
            if self.matriz[novo_y][novo_x] == 2:
                self.matriz[novo_y][novo_x] = 4
                self.matriz[y][x] = 1
                self.posicao_jogador = [novo_y, novo_x]
            elif self.matriz[novo_y][novo_x] == 3:
                self.venceu = True

    def achar_posicao_jogador(self):
        for y in range(len(self.matriz)):
            for x in range(len(self.matriz[y])):
                if self.matriz[y][x] == 4:
                    return [y,x]







