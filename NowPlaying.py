from player import player
from Song import Song

class NowPlaying():

    def __init__(self):
        self.music_player = player()
        self.playlist = []
        self.size = len(self.playlist)
        self.current = 0
        
    def appendPlaylist(self, pl):
        for song in pl:
            self.playlist.append(song)
            self.size += 1
    
    def addSongs(self, song):
        self.playlist.append(song)
        self.size += 1

    def shuffle(self):
        pass

    def start(self):
        currentSong = self.playlist[self.current]
        self.music_player.start(currentSong)

    def play(self):
        self.music_player.play()

    def pause(self):
        self.music_player.pause()

    def stop(self):
        self.music_player.stop()

    def remove(song):
        pass

    def clear():
        self.playlist = []

    def next(self):
        self.stop()
        self.current+= 1
        if self.current >= self.size:
            self.current = 0
        self.start()

    def prev(self):
        self.stop()
        self.current-= 1
        if self.current <= -1:
            self.current = 0
        self.start()

    def tick(self):
        if self.music_player.songEnded():
            self.next()
            return True
        return False

    def hasSong(self):
        return self.playlist


    def getInfo(self):
        playing = {'current' : self.current,
                   'playlist' : self.playlist,
                   'length' : self.size}
        return playing

