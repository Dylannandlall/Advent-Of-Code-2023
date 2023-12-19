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
    game_id = line.split(":")[0].split(" ")[1]
    game = line.split(":")[1].strip()
    
    red = 0
    green = 0
    blue = 0
    for set in game.split(";"):
        for cube in set.split(","):
            #print(cube)
            cube_count = cube.strip().split(" ")[0]
            cube_color = cube.strip().split(" ")[1]

            if cube_color == "red":
                red += int(cube_count)
            elif cube_color == "green":
                green += int(cube_count)
            elif cube_color == "blue":
                blue += int(cube_count)

    #print("red: {}, green: {}, blue: {}".format(red, green, blue))
    if red <= RED and green <= GREEN and blue <= BLUE:
        total += int(game_id)

print(total)

