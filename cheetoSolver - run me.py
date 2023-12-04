#this is just the UI of cheetoSolver. the actual macro bit is in a different file.

import tkinter as ttk
import sys
import os
import win32gui
import win32con
from PIL import ImageTk, Image

def wquit():
    print("quit")
    exit()

def buildLabel(name, text, font, fontsize, foreground, padx, pady):
    label = ttk.Label(
        window,
        text=(text),
        font=(font, fontsize),
        foreground=(foreground),
        background=bgcolor
        )

    label.pack(ipadx=padx, ipady=pady)

def buildFrame(contain, height, width):
    frame = ttk.Frame(
    container=contain,
    height=height,
    width=width
    )


def buildButton(name, text, font, fontsize, foreground, padx, pady, expand, command):
    button = ttk.Button(
        window,
        text=(text),
        font=(font, fontsize),
        foreground=(foreground),
        background=bgcolor,
        command=command
        )

    button.pack(ipadx=padx, ipady=pady, expand=expand)

def launch():
    minimizeWindow("cheetoSolver - sparx maths AI tool")
    os.system("cheetoSolverMacro.py")

def minimizeWindow(window_name):
    def windowEnumHandler(hwnd, top_windows):
        top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

    top_windows = []
    win32gui.EnumWindows(windowEnumHandler, top_windows)

    for i in top_windows:
        if window_name.lower() in i[1].lower():
            win32gui.ShowWindow(i[0], win32con.SW_MINIMIZE)

bgcolor = "light grey"

minimizeWindow("C:\WINDOWS\py.exe")

#build window

window = ttk.Tk()
window.title("cheetoSolver - sparx maths AI tool")
window.geometry("500x800+700+250")
window.resizable(False, False)
window.configure(bg=bgcolor)
window.attributes("-topmost", 1)
window.iconbitmap("./assets/logo.ico")

#build title and subtitle and frame
buildLabel("title", "cheetoSolver", "Berlin Sans FB", 30, "blue", 100, 10)
buildLabel("subtitle", "Sparx Maths AI Helper", "Berlin Sans FB", 20, "blue", 100, 10)

#create image
imPath = "./assets/banner.jpg"
img = ImageTk.PhotoImage(Image.open(imPath))

panel = ttk.Label(window, image = img)

panel.pack()

#buttons
buildButton("2gb button", "Solve", "Berlin Sans FB", 20, "orange", 30, 20, True, lambda: launch())

#checkbox
#checkbox = ttk.Checkbutton(window,
#                           text="Insert Text",
#                           command=lambda: Insert Function,                                
#                           background=bgcolor
#                           )
#checkbox.pack(ipadx=0,ipady=0)

#about
buildLabel("how to use", "this is a screenshotting macro thing.\nit takes a screenshot of the question,\ncrops it, and opens bing AI to solve it.", "Berlin Sans FB", 20, "orange", 10, 10)

#how to use
buildLabel("how to use", "make sure your Sparx Maths window is maximised with\nnothing blocking its way.\nif you have multiple monitors, make sure it is\non your primary one.", "Berlin Sans FB", 16, "orange", 10, 10)

#before using:
buildLabel("before using", "before using, log into Bing AI with a microsoft account\n on google chrome, and allow it to auto log-in.", "Berlin Sans FB", 15, "orange", 10, 10)

#build quit button
buildButton("quitbutton", "Quit", "Berlin Sans FB", 15, "red", 10, 10, True, lambda: wquit())

#run window

window.mainloop()