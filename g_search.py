import google

def getUrl(q, site, source=1):
    query = q + ' site:' + site
    result = google.search(query)
    try:
        URL1 = next(result)
        if source == 1:
            return URL1
        else:
            URL2 = next(result)
            return URL2
    except:
        print("None")
        return None
