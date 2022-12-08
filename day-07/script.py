from collections import defaultdict
from copy import deepcopy 

# Read input
file = open('input.txt', 'r')
lines: list[str] = file.readlines()
file.close()

# You already know we're making a tree baby
# I 100000% really wanted an excuse to make one.
# But I really did try looking for a more efficient solution.
# The only other solutions I could think of involved hashmaps, really similar
# to the subdirs property that I have going on here. But managing that looked
# like it was going to be super annoying. So I figured a tree would just
# be more easy for me to code and visualize
#
# Other methods I could have done:
# Just hashmaps
# Some kind of once over method and keeping track of values. idk
# Flat tree (array)
class Node:
  def __init__(self, dir_name, parent):
    self.path = ''
    self.dir_name = dir_name
    self.parent = parent
    self.size = 0
    self.subdirs = {}

    if dir_name != '/' and parent:
      self.path = f"{parent.path}/{dir_name}"
  
  def add_subdir(self, dir_name):
    self.subdirs[dir_name] = Node(dir_name, self)
  
  def find_subdir(self, dir_name):
    return self.subdirs[dir_name]

head = current = Node('/', None)

# For each line
for index, line in enumerate(lines):
  if index == 0:
    continue 

  item = line.replace("\n", "")

  # We have a dir
  if item.split(' ')[0] == 'dir':
    current.add_subdir(item.split(' ')[1])
    continue
  
  # We have an instruction
  if item[0] == '$':
    # CD Instruction
    if item[2] == 'c':
      dir_name = item.split(' ')[2]

      if dir_name == '..':
        #print(f"update current from {current.dir_name} to {current.parent.dir_name}")
        current = current.parent
      else:
        #print(f"update current from {current.dir_name} to {current.find_subdir(dir_name).dir_name}")
        current = current.find_subdir(dir_name)

      continue
  
    # ls instruction, do nothing
    if item[2] == 'l':
      continue
    
    ## Shouldn't get here
    continue


  # Else we have a file
  # Doesn't matter what the file name is
  current.size += int(item.split(' ')[0])


# dfs dfs dfs dfs dfs dfs dfs
# WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# Go through tree and total up the sizes of each dir so their 
# sizes are accurate and include the size of their subdirs
to_find = [head]
already_seen = set()

while to_find:
  current_node = to_find.pop()
  parent = current_node.parent

  #print(f"{current_node.dir_name} {already_seen} {[x.dir_name for x in to_find]}")

  if current_node in already_seen:
    continue

  if len(current_node.subdirs) == 0: 
    parent.size += current_node.size
    already_seen.add(current_node)
    if parent.parent:
      to_find.append(parent.parent)
    continue

  all_seen = True

  for subdir_name in current_node.subdirs:
    subdir = current_node.subdirs[subdir_name]
    if subdir in already_seen:
      continue

    all_seen = False
    skip = False

    for x in to_find:
      if x.dir_name == subdir_name:
        skip = True
        break

    if not skip and subdir not in already_seen:
      to_find.append(subdir)

  # start backtracking i hope
  #if len(current_node.subdirs) == 0: 
  if all_seen:
    parent.size += current_node.size
    #parent.subdirs.pop(current_node.dir_name)
    already_seen.add(current_node)
    if parent.parent:
      to_find.append(parent)

total_size = head.size
print(f"Total size: {total_size}")

def part1():
  to_find = [head]
  sum = 0

  # If I knew how to backtrack properly I wouldn't have to DFS twice :(
  while to_find:
    current_node = to_find.pop()
    #print(f"Current Node: {current_node.path}, subdirs: {current_node.subdirs.keys()}, size: {current_node.size}")
    if current_node.size < 100000:
      sum += current_node.size

    for subdir_name in current_node.subdirs:
      subdir = current_node.subdirs[subdir_name]
      to_find.append(subdir)

  print(sum)

#part1()

def part2():
  to_find = [head]
  sizes = []

  while to_find:
    current_node = to_find.pop()
    sizes.append(current_node.size)

    for subdir_name in current_node.subdirs:
      subdir = current_node.subdirs[subdir_name]
      to_find.append(subdir)

  sizes.sort()

  print(sizes)
  free_space = 70000000 - total_size # 27919656
  for size in sizes:
    if size + free_space >= 30000000:
      print(size)
      break

part2()