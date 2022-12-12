# Read input
file = open('input.txt', 'r')
lines = file.readlines()
file.close()

monkeys = {}
current_monkey_info = {}

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
    current_monkey_info['divide'] =  int(line.split(' ')[5].strip())
  
  if line.find('true') != -1:
    current_monkey_info['true'] = line.split(' ')[-1].strip()
  
  if line.find('false') != -1:
    current_monkey_info['false'] = line.split(' ')[-1].strip()

def part1():
  # For 20 rounds
  for i in range(0, 20):
    # For each monkey
    for j in range(0, len(monkeys)):
      current_monkey = monkeys[str(j)]
      #print(current_monkey)
      for k in range(0, len(current_monkey['items'])):
        old = current_monkey['items'][k]        # old worry level
        new = eval(current_monkey['operation']) # new worry level

        new_worry = new // 3
        if new_worry % current_monkey['divide'] == 0:
          monkeys[current_monkey['true']]['items'].append(new_worry)
        else:
          monkeys[current_monkey['false']]['items'].append(new_worry)
        
        current_monkey['inspections'] += 1
      
      current_monkey['items'] = []

  print(monkeys)

  # Get two most active monkeys
  most_inspections = second_most_inspections = monkeys['0']['inspections']

  for i in range(0, len(monkeys)):
    current = monkeys[str(i)]
    
    if current['inspections'] > most_inspections:
      second_most_inspections = most_inspections
      most_inspections = current['inspections']
      continue
  
    if current['inspections'] > second_most_inspections:
      second_most_inspections = current['inspections']

  print(most_inspections * second_most_inspections)

part1()