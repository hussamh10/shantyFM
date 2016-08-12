import pafy
from urllib.parse import quote
import urllib.request
import os
from bs4 import BeautifulSoup

class youtube:

    def __init__(self):
        self.video = 0
        pass

    def audioStream(self, Artist, Song, Album=''):
        """ 
            gets the Artist's Album's Song's Audio url
        """
        string = Artist + ' ' + Song +  ' ' + Album
        url = self.search(string)
        return self.getAudioURL(url)

    def getAudioURL(self, url):
        self.video = pafy.new(url)
        audio = self.video.getbestaudio()
        return audio.url

    def getDuration(self):
        duration = self.video.duration
        duration = duration.split(':')
        duration = (360*int(duration[0])) + (60*int(duration[1])) + (int(duration[2]))
        return duration

    def search(self, string):
        """ 
            Returns three result urls for the search query
        """
        query = quote(string)
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        vid = soup.findAll(attrs={'class':'yt-uix-tile-link'})[0]
        url = 'https://www.youtube.com' + vid['href']
        return url
