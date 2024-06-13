import pyautogui
import cv2
import numpy as np
import time
import keyboard
from pynput.mouse import Button, Controller

m = Controller()
region = (0, 135, 1350, 485)
keyboard.wait('ctrl+z')

for i in range (0, 31):
    pyautogui.screenshot('img.jpg', region=region)
    img = cv2.imread('img.jpg')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blurred = cv2.blur(gray, (3, 3))

    detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 20, maxRadius = 70) 

    detected_circles = np.uint16(np.around(detected_circles)) 
    for pt in detected_circles[0, :]: 
        a, b = pt[0], pt[1]
        b = b + 135
        m.position = (a, b)
        m.click(Button.left)
        break
    time.sleep(0.032)