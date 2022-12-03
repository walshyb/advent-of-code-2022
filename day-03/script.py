from collections import defaultdict

# Read input
file = open('input.txt', 'r')
lines: list[str] = file.readlines()
file.close()

## Part 1
priorities = defaultdict(int)

# O(n*m)
for line in lines:
  # Clean the line
  cleaned_line = line.replace("\n", "")

  # Get its breakpoint (half the length)
  break_point = len(cleaned_line) // 2

  # Split the strings in half into 2 varsw
  container1 = cleaned_line[:break_point]
  container2 = cleaned_line[break_point:]

  # Take the items in the first half and add them to a set
  # O(n)
  already_seen = set(list(container1))
  
  # For all the characters in the second half of the string,
  # If we come across a character that's in the first half of the string,
  # Add it to our frequency dict. 
  # Then remove the seen item from the set, bc duplicates in the same string don't matter
  #
  # O(m)
  for char in container2: 
    if char in already_seen:
      priorities[char] += 1
      already_seen.remove(char)
  
total = 0

# For every letter in our frequency dict
# O(n)
for index, letter in enumerate(priorities):
  # Get the num of occurrences
  occurrences = priorities[letter]

  # Calculate the value
  # a is equivalent to 1, z is equivalent to 26
  # A is equivalent to 27
  value = ord(letter) - 38 if letter.isupper() else ord(letter) - 96

  total += (value * occurrences)

print(total)

## Part 2
groups = []
local_group = []

# Separate our lines into groups of three
# O(n)
for index, line in enumerate(lines):
  cleaned_line = line.replace("\n", "")
  local_group.append(cleaned_line)

  if (index + 1) % 3 == 0:
    groups.append(local_group)
    local_group = []

# Keep track of the number of badges found
badges: dict[str, int] = defaultdict(int)

# O(n*m), n being groups and m being the length of a container
# For every 3 contains (a group) in the groups list
for group in groups:
  # Keep track of the common characters amongst the 3 containers
  common_chars_amonst_group = defaultdict(int)

  # O(1 * m) => O(m)
  # For each container
  for container in group:
    # Keep track of the characters we've already seen
    # because we only want to keep track of each character once
    # for a given container
    local_seen = set()

    # O(m)
    # For each character in the container,
    # skip if we've already seen a given character,
    # else add it to the seen set and
    # increment it's frequency amongst the frequency dict we're keep across the 3 containers
    for char in container:
      if char in local_seen:
        continue
      
      local_seen.add(char)
      common_chars_amonst_group[char] += 1
  
  # O(m)
  # Now for each unique character amongst the 3 groups,
  # look for the character that has shown up 3 times.
  # That's our badge
  for char in common_chars_amonst_group:
    if common_chars_amonst_group[char] == 3:
      badges[char] += 1

total = 0
# For every letter in our frequency dict, badges
# O(n)
# note: this could have been a function bc the same code is used above
for index, letter in enumerate(badges):
  # Get the num of occurrences
  occurrences = badges[letter]

  # Calculate the value
  # a is equivalent to 1, z is equivalent to 26
  # A is equivalent to 27
  value = ord(letter) - 38 if letter.isupper() else ord(letter) - 96

  total += (value * occurrences)

print(total)
