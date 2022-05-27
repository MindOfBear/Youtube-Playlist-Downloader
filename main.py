from pytube import YouTube
from pytube import Playlist
import os
def createPlaylistDict():
    playlistDict = {}
    with open('playlist.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
                content = line.split(',')
                link = content[0]
                folderName = content[1].replace('\n','')
                playlistDict[link] = folderName
    return playlistDict
playlistDict = createPlaylistDict()
print("Welcome to Playlist Downloader!\nCreated by Nicolaescu Ovidiu-Constantin")
for key in playlistDict.keys():
    link = key
    folderName = playlistDict[key]
    playlist = Playlist(key)
    playlist.video_urls
    parentDir = os.getcwd()
    path = os.path.join(parentDir, folderName)
    count = 0
    print("Download has started!")
    for url in playlist:
        count+=1
        print("Item",count,"-", YouTube(url).title)
        YouTube(url).streams.filter(only_audio=True).first().download(path)
    print("\nPlaylist successfully downloaded!")
    print(count, "items downloaded!\n")
input("\nPress enter to exit! :)")
