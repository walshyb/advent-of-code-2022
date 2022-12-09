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

def part2():
  poses = [(1000,1000) for _ in range(0, 10)]

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

      print(f"New head pos: {new_head_pos}")

      if max(hx, tx) - min(hx, tx) > 1 or max(hy, ty) - min(hy, ty) > 1:
        print(f'Moving 1 {poses[1]} to {last_head_pos}, hx: {hx}, tx: {tx}, {max(hx, tx) - min(hx, tx) > 1} or {max(hy, ty) - min(hy, ty) > 1}')
        poses[1] = last_head_pos


      # Update the rest
      for index in range(2, len(poses)):
        hx = poses[index-1][0]
        hy = poses[index-1][1]

        tx = poses[index][0]
        ty = poses[index][1]

        # Here we want to move to the direction that will get us 1 space 
        # away from the previous position

        # Check top left and top right
        if hy - ty > 1:
          print(f'Moving {index} {poses[index]} to {(tx, ty + 1)}')
          poses[index] = (tx, ty + 1)
        elif ty - hy > 1:
          print(f'Moving {index} {poses[index]} to {(tx, ty - 1)}')
          poses[index] = (tx, ty - 1)

        # Check left and right
        if hy - ty > 1:
          print(f'Moving {index} {poses[index]} to {(tx, ty + 1)}')
          poses[index] = (tx, ty + 1)
        elif ty - hy > 1:
          print(f'Moving {index} {poses[index]} to {(tx, ty - 1)}')
          poses[index] = (tx, ty - 1)

        # Check up and down
        if hx - tx > 1:
          print(f'Moving {index} {poses[index]} to {(tx + 1, ty)}')
          poses[index] = (tx + 1, ty)
        elif tx - hx > 1:
          print(f'Moving {index} {poses[index]} to {(tx - 1, ty)}')
          poses[index] = (tx - 1, ty)

        visited_tail_pos.add(poses[9])
    print('next step ===================================================')
      
  print(len(visited_tail_pos))

part2()