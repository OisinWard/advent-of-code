import re

line_num = 1
sum_part_1 = 0

# Code for part 1 
with open('input.txt','r') as input_file:
    for line in input_file:
       if not ((re.search(r'(1[3-9] red|1[4-9] green|1[5-9] blue|[2-9][0-9] red|[2-9][0-9] green|[2-9][0-9] blue)', line))): 
           sum_part_1 = line_num + sum_part_1
       line_num += 1
    print( sum_part_1 )
       
