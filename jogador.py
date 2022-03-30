from tabuleiro import Tabuleiro



class Controlador():
    def __init__(self, grid):
        self.tabuleiro1 = Tabuleiro(grid)
    

    def mover_jogador(self, direcao):
        self.tabuleiro1.mover_jogador()

