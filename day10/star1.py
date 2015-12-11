num = 3113322113

def split_string(s):
  last = s[0] 
  count = 1
  split = []

  for i in range(1, len(s)):
    digit = s[i]

    if digit == last:
      count += 1
    else:
      split.append(s[i - count : i])
      count = 1

    last = digit

  split.append(s[len(s) - count : len(s)])

  return split


for i in range(0, 40):
  split = split_string(str(num))

  num = ""
  for group in split:
    num += str(len(group)) + str(group[0])
    
print len(num)
