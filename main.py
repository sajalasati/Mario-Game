'''main module'''
import os
import board
from people import Player
from ticker import Ticker
import manage

M, N = 32, 400
POSITION_PLAYER = [8, M-7]
os.system('aplay -q mario-theme.wav&')


def main():
    '''main function'''
    game_board = board.Board(M, N)
    mario_player = Player(POSITION_PLAYER)
    tickers = []
    tickers.append(Ticker(0.1))
    tickers.append(Ticker(0.4))
    while True:
        manage.manage_objects(mario_player, game_board, tickers)
        game_board.render(mario_player)


if __name__ == '__main__':
    main()
