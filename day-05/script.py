# Read input
file = open('input.txt', 'r')
lines: list[str] = file.readlines()
file.close()

# Get the number of stacks
number_of_stacks = int(len(lines[8]))

# Create all the stacks
stacks = [[] for x in range(9)]

# The first 7 lines of the input contains the stack info
#
# Iterate over the stacks in the input in reverse order.
# This is because if we built the stacks top down and called #append over #insert (like i did),
# we'd be building the arrays backwards.
for i in range(7, 0, -1):
  # Get and clean the line
  line = lines[i].replace("\n", "")

  # Loop through every 4 characters in the line
  # we'd get a create that look like this: `[B] `.
  # The first index contains the potential contents
  for j in range(0, len(line), 4):
    # The current stack is the current index divided by 4
    current_stack_index = j // 4
    crate = line[j:j+4]

    if crate[1] != ' ':
      stacks[current_stack_index].append(crate[1])
    
#print(stacks)

for i in range(10, len(lines)):
  instruction = lines[i].replace("\n", "")
  index_of_f = instruction.index(' f')

  amount_of_crates = int(instruction[5:index_of_f])
  to_stack_index = int(instruction[len(instruction) - 1]) - 1 # I'm not coding to account for double digit stacks

  index_of_m = instruction.index('m ') + 2
  from_stack_index = int(instruction[index_of_m]) - 1

  from_stack = stacks[from_stack_index]
  to_stack = stacks[to_stack_index]

  print(f"AoC: {amount_of_crates}, FS: {from_stack_index+1}, TS: {to_stack_index+1}, ")

  for _ in range(0, amount_of_crates):
    item = from_stack.pop()
    to_stack.append(item)

    # print(f"Item: {item}, FS: {from_stack_index + 1}, TS: {to_stack_index + 1}, AoC: {amount_of_crates}")
  
  print(stacks)



result = ''
for s in stacks:
  if len(s):
    result += s[len(s) - 1]
print(result)



