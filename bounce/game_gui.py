#!/usr/bin/env python3
################################################################################
#   game_gui.py
#
#   Game view
#
#   26.09.2018  Created by:  rada
################################################################################
from tkinter import *
#from game import *

class GameGUI():
    def __init__(self, master, game):
        self.master = master
        
        # Default attributes
        self.master.title = "Отбей мячик"
#        self.master.winfo_toplevel().title("Отбей мячик")
        print(self.master.wm_title())
        self.master.geometry(self.center(master))
        self.master.attributes('-topmost', True)
        self.master.config(background='lightblue')

    # Widgets
    
    # Centers the window on the screen
    def center(self, master): 
        master_width  = 800
        master_height = 600
        
        screen_width    = master.winfo_screenwidth()
        screen_height  = master.winfo_screenheight()

        master_x = (screen_width  - master_width)/2
        master_y = (screen_height - master_height)/2
        return('%dx%d+%d+%d' % (master_width, master_height, master_x, master_y))
