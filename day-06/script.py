# Read input
file = open('input.txt', 'r')
line = file.readlines()[0]
file.close()

def solve(length_of_message: int):
  # Space: O(1) bc we always know it will have 4 or 14 characters
  queue = list(line[:length_of_message])
  local = []

  # O(n) time complexity or O(n * m) with m being message size
  for i in range(length_of_message, len(line)):
    # O(1) to convert array of constant size to set? I think? So constant time? Maybe O(m)
    if len(local) == length_of_message or len(set(queue)) == length_of_message:
      print(i)
      break

    if line[i] not in queue and line[i] not in local:
      local.append(line[i])
    else:
      local = []

    queue.pop(0)
    queue.append(line[i])

solve(4)
solve(14)