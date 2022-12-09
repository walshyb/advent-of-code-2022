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

  for line in lines:
    direction, steps = line.replace("\n", '').split(' ')

    for _ in range(0, int(steps)):
      last_head_pos = poses[0]
      # Save next head position
      new_head_pos = move(direction, poses[0])
      poses[0] = new_head_pos

      # This bit moves position 1 to be at the last head position, if applicable
      hx = new_head_pos[0]
      hy = new_head_pos[1]

      tx = poses[1][0]
      ty = poses[1][1]

      # print(f"New head pos: {new_head_pos}")

      if max(hx, tx) - min(hx, tx) > 1 or max(hy, ty) - min(hy, ty) > 1:
        # print(f'Moving 1 {poses[1]} to {last_head_pos}, hx: {hx}, tx: {tx}, {max(hx, tx) - min(hx, tx) > 1} or {max(hy, ty) - min(hy, ty) > 1}')
        temp = poses[1]
        poses[1] = last_head_pos
        last_head_pos = temp
        pass

      print_board(20, poses)
      print('=============')

      # Update the rest
      for index in range(2, len(poses)):
        hx = poses[index-1][0]
        hy = poses[index-1][1]

        tx = poses[index][0]
        ty = poses[index][1]

        if max(hx, tx) - min(hx, tx) > 1 or max(hy, ty) - min(hy, ty) > 1:
          # Column and row are different, go diaganol
          if abs(hx-tx) > 0 and abs(hy-ty) > 0:
            x_change = 1 if hx > tx else -1
            y_change = 1 if hy > ty else -1
            temp = poses[index]
            poses[index] = (poses[index][0] + x_change, poses[index][1] + y_change)
            last_head_pos = temp
            #print_board(20, poses)
          else:
            temp = poses[index]
            # else go to last position
            poses[index] = last_head_pos
            last_head_pos = temp 

          print_board(20, poses)
          print('===========')
        else:
          break
      visited_tail_pos.add(poses[9])
    print_board(20, poses)
    # print('=====================')
    print('next step ==================================')
      
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