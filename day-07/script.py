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

# Build a tree :)
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

      # Go up a dir
      if dir_name == '..':
        #print(f"update current from {current.dir_name} to {current.parent.dir_name}")
        current = current.parent
      else:
        # Else find existing dir
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


# okay this is named horribly
# already_seen will keep track of nodes who's size has been added to its parent's
already_seen = set()

# lets dfs our way through this baby!
# How this works is we find leaves in the tree, then adds the current node's value to its parent, then puts its 
# parent back at the top of the stack. Then we check for the current node if we've already gone through all the children.
# If so, we add the current node's value to its parent. Else, we go through all the children that we haven't visited yet
while to_find:
  # for quick references
  current_node = to_find.pop()
  parent = current_node.parent

  #print(f"{current_node.dir_name} {already_seen} {[x.dir_name for x in to_find]}")

  if current_node in already_seen:
    continue

  # leaf scenario
  if len(current_node.subdirs) == 0: 
    parent.size += current_node.size
    already_seen.add(current_node)
    if parent.parent:
      to_find.append(parent.parent)
    continue

  # Another poorly named variable
  # this flag marks whether we've visited all the current node's children yet already
  all_seen = True

  # Loop through the current node's children (the subdirectories)
  for subdir_name in current_node.subdirs:
    subdir = current_node.subdirs[subdir_name]

    # Skip if already visited
    if subdir in already_seen:
      continue

    # We get here if haven't visited this node
    # So we mark all_seen as False because we haven't visited all the children of this node yet
    all_seen = False
    skip = False

    # Dirty way to make sure I don't add duplicates on the stack
    for x in to_find:
      if x.dir_name == subdir_name:
        skip = True
        break

    # If this child is not already in the to_find stack add it to the stack
    if not skip:
      to_find.append(subdir)

  # If all the children have been visited
  # add the current value to the parent
  # And then visit the parent
  if all_seen:
    parent.size += current_node.size
    already_seen.add(current_node)
    if parent.parent:
      # to_find.append(parent.parent) works too?? this line is more work probably?
      to_find.append(parent)

total_size = head.size
print(f"Total size: {total_size}")

def part1():
  to_find = [head]
  sum = 0

  # If I knew how to backtrack properly I wouldn't have to DFS twice :(
  # Maybe two DFS is good?
  while to_find:
    current_node = to_find.pop()
    #print(f"Current Node: {current_node.path}, subdirs: {current_node.subdirs.keys()}, size: {current_node.size}")

    # Sum up nodes (dirs) who's size is less than this
    if current_node.size < 100000:
      sum += current_node.size

    for subdir_name in current_node.subdirs:
      subdir = current_node.subdirs[subdir_name]
      to_find.append(subdir)

  print(sum)

part1()

def part2():
  to_find = [head]
  sizes = []

  # Add all sizes to an array
  while to_find:
    current_node = to_find.pop()
    sizes.append(current_node.size)

    for subdir_name in current_node.subdirs:
      subdir = current_node.subdirs[subdir_name]
      to_find.append(subdir)

  # sort array
  sizes.sort()

  # calculate smallest dir we could delete that would give us at least 30000000 space 
  free_space = 70000000 - total_size # 27919656
  for size in sizes:
    if size + free_space >= 30000000:
      print(size)
      break

part2()