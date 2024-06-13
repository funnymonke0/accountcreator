import math
from pynput.mouse import Button, Controller
import keyboard
import time

keyboard.wait('ctrl+q')
center = (683, 388)

radius = 301
pi = math.pi
points = 360
step = 2*pi/points
m = Controller()
coords = []
angle = 0
for i in range (0, points):
   
    y = math.sin(angle)*radius
    x = math.cos(angle)*radius
    coords.append((x+center[0],y+center[1]))
    angle = angle+step
    

m.position = coords[0]
m.press(Button.left)
for coord in coords:
    m.position = coord
    time.sleep(0.01)

m.release(Button.left)