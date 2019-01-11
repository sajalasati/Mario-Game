'''module containing all the moving objects'''

import numpy as np


class Bridge:
    '''bridge object in the game'''

    def __init__(self, pos):
        self.posx = pos[1]
        self.posy = pos[0]
        self.maxup = 17
        self.maxdown = 27
        self.length = 14
        self._fig = np.empty(14, dtype='str')
        self._fig[:] = '@'
        self.go_up = True

    def move_up(self, game_board):
        '''to move the bridge upwards'''
        if self.go_up is True:
            if self.posy != self.maxup:
                game_board.set_range_board(
                    self.posy, self.posy+1, self.posx, self.posx+self.length, " ")
                self.posy -= 1
                game_board.set_range_board(
                    self.posy, self.posy+1, self.posx, self.posx+self.length, "@")
            else:
                self.go_up = False
                self.move_down(game_board)
        else:
            return

    def move_down(self, game_board):
        '''to move the bridge downwards'''
        if self.go_up is False:
            if self.posy != self.maxdown:
                game_board.set_range_board(
                    self.posy, self.posy+1, self.posx, self.posx+self.length, " ")
                self.posy += 1
                game_board.set_range_board(
                    self.posy, self.posy+1, self.posx, self.posx+self.length, "@")
            else:
                self.go_up = True
                self.move_up(game_board)
        else:
            return

    def move(self, game_board):
        '''board oscillates between initial posy and maxup'''
        if self.go_up is True:
            self.move_up(game_board)
        else:
            self.move_down(game_board)


class Bullets:
    '''anyone among mario,boss enemy can create bullets from here'''

    def __init__(self, shape, posx, posy, vel):
        self.posx = posx
        self.posy = posy
        self.velocity = vel
        self.range = [self.posx - 30, self.posx+30]

        # bullets deactivate after 30 steps
        self.life = 1
        self.shape = shape  # an ascii or unicode character

    def move(self):
        self.posx += self.velocity
