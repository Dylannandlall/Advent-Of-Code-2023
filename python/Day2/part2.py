"""
Author: Dylan Nandlall
Advent of Code Day 2 Part 2
"""

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

total = 0
for line in lines:
    game = line.split(":")[1].strip()
    
    max_list = [0, 0, 0]
    for set in game.split(";"):
        for cubes in set.strip().split(","):
            cube_count = cubes.split()[0]
            cube_color = cubes.split()[1]
            
            if cube_color == "red" and int(cube_count) > max_list[0]:
                max_list[0] = int(cube_count)
            if cube_color == "green" and int(cube_count) > max_list[1]:
                max_list[1] = int(cube_count)
            if cube_color == "blue" and int(cube_count) > max_list[2]:
                max_list[2] = int(cube_count)

    total += (max_list[0] * max_list[1] * max_list[2])
print(total)

