try:
  f = open("filename.txt")
  print(f.read())
  print(1 / 0)
finally:
  f.close()