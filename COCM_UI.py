from tkinter import *
import tkinter as tk
from tkinter import messagebox

root = Tk()

theLabel = tk.Label(root,text = "Home Display")
theLabel.pack()
    

btn02 = Button(root)
btn02['text'] = "Accomadation"
btn02.pack()

btn01 = tk.Button(root,text = "Camp")
btn01.pack()

def CampMenu(e):

    frame = tk.Frame(root)
    frame.pack()
    btn = tk.Button(root,text = "StudentCamp")
    btn.pack()


btn01.bind("<Button-1>", CampMenu)

root.geometry("512x512")
root.title("COCM管理软件")

root.mainloop()

 