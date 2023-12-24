"""
Author: Dylan Nandlall
Advent of Code Day 4 Part 1
"""

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

total = 0
for line in lines:
    winning_numbers = line.split("|")[0].split(":")[1].split()
    possessed_numbers = line.split("|")[1].split()
    matches = 0

    for number in winning_numbers:
        if number in possessed_numbers:
            matches += 1
    
    if matches < 1:
        continue
    elif matches == 1:
        total += 1
    else:
        total += 2 ** (matches-1)

print(total)