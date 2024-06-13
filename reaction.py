import pyautogui
from pynput.mouse import Button, Controller
import keyboard
m = Controller()
keyboard.wait('ctrl+z')
region = (300, 500, 100, 100)
m.position = (300, 500)
m.click(Button.left, 1)
prev = pyautogui.screenshot()
while not keyboard.is_pressed('ctrl+q'):
    current = pyautogui.screenshot()
    if not current == prev:
        m.position = (300, 500)
        m.click(Button.left, 2)
    prev = current
        
        
