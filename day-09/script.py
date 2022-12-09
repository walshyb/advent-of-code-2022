# Read input
file = open('input.txt', 'r')
lines = file.readlines()
file.close()

# You can start at 0,0 too and this code works with that
# I just didn't want to debug with negative numbers
head_pos = (1000,1000)
tail_pos = (1000,1000)

visited_tail_pos = set()
visited_tail_pos.add(tail_pos)

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

for line in lines:
  direction, steps = line.replace("\n", '').split(' ')

  for i in range(0, int(steps)):
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