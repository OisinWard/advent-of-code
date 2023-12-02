import re

sum = 0

# Code for part 1 
with open('input.txt','r') as input_file:
    for line in input_file:
       data = (re.findall(r'\d', line))
       sum = int((str(data[0])+str(data[-1]))) + sum
       
    print(sum) 

# Code for part 2
sum = 0
numbers = [
    'one', 
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9'
]

first_occurance_tracker = 100
first_number = ""
last_occurance_tracker = 100
last_number = ""

with open('input.txt','r') as input_file:
    for line in input_file:
       data = (re.findall(r'\d', line))
       for i in numbers:
           if(line.find(i) < first_occurance_tracker and line.find(i) >= 0):
               first_occurance_tracker = line.find(i)
               first_number = i
           if(line[::-1].find(i[::-1]) < last_occurance_tracker and line[::-1].find(i[::-1]) >= 0):
               last_occurance_tracker = line[::-1].find(i[::-1])
               last_number = i
       first_occurance_tracker = 100
       last_occurance_tracker = 100
       match first_number:
           case 'one':
                first_number = '1'
           case 'two':
                first_number = '2'
           case 'three':
                first_number = '3'
           case 'four':
                first_number = '4'
           case 'five':
                first_number = '5'
           case 'six':
                first_number = '6'
           case 'seven':
                first_number = '7'
           case 'eight':
                first_number = '8'
           case 'nine':
                first_number = '9'
       match last_number:
           case 'one':
                last_number = '1'
           case 'two':
                last_number = '2'
           case 'three':
                last_number = '3'
           case 'four':
                last_number = '4'
           case 'five':
                last_number = '5'
           case 'six':
                last_number = '6'
           case 'seven':
                last_number = '7'
           case 'eight':
                last_number = '8'
           case 'nine':
                last_number = '9'
       sum = int (first_number + last_number) + sum
print(sum)
