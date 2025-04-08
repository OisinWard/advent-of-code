import re

# Code for part 1 

def is_special_character(character):
    if character != '.' and character.isdigit() == False:
        return True
    else: 
        return False

lines = open("./input.txt").read().splitlines()
for y_pos, line in enumerate(lines):
    for x_pos, char in enumerate(line):
        if is_special_character(char):
            for cur_y_pos in [y_pos - 1, y_pos, y_pos + 1]: 
                print(cur_y_pos)
