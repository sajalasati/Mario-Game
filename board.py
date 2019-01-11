'''this module creates and manages the mario board'''

import os
import numpy as np
import manage


class Board:
    '''main board class'''

    def __init__(self, m, n):
        '''preferred size = (32, 400)'''
        assert isinstance(n, int) is True
        assert isinstance(m, int) is True
        self.width = n
        self.height = m
        self.dimen = (self.height, self.width)
        self._b = np.empty(self.dimen, dtype='str')
        self.shift = 0
        self.init_board()

    def init_board(self):
        '''initialize and setup the frame of the board'''
        self._b[:] = 'X'
        self._b[1:30, 0:400] = " "
        # to add obstacles and other things on start of game
        manage.add_obstacles(self)

    def set_board(self, posx, posy, value):
        '''set a cell in board'''
        self._b[posx, posy] = value

    def set_range_board(self, posx1, posx2, posy1, posy2, value):
        '''set a grid of cells in board'''
        self._b[posx1:posx2, posy1:posy2] = value

    def get_board(self, posx, posy):
        '''get a cell in board'''
        return self._b[posx, posy]

    def render(self, player):
        '''display and render the board at every frame'''
        os.system('tput reset')
        print("Score is:", player.score, "\t\t\t Lives are:", player.lives,
              "\t", player.posx, "\t", player.posy)

        temp = [[enemy.posy, enemy.posx]
                for enemy in manage.ENEMY_OBJECT_LIST]
        for row in range(self.height):
            for col in range(self.shift, 80 + self.shift):
                if row >= 1 and row < self.height - \
                        2 and col >= self.shift and col < self.shift + 2:
                    print('X', end="")
                elif row >= 1 and row < self.height - 2 and col >= self.shift + 78 \
                        and col < self.shift + 80:
                    print('X', end="")
                elif row == player.posy and col == player.posx:
                    print('M', end="")
                elif [row, col] in temp:
                    print('E', end="")
                elif [col, row] in [[b.posx, b.posy] for b in player.left_bullets]:
                    print(player.left_bullet, end="")
                elif [col, row] in [[b.posx, b.posy] for b in player.right_bullets]:
                    print(player.right_bullet, end="")
                elif manage.BOSS_ENEMY and\
                        [col, row] in \
                        [[b.posx, b.posy] for b in manage.BOSS_ENEMY[0].left_bullets]:
                    print(player.left_bullet, end="")
                elif manage.BOSS_ENEMY and [col, row] in \
                        [[b.posx, b.posy] for b in manage.BOSS_ENEMY[0].right_bullets]:
                    print(player.right_bullet, end="")
                else:
                    print(self._b[row, col], end="")
            print()
