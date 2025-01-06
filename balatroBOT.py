import pyautogui
import time
from pynput import keyboard

pause = True

def on_press(key):
    global pause
    try:
        if key == keyboard.Key.home:  
            pause = False  
        elif key == keyboard.Key.end:  
            pause = True  
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

while True:
    if not pause:  
        pyautogui.moveTo(178, 943)
        time.sleep(0.1)
        pyautogui.click(178, 943)
        time.sleep(0.1)
        pyautogui.click(178, 943)
        time.sleep(0.1)
        pyautogui.moveTo(950, 360)
        time.sleep(0.1)
        pyautogui.click(950, 360)
        time.sleep(0.1)
        pyautogui.moveTo(960, 824)
        time.sleep(0.1)
        pyautogui.click(960, 824)
        time.sleep(0.3)
        pyautogui.moveTo(1665, 885)
        time.sleep(3)
        pyautogui.click(1665, 885)
        time.sleep(3)
    else:
        time.sleep(0.1) 
