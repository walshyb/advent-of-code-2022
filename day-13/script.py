# Read input
file = open('input.txt', 'r')
lines = file.readlines()
file.close()

packets = []

for i in range(1, len(lines)):
  if lines[i] == "\n" or lines[i-1] == "\n":
    continue

  left_packet = eval(lines[i - 1].strip())
  right_packet = eval(lines[i].strip())

  packets.append((left_packet, right_packet))

# Ugly recursive loop xD
def check_list(left_list, right_list):
  # Break condition 1
  # Left loop ran out of items first, 
  # or right loop ran out first
  if len(left_list) == 0 and len(right_list):
    return 1
  elif len(right_list) == 0 and len(left_list):
    return 0
  
  # Go through our list
  for i in range(len(left_list)):
    left_value = left_list[i]

    # Right packet ran out of items first, bad
    try:
      right_value = right_list[i]
    except:
      return 0

    # If both values are ints
    if type(left_value) == int and type(right_value) == int:
      if left_value < right_value:
        return 1
      elif left_value == right_value:
        continue
      else:
        return 0

    # If one value is an int, make it a list
    if type(left_value) == list and type(right_value) == int:
      right_value = [right_value]

    if type(left_value) == int and type(right_value) == list:
      left_value = [left_value]

    result = check_list(left_value, right_value)

    if result == None:
      continue
    else:
      return result

  # If we went through the whole of the left list and there are still right values
  if len(right_list) > len(left_list):
    return 1

  return None


correct_packets = 0
for index, packet in enumerate(packets):
  left_packet, right_packet = packet

  if len(left_packet) == 0 and len(right_packet):
    correct_packets += index + 1
    continue

  if check_list(left_packet, right_packet):
    correct_packets += index + 1

print(correct_packets)
