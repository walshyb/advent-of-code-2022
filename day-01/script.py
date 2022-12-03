# Read input
file = open('input.txt', 'r')
lines: list[str] = file.readlines()
file.close()

## Part 1

# We definitely don't need to store all the totals in an array
# Just keeping track of the highest in an array would suffice (and save space)
calorie_count_per_elf: list[int] = []
local_total: int = 0

# For each calorie
#
# O(n)
for calories in lines:
  # If line is a newline,
  # Add elf's total calories to array and reset local total
  if calories == '\n':
    calorie_count_per_elf.append(local_total)
    local_total = 0
    continue
  
  # Add local total until we hit newline
  local_total += int(calories)

# Sloppy, but account for the input not ending in a new line
calorie_count_per_elf.append(local_total)

# O(n)
print(f"Elf with highest number of calories: {max(calorie_count_per_elf)}")

## Part 2

# Good thing we saved the elves' calories in an array!
# Because we could have saved the highest 3 in variables 
# and kept track of them as we looped through the list,
# but no thank you.

highest_three = 0

print(sorted(calorie_count_per_elf))
# O(3 * n) => O(n)
for i in range(0,3):
  local_max = max(calorie_count_per_elf) # O(n)
  print(local_max)
  calorie_count_per_elf.remove(local_max) # O(n)
  highest_three += local_max
  

print(f"Highest three elves' calories: {highest_three}")