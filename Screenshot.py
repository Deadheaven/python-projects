import time
import pyautogui
import random
import tkinter as tk
def screenshot():

    name=f"{random.randint(1,1000)}.png"
    time.sleep(5)
    img=pyautogui.screenshot(name)
    img.show()



root=tk.Tk()
frame=tk.Frame(root)
frame.pack()

button=tk.Button(frame,text='Take Screenshot',command=screenshot)
button.pack(side=tk.LEFT)
close=tk.Button(frame,text='QUIT',command=quit)
close.pack(side=tk.LEFT)

root.mainloop()