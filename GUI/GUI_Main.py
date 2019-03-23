'''
Created on Mar 4, 2019

@author: justine
'''
import tkinter
from tkinter import *
from PIL import Image, ImageTk
from Lib.tkinter.font import BOLD
from Lib.tkinter.constants import BOTTOM
class GUI_Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect 4")
        image_path = "../images/main_logo.png"
        load = Image.open(image_path)
        self.render = ImageTk.PhotoImage(load)
        self.root.geometry("1100x750") #You want the size of the app to be 500x500
        self.root.resizable(0, 0) #Don't allow resizing in the x or y direction
        self.show_main_menu(self.render)
        self.root.mainloop()

    
    def show_main_menu(self, render):
        self.root.config(bg = "#32808c")
        img = tkinter.Label(self.root, image = self.render, bg = self.root['bg'])
        img.place(x=155,y=80)
        
        bottom = tkinter.Frame(master=self.root, width = "700", height = "350", bg = self.root['bg'])
        bottom.pack(side="bottom")
        bottom.place(y= 450, x = 400)
        #4d686d
        start_game_button = tkinter.Button(master=bottom, text="START GAME", font = ("Helvetica", 20, BOLD), height=2, width=18, bg="#39494c", fg="white")
        start_game_button.pack()
        
        scoreboard_button = tkinter.Button(master=bottom, text="SCOREBOARD", font = ("Helvetica", 20, BOLD), height=2, width=18, bg="#39494c", fg="white")
        scoreboard_button.pack(pady = 20)
    
#     def show_settings(self):
#         self.next = GUI_Multiplayer(self.root)
        
root = tkinter.Tk()
GUI_Main(root)