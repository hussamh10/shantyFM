import win32api
import time
import threading

class Key:
    def __init__(self, code):
        self.code = code
        self.down = False
        self.pressed = False
        self.released = False

    def getCode(self):
        return self.code

    def wasReleased(self):
        return self.released

    def resetReleased(self):
        self.released = False;

    def isReleased(self):
        self.down = ((win32api.GetKeyState(self.code) & (1 << 7)) != 0)
        if self.down == True:
            self.pressed = True
        else:
            if self.pressed == True:
                self.released = True
                self.pressed = False

class Handler:
    def __init__(self, observer):
        self.observer = observer
        self.keys = {"play/pause" : Key(0xB3), "stop" : Key(0xB2), "prev" : Key(0xB1), "next" : Key(0xB0)}

    def handle(self):
        for key in self.keys:
            self.keys[key].isReleased()
            if self.keys[key].wasReleased():
                self.notify(key)
                self.keys[key].resetReleased()

    def notify(self, event):
        self.observer.notify(event)


