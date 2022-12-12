from collections import deque

# Read input
file = open('input.txt', 'r')
lines = file.readlines()
file.close()

# Process input
board = []
start_pos, end_pos = (0,0), (0,0)

for line in lines:
  row = list(line.strip())
  board.append(list(row))

  if 'S' in row: 
    start_pos = (len(board) - 1, row.index('S'))
    board[start_pos[0]][start_pos[1]] = 'a'

  if 'E' in row: 
    end_pos = (len(board) - 1, row.index('E'))
    board[end_pos[0]][end_pos[1]] = 'z'

# bfs bfs bfs 

def fetch(x, y):
  if x >= len(board) or x < 0 or y < 0 or y >= len(board[0]):
    return None
  return board[x][y]

queue = deque()
seen = set({(start_pos, 0)})

queue.append((start_pos, 0))

def solve(any_start):
  while queue:
    (x,y), steps = queue.popleft()
    current_height = board[x][y]

    if (x,y) == end_pos:
      print(steps)
      break

    neighbors = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]

    for neighbor_pos in neighbors:
      neighbor_x, neighbor_y = neighbor_pos
      neighbor = fetch(neighbor_x, neighbor_y)

      step_increase = 1

      if any_start and current_height == 'a' and neighbor == 'a':
        step_increase = 0

      if not neighbor or neighbor_pos in seen:
        continue

      # If the neighbor is 1 elevation higher, it's valid
      # If the neighbor is at max 2 levels lower, it's valid
      if ord(neighbor) - ord(current_height) == 1:
        queue.append(((neighbor_x, neighbor_y), steps + step_increase))
        seen.add(neighbor_pos)
      elif ord(current_height) - ord(neighbor) >= 0 and ord(current_height) - ord(neighbor) < 3: 
        queue.append(((neighbor_x, neighbor_y), steps + step_increase))
        seen.add(neighbor_pos)

#solve(False) # part 1
solve(True)   # part 2