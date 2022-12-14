from functools import cmp_to_key

# Read input
file = open('input.txt', 'r')
lines = file.readlines()
file.close()

packets = []

def part1_setup():
  for i in range(1, len(lines)):
    if lines[i] == "\n" or lines[i-1] == "\n":
      continue

    left_packet = eval(lines[i - 1].strip())
    right_packet = eval(lines[i].strip())

    packets.append((left_packet, right_packet))
part1_setup()

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

def part1():
  correct_packets = 0
  for index, packet in enumerate(packets):
    left_packet, right_packet = packet

    if (len(left_packet) == 0 and len(right_packet)) or check_list(left_packet, right_packet):
      correct_packets += index + 1

  print(correct_packets)

part1()

packets = []

def part2_setup():
  for line in lines:
    if line.strip():
      packets.append(eval(line.strip()))
part2_setup()

def part2():
  # Add two new packets, per part 2
  packets.append([[2]])
  packets.append([[6]])

  # Simple func to get the first item in a nested list
  def shallow_dive(packet):
    if type(packet) == int:
      return packet
    
    if type(packet) == list and len(packet):
      return shallow_dive(packet[0])

    if type(packet) == list and not len(packet):
      return 0

  # Compare function to help us sort our packets
  def packet_compare(a, b):
    # Shallow dive to get the first item in each list
    a_start = shallow_dive(a)
    b_start = shallow_dive(b)

    # If the first item of each list is different, we don't have
    # to go through the rest of the lists
    if a_start < b_start:
      return -1
    elif b_start > a_start:
      return 1
    else:
      result = deep_dive(a,b)
      return result

  # Modified version of check_list from pt 1
  def deep_dive(left_list, right_list):
    if len(left_list) == 0 and len(right_list):
      return -1

    if len(left_list) and len(right_list) == 0:
      return 1

    # Go through our list
    for i in range(len(left_list)):
      left_value = left_list[i]

      try:
        right_value = right_list[i]
      except:
        # Left list bigger than right
        return 1

      # If both values are ints
      if type(left_value) == int and type(right_value) == int:
        if left_value < right_value:
          return -1
        elif left_value == right_value:
          continue
        else:
          return 1

      # If one value is an int, make it a list
      if type(left_value) == list and type(right_value) == int:
        right_value = [right_value]

      if type(left_value) == int and type(right_value) == list:
        left_value = [left_value]

      result = deep_dive(left_value, right_value)

      if result == 0:
        continue
      else:
        return result

    # If we went through the whole of the left list and there are still right values
    if len(right_list) > len(left_list):
      return -1

    return 0

  # Sort the packets
  packets.sort(key=cmp_to_key(packet_compare))

  # Calculate result
  # It's the product of the two indicies (plus one) of [[2]] and [[6]]
  result = 1
  for index, packet in enumerate(packets):
    if str(packet) == '[[2]]' or str(packet) == '[[6]]':
      result *= (index + 1)

  print(result)

part2()