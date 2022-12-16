# Read input
file = open('input.txt', 'r')
lines = file.readlines()
file.close()

x_bounds = set()
y_bounds = set()
paths = []

# read input
for line in lines:
  cleaned = line.strip()
  numbers = cleaned.split(' -> ')

  paths.append(numbers)

  for index, number in enumerate(numbers):
    x_bounds.add(int(number.split(',')[1]))
    y_bounds.add(int(number.split(',')[0]))

# Make grid
min_x = min(x_bounds)
max_x = max(x_bounds)
min_y = min(y_bounds)
max_y = max(y_bounds)

x_diff = max_x - min_x 
y_diff = max_y - min_y

grid = [['.' for y in range(y_diff + 1)] for x in range(0, max_x + 1)]

print(y_bounds)
# populate grid with paths
for path in paths:
  for index, current_coord in enumerate(path):
    if index == len(path) - 1:
      break

    current_x = int(current_coord.split(',')[1])
    current_y = int(current_coord.split(',')[0]) - min_y

    next_x = int(path[index + 1].split(',')[1])
    next_y = int(path[index + 1].split(',')[0]) - min_y

    # Move y
    if current_x == next_x:
      if current_y > next_y:
        for y in range(current_y, next_y - 1, -1):
          grid[current_x][y] = '#'
        continue
      for y in range(current_y, next_y):
        grid[current_x][y] = '#'


    elif current_y == current_y:
      if current_x > next_x:
        for x in range(current_x, next_x - 1, -1):
          grid[x][current_y] = '#'
        continue

      for x in range(current_x, next_x):
        grid[x][current_y] = '#'


for i in range(0, 3):
  for j in range(0, len(grid)):
    temp = min_y + j
    print("   ", str(temp)[i], end="")
  print()
for i,g in enumerate(grid):
  print(i, end=" ")
  print(g)




  