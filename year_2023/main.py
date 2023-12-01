import re

sum = 0

with open('input.txt','r') as input_file:
    for line in input_file:
       data = (re.findall(r'\d', line))
       sum = int((str(data[0])+str(data[-1]))) + sum
       
    print(sum) 
