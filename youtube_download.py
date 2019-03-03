import os, time, glob, shutil
from pytube import YouTube
import moviepy.editor as mp

def downloadYouTube(videourl, path):
    try:
        yt = YouTube(videourl)
        yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if not os.path.exists(path):
            os.makedirs(path)
        yt.download(path, filename=str(round(time.time() * 1000)))
    except Exception as e:
        print("Erro ao baixar link: {}".format(videourl))
        print("[Error]: {}".format(e))

def convertMp3(video):
    try:
        clip = mp.VideoFileClip(video)
        clip.audio.write_audiofile("{}.{}".format(str(round(time.time() * 1000)), "mp3"))
    except Exception as e:
        print("Erro ao converter: {}".format(video))
        print("[Error]: {}".format(e))

def moveToDirectory():
    dst = "./songs_{}".format(str(round(time.time())))
    songs = glob.glob("./*.mp3")

    if(len(songs) == 0):
         return False

    try:
        os.makedirs(dst)
    except:
        print("Erro ao criar pasta")

    for s in songs:
        shutil.move(s, dst)

# Pega lista de vídeos e quebra em arrays
videos = input("Cole os links separado por vírgula: ")
videos = videos.split(",")

path_video = "./videos_{}".format(str(round(time.time())))
for video in videos:
    downloadYouTube(video, path_video)

videos = glob.glob(path_video + "/*.mp4")

# percorre vídeos e converte em música
for video in videos:
    print(video)
    convertMp3(video)

# Move músicas para um diretorio gerado
moveToDirectory()