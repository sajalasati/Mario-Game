'''this module contains various functions controlling game'''

import os
import time
import signal
import figures
import people
from alarmexception import AlarmException
from getch import _getChUnix


# contains all enemy objects
ENEMY_OBJECT_LIST = []
# contains all bosses
BOSS_ENEMY = []
POS_BOS = [260, 29]


def add_coins(game_board):
    '''add coins to various places'''
    game_board.set_range_board(29, 30, 56, 64, figures.COIN_LIST)
    game_board.set_range_board(16, 17, 115, 123, figures.COIN_LIST)
    game_board.set_range_board(29, 30, 133, 141, figures.COIN_LIST)
    game_board.set_range_board(29, 30, 171, 179, figures.COIN_LIST)
    game_board.set_range_board(24, 25, 237, 245, figures.COIN_LIST)


def add_scenery(game_board):
    '''clouds, mountain, water'''
    for i in range(3, 350, 20):
        game_board.set_range_board(1, 4, i, i+6, figures.CLOUD)
        game_board.set_range_board(2, 7, i+8, i+17, figures.MOUNTAIN)

    game_board.set_range_board(game_board.height-2, game_board.height,
                               90, 110, figures.WATER_SMALL)


def add_buildings(game_board):
    '''buildings(start & end), towers, spring, bridge'''
    game_board.set_range_board(26, 30, 2, 16, figures.START_BUILDING)

    game_board.set_range_board(26, 30, 76, 90, figures.SMALL_BUILDING)
    game_board.set_range_board(26, 30, 185, 199, figures.SMALL_BUILDING)

    game_board.set_range_board(25, 26, 191, 199, figures.SPRING)

    game_board.set_range_board(20, 30, 216, 217, figures.HIGH_TOWER)
    game_board.set_range_board(20, 30, 280, 281, figures.HIGH_TOWER)

    # intial append of bridge to the board
    game_board.set_range_board(figures.BRIDGE.posy, figures.BRIDGE.posy+1,
                               figures.BRIDGE.posx, figures.BRIDGE.posx+14, '@')


def add_bricks(game_board):
    ''' add hard and soft bricks'''
    # hard
    for i in range(len(figures.HBL)):
        game_board.set_range_board(figures.HBL[i][2], figures.HBL[i][3], figures.HBL[i]
                                   [0], figures.HBL[i][1], figures.HARD_BRICK)

    # add soft bricks to collect coins from and they turn into hard ones later
    for i in range(len(figures.SBL)):
        game_board.set_range_board(figures.SBL[i][2], figures.SBL[i][3],
                                   figures.SBL[i][0], figures.SBL[i][1],
                                   figures.get_soft_brick(figures.SBL[i][4]))


def add_enemies(game_board):
    '''normal enemies and boss enemy'''
    # here we loop and create the enemies objects using enemy list
    # and append created enemies to enemy_object_list
    for i in range(len(figures.ENEMY_LIST)):
        enem = people.Enemy(figures.ENEMY_LIST[i])
        ENEMY_OBJECT_LIST.append(enem)
    boss = people.EnemyBoss(POS_BOS, game_board)
    BOSS_ENEMY.append(boss)


def add_obstacles(game_board):
    '''main function called in the start to add obstacles to game board'''

    add_scenery(game_board)
    add_coins(game_board)
    add_buildings(game_board)
    add_bricks(game_board)
    add_enemies(game_board)


def move_bridge(game_board, ticker):
    '''move the bridge'''
    var = ticker.get()
    if var > 0.4:
        figures.BRIDGE.move(game_board)  # move bridge


def check_if_in_air(mario_player, game_board, ticker1):
    if mario_player.onbridge is False or figures.BRIDGE.go_up is False:
        if ticker1.get() > 0.1:
            if mario_player.posy == game_board.height - 1:
                if mario_player.iskilled is False:
                    mario_player.lives -= 1
                    mario_player.iskilled = True
                mario_player.stop_jump = False
                if mario_player.lives == 0:
                    game_over("You have no lives left", mario_player)
                else:
                    respawn(mario_player, game_board)
                return
            elif mario_player.posy < game_board.height-1:
                if game_board.get_board(mario_player.posy+1, mario_player.posx) != ' ':
                    mario_player.stop_jump = False
                # to be called in every case to check for going down
                mario_player.move_down(game_board)

    elif mario_player.onbridge is True and figures.BRIDGE.go_up is True:
        mario_player.posy = figures.BRIDGE.posy-1


