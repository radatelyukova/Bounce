################################################################################
#   bounce.py
#
#   <Module Purpose>
#
#   26.09.2018  Created by: rada
################################################################################
import time
from application import *

if __name__ == "__main__":
    print(time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime(time.time())), 'Game starts')

    app = Application()
    
    app.root.mainloop()
    
    print(time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime(time.time())), 'Game is over')
