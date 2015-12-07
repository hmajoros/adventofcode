import hashlib

secret = 'yzbqklnj'
i = 0

while True:
  m = hashlib.md5()
  m.update(secret + str(i))
  if (m.hexdigest()[:5] == '00000'):
    print i
    break

  i += 1