def alarmhandler(signum, frame):
    ''' input method '''
    raise AlarmException


def user_input(timeout=0.1):
    ''' input method '''
    signal.signal(signal.SIGALRM, alarmhandler)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    try:
        text = _getChUnix()()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''


def move_mario_player(mario_player, game_board, ticker):
    '''takes input and moves mario'''

    char = user_input()
    check_if_in_air(mario_player, game_board, ticker)

    # Press 'q' for quit.
    if char == 'q':
        os.system('pkill -kill aplay')
        os.system('aplay -q smb_gameover.wav&')
        print("The game was quitted!!")
        quit()
    # Press 'w' for up.
    if char == 'w':
        if mario_player.stop_jump is False:
            os.system('aplay -q smb_jump-small.wav&')
            mario_player.iskilled = False
            mario_player.move_up(6, game_board)
            mario_player.stop_jump = True
            mario_player.onbridge = False  # as it has jumped hence it cannot be on bridge

    # Press 's' for down.
    if char == 's':
        mario_player.move_down(game_board)
    # Press 'a' for left.
    if char == 'a':
        if mario_player.stop_jump is True:
            mario_player.move_left(2, game_board)
        else:
            mario_player.move_left(1, game_board)
    # Press 'd' for right.
    if char == 'd':
        if mario_player.stop_jump is True:
            mario_player.move_right(2, game_board, 0)
        else:
            mario_player.move_right(1, game_board, 0)
    # Press 'c' to shoot
    if char == 'c':
        mario_player.shoot_enemies()

    # Cheatcode to increase lives
    if char == 'i':
        mario_player.lives += 1

    if mario_player.posx not in range(figures.BRIDGE.posx, figures.BRIDGE.posx+12):
        mario_player.onbridge = False
    game_board.shift = min(300, max(game_board.shift, mario_player.posx-39))

    if mario_player.posx == 287 and mario_player.posy == 25:
        game_over("You won", mario_player)


def remove_killed_enemies():
    for enemy in ENEMY_OBJECT_LIST:
        if enemy.iskilled is True:
            ENEMY_OBJECT_LIST.remove(enemy)


def manage_objects(mario_player, game_board, tickers):
    '''move enemy,bullets,boss,mario,bridge etc moving objects on screen'''

    move_bridge(game_board, tickers[1])
    move_mario_player(mario_player, game_board, tickers[0])
    move_bullets(mario_player, game_board)
    detect_bullet_hits(mario_player, game_board)
    remove_killed_enemies()

    if figures.ALL_BOSS_KILLED is True:
        game_board.set_range_board(20, 30, 280, 281, " ")
        game_board.set_range_board(26, 30, 280, 294, figures.COMPLETE_BUILDING)
        game_board.set_range_board(25, 26, 291, 294, ['E', 'N', 'D'])

    if BOSS_ENEMY:
        BOSS_ENEMY[0].shoot_mario(mario_player)


def bullets_moving(game_board, bul_list):
    '''helper function to move bullets and remove unwanted ones'''
    # return len(bul_list)
    for bullet in bul_list:
        if game_board.get_board(bullet.posy, bullet.posx+1) in figures.OBSTACLES:
            # return -189
            bul_list.remove(bullet)
        else:
            bullet.move()
            if bullet.posx not in range(bullet.range[0], bullet.range[1]+1):
                bul_list.remove(bullet)


def move_bullets(mario_player, game_board):
    '''just move bullets are shot by mario and boss'''
    if BOSS_ENEMY:
        bullets_moving(game_board, BOSS_ENEMY[0].left_bullets)
        bullets_moving(game_board, BOSS_ENEMY[0].right_bullets)
    bullets_moving(game_board, mario_player.left_bullets)
    bullets_moving(game_board, mario_player.right_bullets)


