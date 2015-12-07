with open ("input.txt") as inputfile:
  input = inputfile.read()

floor = count = 0
for char in input:
  count += 1

  if char == '(':
    floor += 1
  else:
    floor -= 1

  if floor == -1:
    print count
    break 

