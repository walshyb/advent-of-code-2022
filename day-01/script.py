# Read input
file = open('input.txt', 'r')
lines: list[str] = file.readlines()
file.close()

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

# O(n)
print(f"Elf with highest number of calories: {max(calorie_count_per_elf)}")
