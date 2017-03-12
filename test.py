import player
import os
import time
from playlist import getPlaylist
from Handling import Handler
from random import shuffle

arr = getPlaylist()
shuffle(arr)

test = player.player(arr)

h = Handler(test)

test.start()
time.sleep(5)

while(True):
    time.sleep(0.1)
    h.handle()
    if not test.is_playing() and test.playing:
        test.next()
        while not test.is_playing():
            time.sleep(5)
 
