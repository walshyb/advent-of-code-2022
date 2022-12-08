from collections import defaultdict

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
    if item[2] == 's':
      continue
    
    ## Shouldn't get here
    continue


  # Else we have a file
  # Doesn't matter what the file name is
  current.size += int(item.split(' ')[0])


# dfs dfs dfs dfs dfs dfs dfs
# WOOOO
to_find = [head]
already_seen = []

while to_find:
  current_node = to_find.pop()

  if current_node in already_seen:
    continue

  already_seen.append(current)

  for subdir_name in current_node.subdirs:
    subdir = current_node.subdirs[subdir_name]
    to_find.append(subdir)
    current_node.size += subdir.size


# sum of all dirs's sizes who's size is over 100000
sum = 0

to_find = [head]
already_seen = []

# If I knew how to backtrack properly I wouldn't have to DFS twice :(
while to_find:
  current_node = to_find.pop()

  if current_node in already_seen:
    continue

  already_seen.append(current_node)

  for subdir_name in current_node.subdirs:
    subdir = current_node.subdirs[subdir_name]
    to_find.append(subdir)
  
    print(f"{subdir.path} size: {subdir.size}")