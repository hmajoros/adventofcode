import hashlib

secret = 'yzbqklnj'
i = 282749

while True:
  m = hashlib.md5()
  m.update(secret + str(i))
  if (m.hexdigest()[:6] == '000000'):
    print i
    break

  i += 1
