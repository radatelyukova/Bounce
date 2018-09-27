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
        
        self.id = self.canvas.create_oval(10, 10, 25, 25, fill=color)