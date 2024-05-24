import sys
import time
import keyboard

width = 10 
height = 10

x = width // 2
y = height // 2

snake = [(x, y)]

def draw():
  data = [" " for i in range(width*height)]
  
  for x, y in snake:
    data[x + y*width] = "O"

  for i in range(height):
    print("".join(data[i*width : (i+1)*width]))

def input():
  global x, y
  
  if keyboard.is_pressed("left"):
    x = x - 1
  if keyboard.is_pressed("right"):
    x = x + 1  
  if keyboard.is_pressed("up"):
    y = y - 1
  if keyboard.is_pressed("down"):
    y = y + 1
        
def logic():
  head = (x, y)
  snake.insert(0, head)
  snake.pop()

while True:
  draw()
  input()
  logic()
  time.sleep(0.1)

if __name__ == "__main__":
  cmd = ["cmd", "/k", sys.executable, "snake.py"]
  
  p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  
  out, err = p.communicate()
