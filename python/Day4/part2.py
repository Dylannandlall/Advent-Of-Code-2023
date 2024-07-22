"""
Author: Dylan Nandlall
Advent of Code Day 4 Part 2
12/20/23
"""

### IDEA: 
### Create a queue that stores all copies of the card, increment the card total when a copy and original are stored
### Each original card loop will have a while loop that goes through the queue to solve all the copies before next iteration
### Store each card data in a dictionary for easy access when solving queue

from collections import deque

def solve_card(card):
    winning_numbers = card.split("|")[0].split(":")[1].split()
    possessed_numbers = card.split("|")[1].split()
    matches = 0
    
    for number in winning_numbers:
        if number in possessed_numbers:
            matches += 1

    return matches

def solution():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    card_total = 0
    card_deck = dict()
    card_queue = deque()

    for card in lines:
        card_id = int(card.split()[1][:-1])
        card = card
        card_deck[card_id] = card

    for card in lines:
        card_id = int(card.split()[1][:-1])
        print(card_id)

        matches = solve_card(card)
        card_total += 1
        if matches > 0:
            for i in range(matches):
                card_queue.append(card_id+i+1)
        
        while len(card_queue) > 0:
            id = card_queue.popleft()
            matches = solve_card(card_deck[id])
            card_total += 1
            if matches > 0:
                for i in range(matches):
                    card_queue.append(id+i+1)
    return card_total

def main():
    print(solution())

if __name__ == "__main__":
    main()



    
    

