# Read input
file = open('input.txt', 'r')
lines = file.readlines()
file.close()

x_value, cycle = 1, 1
seen_cycles = set()
result = 0

screen = ['.' for x in range(0, 6 * 40)]
crt_position = 0

def update_signal():
    global result, crt_position
    if (cycle - 20) % 40 == 0 and cycle not in seen_cycles:
        result += x_value * cycle
        seen_cycles.add(cycle)
    
    if cycle - 1 in range(x_value-1, x_value+2):
        print(cycle, cycle - 1, x_value)
        screen[cycle - 1] = '#'

def part1():
    global cycle, x_value
    for line in lines:
        cleaned_line = line.replace("\n", "")
        instruction = cleaned_line.split(' ')[0]

        update_signal()

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

    #print(result)
    #print(screen)
    for i in range(0, 6 * 40):
        print(screen[i], end='')
        if (i + 1) % 40 == 0:
            print() 

part1()