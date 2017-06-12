import player
import os
import sys
import time
import threading
from playlist import getPlaylist
from Handling import Handler
from random import shuffle


def playPlaylist(file):
    """
        File is a playlist file of extension .plt
        Contains the name of the songs
        The playlist is always shuffled
    """
    arr = getPlaylist(file)
    shuffle(arr)

    test = player.player(arr)

    play(test)

    h = Handler(test)

    test.start()
    time.sleep(5)

    while(True):
        time.sleep(0.1)
        h.handle()
        if test.is_playing():
            test.is_skipping = False
        if not test.is_playing() and test.playing and not test.is_skipping:
            test.next()
            while not test.is_playing():
                time.sleep(5)


def play(test):
    h = Handler(test)

    test.start()
    time.sleep(5)

    while(True):
        time.sleep(0.1)
        h.handle()
        if test.is_playing():
            test.is_skipping = False
        if not test.is_playing() and test.playing and not test.is_skipping:
            test.next()
            while not test.is_playing():
                time.sleep(5)


def createPlaylist():
    """
        Gets the input of the song from the user to play
        runs the player in bg thread and takes more inputs and appends to playlist.
        No shuffle or loop
        When the playlist ends the player halts until a song name is provided
        TODO user can input playlist file name
    """

    playlist = []
    song = input()

    playlist.append(song)

    test = player.player(playlist)

    player_thread = threading.Thread(target=play, args=(test,))

    player_thread.start()

    quit_commands = ['e', 'q', 'quit', 'exit']

    while song not in quit_commands:
        song = input()
        test.addSong(song)


def main():
    file = sys.argv[-1] # playlist

    if sys.argv.__len__() < 2:
        createPlaylist()
    else:
        if file[:-3] == '.plt':
            playPlaylist(file)
        else:
            print("Incorrect file format, .plt file expected.")

main()
