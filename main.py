import pygame
from board import Board
from player import Player
import sqlite3

#criando uma base de dados SQL para registrar as pontuações
conn = sqlite3.connect('records.sqlite')
cur = conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS Jogador;
CREATE TABLE Jogador(
    id        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    nome      TEXT UNIQUE,
    score     INTEGER NOT NULL
)''')

name = input('Digite seu nome: ')

'''tabuleiro1 = Board()
tabuleiro1.create_board1()
print(tabuleiro1.matrix)'''

'''tabuleiro2 = Board()
tabuleiro2.create_board2()
print(tabuleiro2.matrix)'''

jogador1 = Player(position=[0,0])

def main():
    pygame.init
    
    score = 0

#executando o script SQL para inserir o nome e a pontuação na base de dados
    cur.execute('''INSERT OR IGNORE INTO Jogador (nome)
            VALUES ( ? )''', ( name, ) )




main()


