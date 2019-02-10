################################################################################
#   logbook.py
#
#  Class Logbook for output
#
#   09.02.2019  Created by: rada
################################################################################
import time

class Logbook():
    def __init__(self):
        pass
        
    def log(msg):
        print(time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime(time.time())), msg)