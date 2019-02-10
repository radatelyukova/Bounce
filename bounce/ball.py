################################################################################
#   ball.py
#
#   Model: Ball
#
#   26.09.2018  Created by: rada
################################################################################

class Ball():
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = self.canvas.create_oval(10, 10, 25, 25, fill=color, outline=color)
        
        self.canvas.move(self.id, 245, 100)
             
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width  = self.canvas.winfo_width()
        self.hit_bottom    = False
        


#    def move(self):
#        self.canvas.move(self.id, self.x, self.y)