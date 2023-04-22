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


def generate_random_map(rank=0.9):
    level_map = []
    first_line = ""

    for cell in range(24):
        var = random()
        if var > (rank * 2 / 3):
            first_line += " "
        else:
            first_line += "X"

    level_map.insert(0, first_line)

    for i in range(3):
        line = ""
        for cell in range(24):
            if level_map[len(level_map) - 1 - i][cell] == "X":
                var = random()
                if cell > 0 and line[cell - 1] == "X":
                    if var > rank:
                        line += " "
                    else:
                        line += "X"
                else:
                    if var > (rank * 2 / 3):
                        line += " "
                    else:
                        line += "X"
            else:
                line += " "

        level_map.insert(0, line)

    emptyLine = '                        '  # 24 Cells
    for i in range(11):
        level_map.insert(0, emptyLine)

    # for line in level_map:
    #     print(line)

    return level_map
