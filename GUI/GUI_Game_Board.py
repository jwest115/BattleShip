'''
Created on Mar 22, 2019

@author: justine
'''
from tkinter import *
from PIL.FontFile import WIDTH
from Tools.scripts import highlight
from pip._vendor.msgpack.fallback import xrange
from PIL import Image, ImageTk
from BattleShip.Drag_And_Drop import CreateCanvasObject

class GUI_Game_Board:
    def __init__(self):
        self.window = Tk()
        self.window.title("Battle Ship")
        self.window.config(bg="#4ca8ba")
        self.window.geometry("1100x850") #You want the size of the app to be 500x500
        self.window.resizable(0, 0) #Don't allow resizing in the x or y direction
        self.left_canvas = Canvas(self.window, width = 200, height = 1100, highlightthickness = 0, bg = "#3f727c")
        self.left_canvas.place(x = 0, y = 0)
         
          
        self.image_path = "../images/aircraft carrier.png"
        self.load = Image.open(self.image_path)
        self.load = self.load.resize((90, 280), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.load)
        self.img = Label(self.left_canvas, image = self.render, bg = self.left_canvas['bg'])
        self.img.place(x=50,y=10)
          
        self.image_path2 = "../images/battleship.png"
        self.load2 = Image.open(self.image_path2)
        self.load2 = self.load2.resize((100, 260), Image.ANTIALIAS)
        self.render2 = ImageTk.PhotoImage(self.load2)
        self.img2 = Label(self.left_canvas, image = self.render2, bg = self.left_canvas['bg'])
        self.img2.place(x=5,y=340)
        
        self.image_path3 = "../images/submarine.png"
        self.load3 = Image.open(self.image_path3)
        self.load3 = self.load3.resize((120, 200), Image.ANTIALIAS)
        self.render3 = ImageTk.PhotoImage(self.load3)
        self.img3 = Label(self.left_canvas, image = self.render3, bg = self.left_canvas['bg'])
        self.img3.place(x=90,y=380)
        
        self.image_path4 = "../images/cruiser.png"
        self.load4 = Image.open(self.image_path4)
        self.load4 = self.load4.resize((100, 200), Image.ANTIALIAS)
        self.render4 = ImageTk.PhotoImage(self.load4)
        self.img4 = Label(self.left_canvas, image = self.render4, bg = self.left_canvas['bg'])
        self.img4.place(x=5,y=630)
         
        self.image_path5 = "../images/destroyer.png"
        self.load5 = Image.open(self.image_path5)
        self.load5 = self.load5.resize((45, 135), Image.ANTIALIAS)
        self.render5 = ImageTk.PhotoImage(self.load5)
        self.img5 = Label(self.left_canvas, image = self.render5, bg = self.left_canvas['bg'])
        self.img5.place(x=120,y=670)
      
        
        self.frame = Frame(self.window, width = 625, height = 675, bg="#3f727c", highlightthickness=1, highlightbackground="black")
        self.frame.place(x = 257.5, y = 150)

        self.canvas = Canvas(self.frame, width= 700, height = 500, bg="#3f727c", highlightthickness=1, highlightbackground="black")
        self.canvas.place(x = 20, y = 17)
        
#         self.top_canvas = Canvas(self.window, width= 1100, height = 850, bg=self.frame['bg'], highlightthickness=1, highlightbackground="black")
#         self.top_canvas.place(x=0, y=0)
#         self.image_1 = CreateCanvasObject(self.canvas, self.render5, 0, 0)
#         self.image_2 =CreateCanvasObject(self.canvas, self.render5, 200, 100)
#         self.canvas.pack()
#         self.canvas.grid(row=1, column=0, sticky='ew', columnspan=8, rowspan=8)
    
      # Add 9-by-8 buttons to the frame
        rows = 9
        columns = 8
#         buttons = [[Button() for j in xrange(columns)] for i in xrange(rows)]
#         buttons[i][j].
        for i in range(0, rows):
            for j in range(0, columns):
                b = Button(self.canvas, height = 4, width = 9, text=("%d,%d" % (i+1, j+1)), bg = self.canvas['bg'])
                b.grid(row=i, column=j)
        
        # TRYING TO DRAG AND DROP LOAD5 IN CreateCanvasObject 
#         self.image_path5 = "../images/destroyer.png"
#         self.load5 = Image.open(self.image_path5)
#         self.load5 = self.load5.resize((45, 135), Image.ANTIALIAS)
#         self.render5 = ImageTk.PhotoImage(self.load5)
#         self.img5 = Label(self.frame, image = self.render5, bg = self.frame['bg'])
#         self.img5.place(x=120,y=670)
# #         
#         self.image_path6 = "../images/Capture.JPG"
#         self.load6 = Image.open(self.image_path6)
#         self.load6 = self.load6.resize((100, 100), Image.ANTIALIAS)
#         self.render6 = ImageTk.PhotoImage(self.load6)
#         self.img6 = Label(self.frame, image = self.render6)
#         self.img6.place(x=0,y=0)
#         
#         im1 = CreateCanvasObject(self.frame, self.render5, 150, 150)
        
        self.window.mainloop()
board = GUI_Game_Board()