def mario_boss_bullet_hits(per, bul_list, mario_player):
    '''function to detect bullet hits on mario or boss enemy'''
    for bullet in bul_list:
        if per.posx == bullet.posx and bullet.posy in range(per.posy, per.posy+per.height):
            bul_list.remove(bullet)
            if per.lives > 0:
                per.lives -= 1
            if per.lives == 0:
                if per.name == "mario":
                    game_over("You have no lives left", mario_player)
                elif per.name == "boss":
                    per.iskilled = True
                    mario_player.score += 10


def enemy_bullet_hits(bul_list, mario_player):
    '''function to detect whether a enemy was hit by bullet'''
    for enem in ENEMY_OBJECT_LIST:
        for bullet in bul_list:
            if enem.posx == bullet.posx and bullet.posy == enem.posy:
                mario_player.score += 2
                ENEMY_OBJECT_LIST.remove(enem)
                bul_list.remove(bullet)


def detect_bullet_hits(mario_player, game_board):
    '''mario fires bullets to normal enemies and boss and boss fires bullets on mario'''
    # all bullets have already moved
    if BOSS_ENEMY:
        mario_boss_bullet_hits(
            mario_player, BOSS_ENEMY[0].left_bullets, mario_player)
        mario_boss_bullet_hits(
            mario_player, BOSS_ENEMY[0].right_bullets, mario_player)
        mario_boss_bullet_hits(
            BOSS_ENEMY[0], mario_player.left_bullets, mario_player)
        mario_boss_bullet_hits(
            BOSS_ENEMY[0], mario_player.right_bullets, mario_player)
        # remove the boss if killed
        if BOSS_ENEMY[0].iskilled:
            figures.ALL_BOSS_KILLED = True
            for hello in range(BOSS_ENEMY[0].posy-2, BOSS_ENEMY[0].posy+1):
                for world in range(BOSS_ENEMY[0].posx, BOSS_ENEMY[0].posx+4):
                    game_board.set_board(hello, world, " ")
            BOSS_ENEMY.pop()

    enemy_bullet_hits(mario_player.right_bullets, mario_player)
    enemy_bullet_hits(mario_player.left_bullets, mario_player)


def destroy_soft_bricks(posx, game_board, mario_player):
    '''function to destroy a soft brick'''
    for i in range(len(figures.SBL)):
        if posx >= figures.SBL[i][0] and posx < figures.SBL[i][1]:
            if figures.SBL[i][4] == 1:
                mario_player.score += 1
                game_board.set_range_board(figures.SBL[i][2], figures.SBL[i][3], figures.SBL[i]
                                           [0], figures.SBL[i][1], figures.HARD_BRICK_KEY)
            else:
                figures.SBL[i][4] -= 1
                mario_player.score += 1
                game_board.set_range_board(figures.SBL[i][2], figures.SBL[i][2]+1, figures.SBL[i]
                                           [0], figures.SBL[i][1], figures.SBL[i][4])
                game_board.set_range_board(figures.SBL[i][3]-1, figures.SBL[i][3], figures.SBL[i]
                                           [0], figures.SBL[i][1], figures.SOFT_BRICK_KEY)
            break


def handle_bricks(posx, types, game_board, mario_player):
    ''' handle collision with the bricks '''
    if types == figures.SOFT_BRICK_KEY:
        destroy_soft_bricks(posx, game_board, mario_player)
    else:
        pass


def respawn(mario_player, game_board):
    '''respawn a player after one life is lost'''
    mario_player.posx = 8
    mario_player.posy = 25
    game_board.shift = 0
    os.system('tput reset')
    print("Re-Spawning")
    print("Lives left:", mario_player.lives)
    time.sleep(3)
    game_board.render(mario_player)


def game_over(statement, mario_player):
    '''finish game function when all lives are over'''
    os.system("tput reset")
    print(statement)
    print("Score:", mario_player.score)
    print("The Game is Over")
    os.system('pkill -kill aplay')
    os.system('aplay -q smb_gameover.wav')
    quit()
