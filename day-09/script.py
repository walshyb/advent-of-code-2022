# Read input
file = open('input.txt', 'r')
lines = file.readlines()
file.close()

def move(direction, pos):
  pos1, pos2 = pos

  if direction == 'D':
    # Move down one step
    return (pos1 + 1, pos2)

  if direction == 'R':
    # Move right one step
    return (pos1, pos2 + 1)

  if direction == 'U':
    # Move up one step
    return (pos1 - 1, pos2)

  if direction == 'L':
    # Move left one step
    return (pos1, pos2 - 1)

def part1():
  # Starting positions
  # You can start at 0,0 too and this code works with that
  # I just didn't want to debug with negative numbers
  head_pos = (1000,1000)
  tail_pos = (1000,1000)

  visited_tail_pos = set()
  visited_tail_pos.add(tail_pos)

  for line in lines:
    direction, steps = line.replace("\n", '').split(' ')

    for _ in range(0, int(steps)):
      last_head_pos = head_pos
      head_pos = move(direction, head_pos)
      
      hx = head_pos[0]
      hy = head_pos[1]

      tx = tail_pos[0]
      ty = tail_pos[1]

      if max(hx, tx) - min(hx, tx) > 1 or max(hy, ty) - min(hy, ty) > 1:
        tail_pos = last_head_pos
        visited_tail_pos.add(tail_pos)
      
  print(len(visited_tail_pos))

#part1()

def print_board(board, p):
  for i in range(0, board):
    for j in range(0, board):
      char = '.'
      if (i,j) in p:
        char = p.index((i,j))
      if i == 10 and j == 10:
        char = 's'
      print(char,end="")
    print()

def part2():
  poses = [(10,10) for _ in range(0, 10)]

  visited_tail_pos = set()
  visited_tail_pos.add(poses[9])

  # for every step
  for line in lines:
    direction, steps = line.replace("\n", '').split(' ')

    # Move the head for each step
    for _ in range(0, int(steps)):
      # Save next head position
      poses[0] = move(direction, poses[0])

      # Update everything after this head move
      for index in range(1, len(poses)):
        hx = poses[index-1][0]
        hy = poses[index-1][1]

        tx = poses[index][0]
        ty = poses[index][1]

        x_change = 1 if hx > tx else -1
        y_change = 1 if hy > ty else -1

        # If the previous item is now more than 1 space away in any direction
        if max(hx, tx) - min(hx, tx) > 1 or max(hy, ty) - min(hy, ty) > 1:
          # If both column and row are different positions, go diaganol
          if abs(hx-tx) > 0 and abs(hy-ty) > 0:
            poses[index] = (poses[index][0] + x_change, poses[index][1] + y_change)
          else:
            # If the current item and the last item are in the same column or row now,
            # go up down, left or right
            if hx == tx:
              poses[index] = (poses[index][0], poses[index][1] + y_change)
            elif hy == ty:
              poses[index] = (poses[index][0] + x_change, poses[index][1])
        else:
          # We can end this loop because since this
          # item doesn't need to change position, neither does what follows
          break

      # Keep track of any updates to the tail
      visited_tail_pos.add(poses[9])
      
  print(len(visited_tail_pos))

  def print_tail_path():
    for i in range(0, 350):
      for j in range(0, 134):
        char = '.'
        if (i,j) in visited_tail_pos:
          char = '#'
        print(char,end="")
      print()
  # print_tail_path()

part2()

# 2658 too high
# 2567, 2568 too low