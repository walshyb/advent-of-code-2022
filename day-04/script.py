# Read input
file = open('input.txt', 'r')
lines: list[str] = file.readlines()
file.close()

# Part 1

# Hopefully we don't have to know how we got part 1's answer for part 2

counter = 0
# O(n * n) => O(n*2)
for line in lines:
  cleaned_line = line.replace("\n", "")
  section1, section2 = cleaned_line.split(",") # ex. 2-4

  # Get the numbers from the input and convert to ints
  section1_start, section1_end = [int(x) for x in section1.split('-')]
  section2_start, section2_end = [int(x) for x in section2.split('-')]

  # O(4n) => O(n)
  # Check to see if one range is contained in the other.
  # Pretty darn inefficient
  if section1_start in range(section2_start, section2_end + 1) and section1_end in range(section2_start, section2_end + 1) or section2_start in range(section1_start, section1_end + 1) and section2_end in range(section1_start, section1_end + 1):
    counter += 1

print(counter)

# Part 2

counter = 0
# O(n * n) => O(n*2)
for line in lines:
  cleaned_line = line.replace("\n", "")
  section1, section2 = cleaned_line.split(",") # ex. 2-4

  # Get the numbers from the input and convert to ints
  section1_start, section1_end = [int(x) for x in section1.split('-')]
  section2_start, section2_end = [int(x) for x in section2.split('-')]

  # O(4n) => O(n)
  # Check to see if one range is contained in the other.
  # Pretty darn inefficient
  if section1_start in range(section2_start, section2_end + 1) or section1_end in range(section2_start, section2_end + 1) or section2_start in range(section1_start, section1_end + 1) or section2_end in range(section1_start, section1_end + 1):
    counter += 1

print(counter)