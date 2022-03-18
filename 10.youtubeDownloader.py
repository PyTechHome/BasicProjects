#install pytube library
from pytube import YouTube
import os

#where to save the file
savePath='E:/'

#get the link and check for correctness
try:
    link=input("Enter the link: ")
    yt=YouTube(link)
except:
    print("Connection Error")

#information about the video
print("Title: ", yt.title)

dlVideo=yt.streams.filter(res="480p", file_extension='mp4').first()

try:
    print("Downloading...")
    dlVideo.download(savePath)
    print("Download completed!!")
except:
    print("Error!")
