import sys
import time

map = [
        [1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 2, 1]
]

def ShowMap():
 print()
 for row in map:
  for item in row:
   print(item, end="")
  print()

def action(x, y):
  if (map [y][x] == 2):
    print("exit found")
    sys.exit()
  if (map [y][x] == 0):
    map[y][x] ="*"
    ShowMap()
    time.sleep(1)
    AI(x,y)

def AI(x, y):
 ShowMap()
 action(x-1, y)
 action(x+1, y)
 action(x, y-1)
 action(x, y+1)

AI(1,1)
