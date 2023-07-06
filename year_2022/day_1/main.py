currentTotal = 0
highestTotal = 0
currentValue = 0
total_list = []

with open('input.txt','r') as input_file:
    for line in input_file:
        if(line.strip() != ""):
            currentValue = int(line)
            currentTotal = currentValue + currentTotal
        else:
            if highestTotal < currentTotal:
                highestTotal = currentTotal
                total_list.append(currentTotal)
            currentTotal = 0

total_list.sort(reverse=True)

print(f"Part 1: {total_list[0]}")
print(f"Part 2: {sum(total_list[0:3])}")