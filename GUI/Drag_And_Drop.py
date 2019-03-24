#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
try:
    # Tkinter for Python 2.xx
    import Tkinter as tk
except ImportError:
    # Tkinter for Python 3.xx
    import tkinter as tk
 
APP_TITLE = "Drag & Drop Tk Canvas Images"
APP_XPOS = 100
APP_YPOS = 100
APP_WIDTH = 300
APP_HEIGHT = 200
 
IMAGE_PATH = "../images/"
 
class CreateCanvasObject(object):
    def __init__(self, canvas, image, xpos, ypos):
        self.canvas = canvas
        self.image = image
        self.xpos, self.ypos = xpos, ypos
 
        self.image_obj= canvas.create_image(
            xpos, ypos, image=self.image)
         
        canvas.tag_bind(self.image_obj, '<Button1-Motion>', self.move)
        canvas.tag_bind(self.image_obj, '<ButtonRelease-1>', self.release)
        self.move_flag = False
         
    def move(self, event):
        if self.move_flag:
            new_xpos, new_ypos = event.x, event.y
             
            self.canvas.move(self.image_obj,
                new_xpos-self.mouse_xpos ,new_ypos-self.mouse_ypos)
             
            self.mouse_xpos = new_xpos
            self.mouse_ypos = new_ypos
        else:
            self.move_flag = True
            self.canvas.tag_raise(self.image_obj)
            self.mouse_xpos = event.x
            self.mouse_ypos = event.y
 
    def release(self, event):
        self.move_flag = False