
import time
import pyautogui
import tkinter as tk

def take_screenshot():
    name = int(round(time.time() * 1000))
    name = 'C:/Users/abieg/Documents/Python-Skillup/screenshot-app/screenshot.images/{}.png'.format(name)
    time.sleep(5)
    screenshot = pyautogui.screenshot(name)
    screenshot.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text="Take Screenshot",
    command=take_screenshot
)

button.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    text="QUIT",
    command=quit
)
close.pack(side=tk.LEFT)

root.mainloop()
