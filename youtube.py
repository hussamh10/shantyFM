import pafy
import g_search

def audioStream(query):
    url = g_search.getUrl(query, 'youtube.com')
    return getAudioURL(url)

def getAudioURL(url):
    video = pafy.new(url)
    audio = video.getbestaudio()
    return audio.url
