import Handling
import os
import sys

class ob:
    def __init__(self):
        pass

    def notify(self, notif):
        print(notif)




o = ob()
h = Handling.Handler()
h.addObserver(o)

h.start()

while(True):
    try:
        pass
    except (KeyboardInterrupt, SystemExit):
        os._exit(1)
        print('exit')
