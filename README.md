# Mario Game

[![Language](https://img.shields.io/badge/language-python-blue.svg?style=flat)](https://www.python.org)
[![Module](https://img.shields.io/badge/module-numpy-brightgreen.svg?style=flat)](http://www.numpy.org/)

This **README** file contains :

1.  Information About the Game
2.  Rules of the Game
3.  Description of Classes Created
4.  Instructions on how to Run the Code
5.  Requirements

### About

> **Mario Bros** (マリオブラザーズ Mario Burazāzu) is a platform game published and developed for arcades by Nintendo in 1983. It was created by Shigeru Miyamoto. It has been featured as a minigame in the Super Mario Advance series and numerous other games. Mario Bros. has been re-released for the Wii's, Nintendo 3DS's, and Wii U's Virtual Console services in Japan, North America, Europe and Australia. This game is an attempt to recreate the first level of Super Mario Bros.

For more information click [here](https://en.wikipedia.org/wiki/Mario_Bros).

**Important** to note that the game has been tested on **ONLY** Linux-based OSs.

### Rules of the Game

> - A,S,W,D : to control Left,Down,Up and Right movements of the Mario (M character)
> - Enemies and Boss can be killed by shooting bullets by pressing 'C' key, but _contact_ with them can kill the Mario(decrease the life by one).
> - Falling in the hole also decreases the life of the Mario.
> - Normal enemies ('E') can be killed by single hit but killing Boss Enemy requires multiple hits
> - You have 3 lives for you, getting killed 3 times will result in a **GAME OVER**.
> - The Mario and Boss enemy's bullets deactivate after certain range.
> - Each coin adds 4 points, killing normal enemy adds 2 points to the score, while killing boss enemy adds 10 points.

### Description of Classes Created

> **Board**:
> The board class creates a 32X80 board for gameplay, with boundaries, walls, empty spaces, bricks and various other obstacles, moving objects and characters. It also comprises of render and init_board function.
> **Bullets**:
> The Bullets class provides Mario and Boss Enemy with bullets when they shoot.
> **People**:
> The People class has all the variables and basic functionality common for Mario and enemies.
> **Player**:
> The Player class inherits any People class, it provides movement functionality, and shooting options for the Mario Player and stores various things like its score and lives.
> **Enemy**:
> The Enemy class also inherits People. It provides the motion, deletion, generation and functionality of enemies.
> **EnemyBoss**:
> EnemyBoss class inherits People class, in addition to functionality of normal enemy it also has 'smart sense' so as to kill the Mario.
> **Bridge**:
> Creates a Bridge object which moves up and down.

## Requirements

- Python3

For mac:

```
brew cask update
sudo brew cask install python3
```

For Linux:

```
sudo apt-get update
sudo apt-get install python3
```

- Install the rest of the dependencies from the requirements file.

### How To Play:

> - Run the following code to start the game.

```
cd MarioGame
python3 main.py
```

> - Press enter to start the game.
> - 'w, a, s, d' use these controls for up, left, down, and right.
> - i is a cheatcode to increase lives
> - use 'c' to plant a bomb.
> - press 'q' to quit.

### Author:

Sajal Asati
