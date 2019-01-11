'''a module for all people involved - mario, enemy and boss'''

import os
import random
import numpy as np
import manage
import figures
import moving_objects


class People:
    '''base class for people - enemy and mario in the game'''

    def __init__(self, name, posx, posy, lives, height, width):
        self.name = name
        self.posx = posx
        self.posy = posy
        self.lives = lives
        self.iskilled = False
        self.direc = "right"
        self.height = height
        self.width = width

    def left_move(self, steps):
        '''parent function to move left'''
        self.posx -= steps

    def right_move(self, steps):
        '''parent function to move left'''
        self.posx += steps

    def up_move(self, steps):
        '''parent function to move left'''
        self.posy -= steps

    def down_move(self, steps):
        '''parent function to move left'''
        self.posy += steps


class Player(People):
    '''class for mario player'''

    def __init__(self, pos):
        '''created in main'''
        People.__init__(self, "mario", pos[0], pos[1], 3, 1, 1)
        self.stop_jump = False
        self.bullets = 0
        self.score = 0
        self.onbridge = False
        self.left_bullet = u'\u2b31'
        self.right_bullet = u'\u21f6'
        self.right_bullets = []
        self.left_bullets = []

    def shoot_enemies(self):
        '''mario shooting the enemies'''
        if self.direc == 'right':
            bul = moving_objects.Bullets(
                self.right_bullet, self.posx+1, self.posy, 1)
            self.right_bullets.append(bul)
        else:
            bul = moving_objects.Bullets(
                self.left_bullet, self.posx-1, self.posy, -1)
            self.left_bullets.append(bul)

    def move_up(self, steps, game_board):
        '''mario move up function'''
        var = 0
        self.onbridge = False
        for i in range(steps):
            if game_board.get_board(self.posy-1-i, self.posx) == " ":
                var += 1
            elif game_board.get_board(self.posy-1-i, self.posx) == figures.COIN:
                self.score += 4
                game_board.set_board(self.posy-1-i, self.posx, " ")
                os.system('aplay -q coin.ogg')
            elif game_board.get_board(self.posy-1-i, self.posx) == figures.HIT_BRICK_KEY:
                manage.handle_bricks(
                    self.posx, figures.HIT_BRICK_KEY, game_board, self)
                break
            elif game_board.get_board(self.posy-1-i, self.posx) == figures.SOFT_BRICK_KEY:
                manage.handle_bricks(
                    self.posx, figures.SOFT_BRICK_KEY, game_board, self)
                break
            else:
                break
        self.up_move(var)

    def move_down(self, game_board):
        '''mario move down function'''
        if self.posy + 1 < game_board.height:
            if self.posy + 1 == game_board.height-3:
                for enemy in manage.ENEMY_OBJECT_LIST:
                    if enemy.posx == self.posx:
                        enemy.iskilled = True
                        self.score += 2
                        return
            if game_board.get_board(self.posy+1, self.posx) == " ":
                self.down_move(1)
            elif game_board.get_board(self.posy+1, self.posx) == "@":
                self.onbridge = True
                return
            elif game_board.get_board(self.posy+1, self.posx) == "%":
                self.move_up(12, game_board)
            elif game_board.get_board(self.posy+1, self.posx) == figures.COIN:
                self.score += 4
                game_board.set_board(self.posy+1, self.posx, " ")
                os.system('aplay -q coin.ogg')

    def move_left(self, steps, game_board):
        '''mario move left function'''
        self.direc = "left"
        var = 0
        for i in range(steps):
            if self.posx-1-i > game_board.shift+1:
                if self.posx-1-i in [enemy.posx for enemy
                                     in manage.ENEMY_OBJECT_LIST] and self.posy == 29:
                    self.lives -= 1
                    if self.lives is 0:
                        manage.game_over("You have no lives left", self)
                    break
                elif game_board.get_board(self.posy, self.posx-1-i) == " ":
                    var += 1
                elif game_board.get_board(self.posy, self.posx-1-i) == figures.COIN:
                    self.score += 4
                    game_board.set_board(self.posy, self.posx-1-i, " ")
                    var += 1
                    os.system('aplay -q coin.ogg')
                elif game_board.get_board(self.posy, self.posx-1-i) in figures.DANGERS:
                    self.lives -= 1
                    if self.lives is 0:
                        manage.game_over("You have no lives left", self)
                    manage.respawn(self, game_board)
                    break
                else:
                    break
            else:
                break
        self.left_move(var)

    def move_right(self, steps, game_board, test):
        '''mario move right function'''
        self.direc = "right"
        var = 0
        for i in range(steps):
            if self.posx+1+i < 398:
                if self.posx+1+i in [enemy.posx for enemy in
                                     manage.ENEMY_OBJECT_LIST] and self.posy == 29:
                    self.lives -= 1
                    if self.lives is 0:
                        if test is 1:
                            return 1
                        else:
                            manage.game_over("You have no lives left", self)
                    break
                elif game_board.get_board(self.posy, self.posx+1+i) == " ":
                    var += 1
                elif game_board.get_board(self.posy, self.posx+1+i) == figures.COIN:
                    game_board.set_board(self.posy, self.posx+1+i, " ")
                    self.score += 4
                    os.system('aplay -q smb_coin.wav&')
                elif game_board.get_board(self.posy, self.posx+1+i) in figures.DANGERS:
                    self.lives -= 1
                    if self.lives is 0:
                        if test is 1:
                            return 1
                        else:
                            manage.game_over("You have no lives left", self)
                    manage.respawn(self, game_board)
                    break
                else:
                    break
            else:
                break
        self.right_move(var)


class Enemy(People):
    '''class for enemy'''

    def __init__(self, pos):
        People.__init__(self, "enemy", pos[0], pos[2], 1, 1, 1)
        self.rangex = pos[:2]  # range in which it will move
        self.goright = "right"


class EnemyBoss(People):
    '''smart enemy S approaches the mario'''

    def __init__(self, pos, game_board):
        '''posx and posy correspond to bottom left corner'''
        People.__init__(self, "boss", pos[0], pos[1], 10, 3, 4)
        self._fig = np.empty(figures.BOSS_FIG.shape, dtype='str')
        self._fig[:] = figures.BOSS_FIG
        self.right_bullets = []
        self.left_bullets = []
        self.left_bullet = '<'
        self.right_bullet = '>'
        game_board.set_range_board(self.posy-2, self.posy+1,
                                   self.posx, self.posx+4, self._fig)

    def shoot_mario(self, mario_player):
        '''calls shoot_bullet accroding to probability'''
        if mario_player.posx > 65:
            var = random.randint(0, 100)
            if var < 2:
                self.shoot_bullet(mario_player)

    def shoot_bullet(self, mario_player):
        '''shoot a bullet in appropriate direction'''
        if mario_player.posx > self.posx:
            bul = moving_objects.Bullets(
                self.right_bullet, self.posx+2, self.posy, 1)
            self.right_bullets.append(bul)
        else:
            bul = moving_objects.Bullets(
                self.left_bullet, self.posx-1, self.posy, -1)
            self.left_bullets.append(bul)
