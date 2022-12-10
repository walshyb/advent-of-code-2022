# Read input
file = open('input.txt', 'r')
lines = file.readlines()
file.close()

x_value, cycle = 1, 1
seen_cycles = set()
result = 0

# Screen will represent our CRT, which in for this problem,
# is 6 high and 40 wide. It's easier to maintain, imo,
# by just having a 1D array
screen = ['.' for x in range(0, 6 * 40)]
crt_position = 0

def update_signal():
    global result, crt_position
    # Every 40 cycles we update the signal strength (result)
    # This is to calculate part 1
    if (cycle - 20) % 40 == 0 and cycle not in seen_cycles:
        result += x_value * cycle
        # I keep track of cycles we've already
        # updated signal strength (result) for because
        # it's possible to call this function
        # multiple times during a instruction processing
        seen_cycles.add(cycle)
    
    # If the cycle (the CRT position) is in the range of
    # x_value (register X, or the sprite position per the
    # instructions), then we will draw a character on the screen
    #
    # We mod 40 here because we're dealing with a 1D array
    if (cycle % 40) - 1 in range(x_value-1, x_value+2):
        screen[cycle - 1] = '#'

# Handles parts 1 and 2
def solve():
    global cycle, x_value
    for line in lines:
        cleaned_line = line.replace("\n", "")
        instruction = cleaned_line.split(' ')[0]

        # Clock up
        update_signal()

        if instruction == 'noop':
            cycle += 1
            continue
        
        # Clock down
        update_signal()
        
        # Getting the value from the instruction is 1 clock cycle
        cycle += 1
        instruction_value = int(cleaned_line.split(' ')[1])

        # Clock up
        update_signal()

        cycle += 1
        x_value += instruction_value

        # Clock down
        update_signal()

    # Part 1
    print(result)

    # Print letters on the screen for
    # Part 2
    for i in range(0, 6 * 40):
        print(screen[i], end='')
        if (i + 1) % 40 == 0:
            print() 

solve()

# Part 2 Output
"""
####.#..#...##.####.###....##.####.####.
...#.#.#.....#.#....#..#....#.#.......#.
..#..##......#.###..###.....#.###....#..
.#...#.#.....#.#....#..#....#.#.....#..#
#....#.#..#..#.#....#..#.#..#.#....#....
####.#..#..##..#....###...##..#....####.
"""