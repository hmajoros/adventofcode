with open ("input.txt") as inputfile:
  input = inputfile.read()

left = input.count('(')
right = input.count(')')

print left - right
