with open ("input.txt") as inputfile:
  input = inputfile.readlines()


total = 0
for line in input:
  sides = line.replace('\n', '').split('x')
  sides = [int(x) for x in sides]

  # sort list numerically
  sides.sort()

  total += 2 * (sides[0] + sides[1])
  
  # total amount for ribbon 
  total += sides[0] * sides[1] * sides[2]

print total
