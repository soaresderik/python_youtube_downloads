import time
import os
import glob
from pytube import YouTube
import moviepy.editor as mp

def downloadYouTube(videourl, path):
    try:
        yt = YouTube(videourl)
        yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if not os.path.exists(path):
            os.makedirs(path)
        yt.download(path, filename=str(round(time.time() * 1000)))
    except:
        print("Erro ao baixar link: {}".format(videourl))

def convertMp3(video):
    try:
        clip = mp.VideoFileClip(video)
        clip.audio.write_audiofile("{}.{}".format(str(round(time.time() * 1000)), "mp3"))
    except:
        print("Erro ao converter: {}".format(video))


videos = input("Cole os links separado por vírgula: ")

videos = videos.split(",")

for video in videos:
    downloadYouTube(video, "./videos")

videos = glob.glob("./videos/*.mp4")

for video in videos:
    print(video)
    convertMp3(video)



# downloadYouTube('https://www.youtube.com/watch?v=ikYQSS5ejEw', './videos')
# convertMp3("./videos/Salve.mp4", "./music")
