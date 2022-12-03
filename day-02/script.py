# Read input
file = open('input.txt', 'r')
lines: list[str] = file.readlines()
file.close()

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
  openent_option, my_option = line.replace("\n", "").split(" ") # ex. B Z

  oponent_shape = shape_map[openent_option]
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