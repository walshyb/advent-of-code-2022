# Read input
file = open('input.txt', 'r')
lines: list[str] = file.readlines()
file.close()

## Part 1

# Types as in Pokemon types
# Really a supereffective chart
type_chart = {
  'Rock': {
    'beats': 'Scissors',
    'value': 1 
  },
  'Paper': {
    'beats': 'Rock',
    'value': 2
  },
  'Scissors': {
    'beats': 'Paper',
    'value': 3
  }
}

shape_map = {
  'A': 'Rock',
  'B': 'Paper',
  'C': 'Scissors',
  'X': 'Rock',
  'Y': 'Paper',
  'Z': 'Scissors'
}

total_score = 0

for line in lines:
  opponent_option, my_option = line.replace("\n", "").split(" ") # ex. B Z

  oponent_shape = shape_map[opponent_option]
  my_shape = shape_map[my_option]

  # If we chose the same shape, it's a draw
  # Add shape value + points for draw (3)
  if my_shape == oponent_shape:
    total_score += type_chart[my_shape]['value'] + 3
    continue

  # If my shape beats my oponnents, we win
  # Add shape value + points for win (6)
  #
  # Else we lose,
  # Add shape value
  if type_chart[my_shape]['beats'] == oponent_shape:
    total_score += type_chart[my_shape]['value'] + 6
  else:
    total_score += type_chart[my_shape]['value']

print(f"Total Points: {total_score}")

## Part 2

total_score = 0

# If I need to lose, this is a dictionary
# to map the losing option to my opponent's selection
lose_map = {
  'Rock': 'Scissors',
  'Paper': 'Rock',
  'Scissors': 'Paper'
}

# If I need to win, this is a dictionary
# to map the win option to my opponent's selection
win_map = {
  'Rock': 'Paper',
  'Paper': 'Scissors',
  'Scissors': 'Rock'
}

point_values = {
  'Rock': 1,
  'Paper': 2,
  'Scissors': 3
}

for line in lines:
  opponent_option, task = line.replace("\n", "").split(" ") # ex. B Z

  oponent_shape = shape_map[opponent_option]
  
  # Lose condition
  if task == "X":
    total_score += point_values[lose_map[oponent_shape]]
    continue

  # Draw condition
  if task == "Y":
    total_score += point_values[oponent_shape] + 3
    continue

  # Win condition
  if task == "Z":
    total_score += point_values[win_map[oponent_shape]] + 6

print(f"Total score: {total_score}")