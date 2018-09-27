#!/usr/bin/env python3
################################################################################
#   applicaition.py
#
#   This module initializes and runs the App
#
#   26.09.2018  Created by:  rada
################################################################################
from game     import *
from game_gui import *

class Application:
  def __init__(self):
    self.game = Game()
    self.root = Tk()
    self.gui  = GameGUI(self.root, self.game)
