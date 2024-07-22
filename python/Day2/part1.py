"""
Author: Dylan Nandlall
Advent of Code Day 2 Part 1
"""

RED = 12
GREEN = 13
BLUE = 14

with open("input.txt") as f:
    lines = f.read().splitlines()

total = 0
for line in lines:
    game_id = line.split()[1][:-1]
    game = line.split(":")[1].strip()
    
    max_list = [0, 0, 0]
    for group in game.split(";"):
        for cube in group.strip().split(","):
            cube_count = cube.split()[0]
            cube_color = cube.split()[1]
            
            if cube_color == "red" and int(cube_count) > RED:
                max_list[0] = int(cube_count)
            if cube_color == "green" and int(cube_count) > GREEN:
                max_list[1] = int(cube_count)
            if cube_color == "blue" and int(cube_count) > BLUE:
                max_list[2] = int(cube_count)
        
    if max_list[0] <= RED and max_list[1] <= GREEN and max_list[2] <= BLUE:
        total += int(game_id)

print(total)