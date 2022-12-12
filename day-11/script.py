# Read input
file = open('input.txt', 'r')
lines = file.readlines()
file.close()

monkeys = {}
current_monkey_info = {}
global_divide = 1

# Parse input
for index, line in enumerate(lines):
  if line == "\n" or index == len(lines) - 1:
    current_monkey_info['inspections'] = 0
    monkeys[current_monkey_info['id']] = current_monkey_info
    current_monkey_info = {} 
  
  if line.find('Monkey') != -1:
    current_monkey_info['id'] = line.split(' ')[1].replace(":", "").strip()
  
  if line.find('Starting') != -1:
    current_monkey_info['items'] = [int(x) for x in line.split(': ')[1].split(', ')]
  
  if line.find('Operation') != -1:
    current_monkey_info['operation'] = line.split('= ')[1].strip()
  
  if line.find('Test: ') != -1:
    divide = int(line.split(' ')[5].strip())
    current_monkey_info['divide'] = divide 
    global_divide *= divide
  
  if line.find('true') != -1:
    current_monkey_info['true'] = line.split(' ')[-1].strip()
  
  if line.find('false') != -1:
    current_monkey_info['false'] = line.split(' ')[-1].strip()

#print(monkeys)
#print(global_divide)
def solve(rounds, divide_worry):
  # For 20 rounds
  for i in range(0, rounds):
    # For each monkey
    for j in range(0, len(monkeys)):

      current_monkey = monkeys[str(j)]

      for k in range(0, len(current_monkey['items'])):
        old = current_monkey['items'][k]        # old worry level, used in eval
        new = eval(current_monkey['operation']) # new worry level
        
        if divide_worry:
          new = new // 3

          if new % current_monkey['divide'] == 0:
            monkeys[current_monkey['true']]['items'].append(new)
          else:
            monkeys[current_monkey['false']]['items'].append(new)
        else:
          if new % current_monkey['divide'] == 0:
            monkeys[current_monkey['true']]['items'].append(new % global_divide)
          else:
            monkeys[current_monkey['false']]['items'].append(new % global_divide)
        
      current_monkey['inspections'] += len(current_monkey['items'])
      current_monkey['items'] = []

  # Get two most active monkeys
  most_inspections = second_most_inspections = 0

  for i in range(0, len(monkeys)):
    current = monkeys[str(i)]
    
    if current['inspections'] > most_inspections:
      second_most_inspections = most_inspections
      most_inspections = current['inspections']
      continue
  
    if current['inspections'] > second_most_inspections:
      second_most_inspections = current['inspections']

  print(most_inspections * second_most_inspections)

# solve(20, True) # Part 1
solve(10000, False) # Part 2