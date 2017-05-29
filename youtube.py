import pafy
import g_search

def audioStream(query, src):
    url = g_search.getUrl(query, 'youtube.com', source=src)
    return getAudioURL(url)

def getAudioURL(url):
    video = pafy.new(url)
    audio = video.getbestaudio()
    return audio.url
