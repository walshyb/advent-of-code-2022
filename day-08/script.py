# Read input
file = open('input.txt', 'r')
lines = file.readlines()
file.close()

board = []

# Build our grid
for line in lines:
  cleaned_line = line.replace("\n", '')
  trees = [ int(x) for x in list(cleaned_line)]
  board.append(trees)

def part1():
  visible_trees = 0
  for i in range(0, len(board)):
    for j in range(0, len(board[0])):
      if i - 1 < 0 or i + 1 >= len(board) or j - 1 < 0 or j + 1 >= len(board[0]):
        visible_trees += 1
        continue
        
      #print(i, j)
      safe = 0
      # Check left
      for a in range(j - 1, -1, -1):
        if board[i][a] >= board[i][j]:
          safe += 1
          #print('a', (i,j), (i, a))
          break

      # Check right
      for a in range(j + 1, len(board[0])):
        if board[i][a] >= board[i][j]:
          #print('b', (i,j), (i, a))
          safe += 1
          break

      # check Up
      for a in range(i - 1, -1, -1):
        if board[a][j] >= board[i][j]:
          #print('c', (i,j), (a, j))
          safe += 1
          break

      # check down
      for a in range(i + 1, len(board[0])):
        if board[a][j] >= board[i][j]:
          #print('d', (i,j), (a, j))
          safe += 1
          break

      if safe < 4:
        visible_trees += 1

  print(visible_trees)

part1()

def part2():
  highest_scenic_score = 0

  for i in range(0, len(board)):
    for j in range(0, len(board[0])):
      if i - 1 < 0 or i + 1 >= len(board) or j - 1 < 0 or j + 1 >= len(board[0]):
        continue
        
      left_score = 0
      # Check left
      for a in range(j - 1, -1, -1):
        left_score += 1
        if board[i][a] >= board[i][j]:
          break
          
      # Check right
      right_score = 0
      for a in range(j + 1, len(board[0])):
        right_score += 1
        if board[i][a] >= board[i][j]:
          break

      # check Up
      up_score = 0
      for a in range(i - 1, -1, -1):
        up_score += 1
        if board[a][j] >= board[i][j]:
          break

      # check down
      down_score = 0
      for a in range(i + 1, len(board[0])):
        down_score += 1
        if board[a][j] >= board[i][j]:
          break

      local_score = up_score * down_score * left_score * right_score
      #print((i,j), up_score, down_score, left_score, right_score)
      highest_scenic_score = max(highest_scenic_score, local_score)

  print(highest_scenic_score)

part2()