def getPlaylist(file):
    
    file = open(file, 'r')
    temp = file.readlines()
    arr = []
    
    for a in temp:
        arr.append(a[:-1])

    return arr

