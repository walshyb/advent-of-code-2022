from collections import defaultdict

# Read input
file = open('input.txt', 'r')
lines: list[str] = file.readlines()
file.close()

priorities = defaultdict(int)

for line in lines:
  # Clean the line
  cleaned_line = line.replace("\n", "")

  # Get its breakpoint (half the length)
  break_point = len(cleaned_line) // 2

  # Split the strings in half into 2 varsw
  container1 = cleaned_line[:break_point]
  container2 = cleaned_line[break_point:]

  # Take the items in the first half and add them to a set
  already_seen = set(list(container1))
  
  # For all the characters in the second half of the string,
  # If we come across a character that's in the first half of the string,
  # Add it to our frequency dict. 
  # Then remove the seen item from the set, bc duplicates in the same string don't matter
  for char in container2: 
    if char in already_seen:
      priorities[char] += 1
      already_seen.remove(char)
  
total = 0

# For every letter in our frequency dict
for index, letter in enumerate(priorities):
  # Get the num of occurrences
  occurrences = priorities[letter]

  # Calculate the value
  # a is equivalent to 1, z is equivalent to 26
  # A is equivalent to 27
  value = ord(letter) - 38 if letter.isupper() else ord(letter) - 96

  total += (value * occurrences)

print(total)
