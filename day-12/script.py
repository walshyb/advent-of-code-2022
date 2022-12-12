from collections import deque

# Read input
file = open('input.txt', 'r')
lines = file.readlines()
file.close()

# Process input
board = []
start_pos, end_pos = (0,0), (0,0)

# Make the board
for line in lines:
  row = list(line.strip())
  board.append(list(row))

  # Little hack to assist with checking neighbors when processing the board
  if 'S' in row: 
    start_pos = (len(board) - 1, row.index('S'))
    board[start_pos[0]][start_pos[1]] = 'a'

  if 'E' in row: 
    end_pos = (len(board) - 1, row.index('E'))
    board[end_pos[0]][end_pos[1]] = 'z'

# Helper to return None for out of bounds checks
def fetch(x, y):
  if x >= len(board) or x < 0 or y < 0 or y >= len(board[0]):
    return None
  return board[x][y]

# any_start param is for part 2
# that will make it so it tracks steps from any 'a' elevation and not just the start's
def solve(any_start):
  # Make a queue for our BFS (Breadth first search)
  queue = deque()
  queue.append((start_pos, 0))
  seen = set({(start_pos, 0)})

  # bfs bfs bfs 
  while queue:
    (x,y), steps = queue.popleft()

    # Get current character
    current_height = board[x][y]

    # If we're at the end, print the number of steps
    if (x,y) == end_pos:
      print(steps)
      break

    # Check which neighbors we can go to
    neighbors = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]

    # For every neighbor candidate
    for neighbor_pos in neighbors:
      neighbor_x, neighbor_y = neighbor_pos
      neighbor = fetch(neighbor_x, neighbor_y)

      # This is for part 2
      # This makes it so we can track the shortest path
      # from any elevation 'a' and not just the starting position
      step_increase = 1
      if any_start and current_height == 'a' and neighbor == 'a':
        step_increase = 0

      # Ignore if out of bounds or already seen
      if not neighbor or neighbor_pos in seen:
        continue

      # If the neighbor is 1 elevation higher, it's valid
      if ord(neighbor) - ord(current_height) == 1:
        queue.append(((neighbor_x, neighbor_y), steps + step_increase))
        seen.add(neighbor_pos)
      # If the neighbor is at max 2 levels lower, it's valid
      elif ord(current_height) - ord(neighbor) >= 0 and ord(current_height) - ord(neighbor) < 3: 
        queue.append(((neighbor_x, neighbor_y), steps + step_increase))
        seen.add(neighbor_pos)

solve(False)  # part 1
solve(True)   # part 2