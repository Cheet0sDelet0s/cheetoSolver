import numpy as np
import cv2
import pyautogui
import os
import webbrowser
import time
import keyboard
import mouse
from io import BytesIO
import win32clipboard
import win32gui
import win32con
from PIL import Image

currentFilePath = os.path.realpath(__file__)
parentDirectory = os.path.dirname(currentFilePath)

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

#take screenshot
image = pyautogui.screenshot()

#convert to numpy array and bgr
image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)

#write to disk using opencv
cv2.imwrite("screenshot.png", image)

#cropping image
imageToBeEdited = cv2.imread(os.path.join(parentDirectory, "screenshot.png"))

#cropping parameters
x=320
y=285
w=1610
h=965
cropImage = image[y:h, x:w]
# -- show the output in a new window-- cv2.imshow("Cropped", cropImage)

#write cropped image to disk
cv2.imwrite("screenshot.png", cropImage)
cv2.waitKey(0)

toplist = []
winlist = []

def enumHandler(hwnd, lParam):
   if '- Google Chrome' in win32gui.GetWindowText(hwnd) and not "Sparx" in win32gui.GetWindowText(hwnd):
      win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

win32gui.EnumWindows(enumHandler, None)

#open bing AI
webbrowser.open("https://www.bing.com/chat", new=1)
time.sleep(4)
print("typing")
keyboard.write("solve this problem. make sure to read the text very carefully and give the most precise answer you can.")
mouse.drag(245, 1000, 245, 1000, absolute=True, duration=0)

imageFilePath = "screenshot.png"
image = Image.open(imageFilePath)

output = BytesIO()
image.convert("RGB").save(output, "BMP")
data = output.getvalue()[14:]

output.close()

#add image to clipboard
send_to_clipboard(win32clipboard.CF_DIB, data)

time.sleep(1)

#paste image and send prompt
keyboard.send("control+v")
time.sleep(3)
keyboard.send("enter")