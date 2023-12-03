import re

line_num = 1
sum_part_1 = 0

# Code for part 1 
with open('input.txt','r') as input_file:
    for line in input_file:
       for match in re.finditer(r'\d+', line):
         print (match)
    #       sum_part_1 = line_num + sum_part_1
    #   line_num += 1
    print( sum_part_1 )
       
