# Read input
file = open('input.txt', 'r')
lines = file.readlines()
file.close()

x_value, cycle = 1, 1
seen_cycles = set()
result = 0

def update_signal():
    global result
    if (cycle - 20) % 40 == 0 and cycle not in seen_cycles:
        result += x_value * cycle
        seen_cycles.add(cycle)


for line in lines:
    cleaned_line = line.replace("\n", "")
    instruction = cleaned_line.split(' ')[0]
    
    if instruction == 'noop':
        cycle += 1
        continue
    
    update_signal()
    
    # Getting the value from the instruction is 1 clock cycle
    cycle += 1
    instruction_value = int(cleaned_line.split(' ')[1])

    update_signal()

    cycle += 1
    x_value += instruction_value


    update_signal()

print(result)