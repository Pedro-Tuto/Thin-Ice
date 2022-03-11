import pygame
from board import Board
from player import Player
import sqlite3
import sys

#criando uma base de dados SQL para registrar as pontuações
conn = sqlite3.connect('records.sqlite')
cur = conn.cursor()
cur.executescript('''
CREATE TABLE IF NOT EXISTS Jogador(
    id        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    nome      TEXT UNIQUE,
    score     INTEGER NOT NULL
)''')

name = input('Digite seu nome: ')
cur.execute('''INSERT OR IGNORE INTO Jogador (nome) 
        VALUES ( ? )''', ( name, ) )
conn.commit()

jogador1 = Player(position=[0,0])

largura_tela = 800
altura_tela = 600

def main():
    #chamando os métodos do pygame para iniciar o jogo
    pygame.init
    #dimensões da janela
    pygame.display.set_mode((800,600))
    #nome do programa aberto
    pygame.display.set_caption('Thin Ice')
    #definindo o clock em que o jogo roda
    clock = pygame.time.Clock()
    #definindo o tick em que o clock funciona(FPS)
    clock.tick(60)

    
'''tabuleiro1 = Board()
tabuleiro1.create_board1()
print(tabuleiro1.matrix)'''

'''tabuleiro2 = Board()
tabuleiro2.create_board2()
print(tabuleiro2.matrix)'''






main()


