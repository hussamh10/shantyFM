import time
import vlc
import youtube

class player():

    def __init__(self, playlist = []):
        self.playing = True
        self.playlist = playlist
        self.current = 0
        self.song = None
        self.is_skipping = False
        if playlist:
            self.song = playlist[self.current]
        self.vlc = None

    def toggle_mute(self):
        self.vlc.audio_toggle_mute()

    def start(self):
        print(self.song)
        try:
            url = youtube.audioStream(self.song, 1)
        except:
            try:
                print("Trying a different source")
                url = youtube.audioStream(self.song, 2)
            except:
                print("Sorry, there is  a Copyrights law on this song")
                return False
        if url:
            self.vlc = vlc.MediaPlayer(url)
            self.vlc.play()
            return True
        return False

    def addSong(self, song):
        self.playlist.append(song)

    def appendPlaylist(self, playlist):
        self.playlist += playlist

    def prevSong(self):
        self.current -= 1
        if self.current <= 0:
            self.current = self.playlist.__len__() - 1
        return self.playlist[self.current]

    def nextSong(self):
        self.current += 1
        if self.current >= self.playlist.__len__():
            self.current = 0
        return self.playlist[self.current]

    def is_playing(self):
        return self.vlc.is_playing()

    def toggle_pause(self):
        if self.playing:
            self.vlc.pause()
        else:
            self.vlc.play()
        self.playing = not self.playing
        if self.playing:
            print('playing')
        else:
            print('paused')

    def pause(self):
        print('pause')
        self.vlc.pause()

    def stop(self):
        print('stop')
        self.vlc.stop()

    def next(self):
        print('next')
        self.song = self.nextSong()
        try:
            p = self.start()
        except:
            #self.next()
            pass

    def prev(self):
        print('prev')
        self.vlc.stop()
        self.start()

    def notify(self, notif):
        if notif == 'stop':
            self.toggle_mute()

        if notif == 'play/pause':
            self.toggle_pause()

        if notif == 'next':
            self.is_skipping = True
            self.stop()
            self.next()

        if notif == 'prev':
            self.prev()

    def addSong(self, song):
        self.playlist.append(song)
