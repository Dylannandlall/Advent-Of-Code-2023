"""
Author: Dylan Nandlall
Advent of Code Day 1
"""
mapping = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five":'5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9',
        "zero": '0'
        }

with open("input.txt", "r") as f:
    data = f.read().splitlines()

total = 0
line_num = 0
for line in data:
    num_list = []
    # Gets the number in the line and appends the index and number to the list
    for i in range(len(line)):
        if line[i].isdigit():
            num_list.append([i, line[i]])
    # Gets all the occurences of the number word in the line and appends the index and number to the list   
    for key in mapping.keys():
        current_index = line.find(key)
        while current_index != -1:
            num_list.append([current_index, mapping[key]])
            current_index = line.find(key, current_index + 1)
    # Sorts the list by index and then gets the number from the list
    num_list = sorted(num_list, key=lambda x: x[0])
    number = int(num_list[0][1] + num_list[-1][1])
    total += number
    line_num += 1

print(total)


