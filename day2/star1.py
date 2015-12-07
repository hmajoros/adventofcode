with open ("input.txt") as inputfile:
  input = inputfile.readlines()


total = 0
for line in input:
  sides = line.replace('\n', '').split('x')
  sides = [int(x) for x in sides]

  # sort list numerically
  sides.sort()
  
  total += 2 * (sides[0] * sides[1])
  total += 2 * (sides[1] * sides[2])
  total += 2 * (sides[2] * sides[0])

  # total amount of slack
  total += sides[0] * sides[1]

print total
