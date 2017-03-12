import google

def getUrl(q, site):
    query = q + ' site:' + site
    result = google.search(query)
    try:
        URL = next(result)
        return URL
    except:
        print("None")
        return None

