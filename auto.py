import pyautogui
import time

comments = ['Hi', 'hello']

time.sleep(5)

for i in range(10):
    pyautogui.typewrite(comments[i%2])
    pyautogui.typewrite("\n")
    time.sleep(3)