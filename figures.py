'''this module contains all the objects of game board'''

import numpy as np
import moving_objects

OBSTACLES = ['/', '\\', '0', '@']
DANGERS = ['/', '\\', '0', 'E']

# currently single boss
ALL_BOSS_KILLED = False

# harcoded y coordinates
BRIDGE = moving_objects.Bridge([25, 92])

MOUNTAIN_KEY = u'\u25b2'
OBSTACLES.append(MOUNTAIN_KEY)
MOUNTAIN = np.empty((5, 9), dtype='str')
MOUNTAIN[:] = ' '
for i in range(5):
    for j in range(5-i-1, 5+i):
        MOUNTAIN[i, j] = MOUNTAIN_KEY

CLOUD = np.array([' ', ' ', '_', '_', ' ', ' ', ' ',
                  '(', ' ', ' ', ')', ' ', '(', '_', '_', '_', '_', ')'])
CLOUD = CLOUD.reshape(3, 6)

COIN = u'\u25c9'
OBSTACLES.append(COIN)
COIN_LIST = np.empty(8, dtype='str')
COIN_LIST[:] = [COIN, ' ', COIN, ' ', COIN, ' ', COIN, ' ']

WATER_SMALL = np.empty((2, 20), dtype='str')
WATER_SMALL[:] = ' '

SMALL_BUILDING_KEY = 'W'
OBSTACLES.append(SMALL_BUILDING_KEY)
SMALL_BUILDING = np.empty((4, 14), dtype='str')
SMALL_BUILDING[:] = SMALL_BUILDING_KEY
SMALL_BUILDING[1:4, 1:13] = ' '

START_BUILDING_KEY = u'\u25a4'
OBSTACLES.append(START_BUILDING_KEY)
START_BUILDING = np.empty((4, 14), dtype='str')
START_BUILDING[:] = START_BUILDING_KEY
START_BUILDING[1, 4:10] = [' ', 'S', 'T', 'A', 'R', 'T']

COMPLETE_BUILDING_KEY = u'\u25a4'
OBSTACLES.append(COMPLETE_BUILDING_KEY)
COMPLETE_BUILDING = np.empty((4, 14), dtype='str')
COMPLETE_BUILDING[:] = COMPLETE_BUILDING_KEY
COMPLETE_BUILDING[1, 2:12] = [' ', 'C', 'O', 'M', 'P', 'L', 'E', 'T', 'E', ' ']
COMPLETE_BUILDING[2, 5:10] = [' ', 'T', 'H', 'E', ' ']
COMPLETE_BUILDING[3, 4:11] = [' ', 'L', 'E', 'V', 'E', 'L', ' ']

HIGH_TOWER_KEY = u'\u25a5'
OBSTACLES.append(HIGH_TOWER_KEY)
HIGH_TOWER = np.empty((10, 1), dtype='str')
HIGH_TOWER[:] = HIGH_TOWER_KEY

BOSS_FIG = np.empty(12, dtype='str')
BOSS_FIG[:] = [' ', '0', '0', ' ', '\\', 'W', 'W', '/', ' ', '/', '\\', ' ']
BOSS_FIG = BOSS_FIG.reshape(3, 4)

EMPTY_BOSS_FIG = np.empty(12, dtype='str')
EMPTY_BOSS_FIG[:] = [' ', ' ', ' ', ' ',
                     ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
EMPTY_BOSS_FIG = EMPTY_BOSS_FIG.reshape(3, 4)

ENEMY = np.empty(1, dtype='str')
ENEMY[:] = ['E']
ENEMY = ENEMY.reshape(1, 1)

MARIO = np.empty(4, dtype='str')
MARIO[:] = ['U', 'U', 'T', 'T']
MARIO = MARIO.reshape(2, 2)

SPRING = np.empty(8, dtype='str')
SPRING[:] = '%'
OBSTACLES.append('%')

# SOFT_BRICK_KEY = '?'
SOFT_BRICK_KEY = u'\u25a3'
OBSTACLES.append(SOFT_BRICK_KEY)


def get_soft_brick(coins):
    ''' get a soft brick'''
    soft_brick = np.empty((2, 3), dtype='str')
    soft_brick[0, :] = str(coins)  # just for example 3 points brick
    soft_brick[1, :] = SOFT_BRICK_KEY
    return soft_brick


HARD_BRICK_KEY = u'\u2588'
OBSTACLES.append(HARD_BRICK_KEY)
HARD_BRICK = np.empty((2, 4), dtype='str')
HARD_BRICK[:] = HARD_BRICK_KEY

# HIT_BRICK_KEY = "B"
HIT_BRICK_KEY = u'\u2591'
OBSTACLES.append(HIT_BRICK_KEY)
HIT_BRICK = np.empty((2, 4), dtype='str')
HIT_BRICK[:] = HIT_BRICK

# HBL - hard
# hbt - hit
# SBL - soft
# x1,x2,y1,y2,coins number
HBL = [[45, 49, 25, 27], [115, 119, 20, 22], [119, 123, 20, 22], [117, 121, 25, 27], [
    237, 241, 25, 27], [241, 245, 25, 27]]  # contains the ending appropriate for numpy array

# contains the ending appropriate for numpy array
SBL = [[39, 42, 25, 27, 2], [112, 115, 23, 25, 1]]
CST = [[56, 64, 29], [115, 123, 16], [133, 141, 29],
       [171, 179, 29]]  # contains string of coins

# Enemy represented by E
# range in which "Normal" enemies will move
# [x1,x2,y coord] ENEMY will start at x1 i.e posx=x1

ENEMY_LIST = [[30, 31, 29], [150, 155, 29], [
    204, 212, 29], [219, 228, 29], [230, 240, 29], ]

ENEMY_LEFT_ARROW = u'\u2b31'
ENEMY_RIGHT_ARROW = u'\u21f6'
