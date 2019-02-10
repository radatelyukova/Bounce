################################################################################
#   bounce.py
#
#   <Module Purpose>
#
#   26.09.2018  Created by: rada
################################################################################
from application import *
from my_lib.logbook import *

if __name__ == "__main__":
    Logbook.log('Game starts')
    
    app = Application()
    
    app.root.mainloop()
    
    Logbook.log('Game is over')