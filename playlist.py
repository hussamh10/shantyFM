def getPlaylist():
    
    file = open('rock', 'r')
    temp = file.readlines()
    arr = []
    
    for a in temp:
        arr.append(a[:-1])

    return arr

