from random import random

level_map_1 = [
    '                        ',
    '                  X     ',
    '                        ',
    '                        ',
    '                        ',
    'XX                      ',
    '                      X ',
    '     X      X   XXXXX   ',
    'X X      X              ',
    'X   X                   ',
    'X      X  X      X    X ',
    'X                     X ',
    'XXX P       XXX      xxx',
    'XXXXXXX       XX        ',
    'XXXXXXXXXXX   XXXXX    X',
]

tile_size = 32

DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = len(level_map_1) * tile_size

ROWS = len(level_map_1)
CELLS = len(level_map_1[0])

print(len(level_map_1), " x ", len(level_map_1[0]))


def generate_random_map():
    level_map = []
    for i in range(15):
        line = ""
        for j in range(24):
            var = random()
            if i != 14:
                if var > 0.008 * (i + 1):
                    line += " "
                else:
                    line += "X"
            else:
                if var > 0.7:
                    line += " "
                else:
                    line += "X"

        # pad the line with spaces to ensure it has the same length as the others
        line = line.ljust(24)
        level_map.append(line)

    for line in level_map:
        print(line)

    return level_map
