import time
from Song import Song
import vlc
from youtube import youtube

class player():
    
    def __init__(self):
        self.song = 0
        self.paused = False
        self.start_time = 0
        self.pause_time = 0
        self.duration = 0
        self.YT = youtube()
        pass

    def start(self, song):
        self.current_time = 0
        self.pause_start = 0
        self.pause_time = 0
        self.paused = False
        url = self.YT.audioStream(song.artist, song.title)
        self.duration = self.YT.getDuration()
        self.start_time = time.time()
        self.song = vlc.MediaPlayer(url)
        self.song.play()
        return self.duration

    def play(self):
        if not self.paused:
            return
        self.pause_time += self.pause_start - time.time()
        self.paused = False
        self.song.play()

    def pause(self):
        if self.paused:
            return
        self.paused = True
        self.pause_start = time.time()
        self.song.pause()

    def stop(self):
        self.song.stop()
        self.current_time = 0
        self.song = 0
        self.paused = False
        self.start_time = 0
        self.pause_time = 0
        self.duration = 0

    def songEnded(self):
        time_passed = abs(self.start_time - self.pause_time - time.time())
        if not self.paused :
            self.current_time = time_passed
        if self.current_time > self.duration and self.duration > 0:
            return True
        return False






