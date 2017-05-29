import player
import os
import sys
import time
from playlist import getPlaylist
from Handling import Handler
from random import shuffle

file = sys.argv[-1]

arr = getPlaylist(file)
shuffle(arr)

test = player.player(arr)

h = Handler(test)

test.start()
time.sleep(5)

while(True):
    time.sleep(0.1)
    h.handle()
    if not test.is_playing() and test.playing:
        if not test.is_skipping:
            test.next()
        while not test.is_playing():
            time.sleep(5)
