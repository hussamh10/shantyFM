import time
import msvcrt
from Song import Song
from NowPlaying import NowPlaying

def display(info, paused):
    import os
    os.system('cls')

    playlist = info['playlist']

    index = info['current']
    i = 0

    for s in playlist:
        if index == i:
            if paused :
                print ("||", s.title)
            else:
                print ("> ", s.title)

        else:
            print("  ", s.title)
        i+= 1

    print ('\n' + "- For adding new songs press the key ESC")

def main():
    exit = False
    first = True
    playing = NowPlaying()
    paused = False
    changed = True

    while not exit:
        
        if changed:
            display(playing.getInfo(), paused)
            changed = False

        if playing.hasSong():
            changed = playing.tick()

        if msvcrt.kbhit() and msvcrt.getch() == chr(32).encode():
            if paused:
                playing.play()
                paused = False
            else :
                playing.pause()
                paused = True
        
        if msvcrt.kbhit() and msvcrt.getch() == chr(27).encode():
            changed = True
            inp = input("Enter the song title: ")
            
            if (inp == ''):
                continue

            else:
                song = Song(artist = '', title = inp, album = '')
                playing.addSongs(song)
                if first:
                    playing.start()
                    first = False

main()
