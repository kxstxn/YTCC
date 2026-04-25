from pytubefix import YouTube
from pytubefix.cli import on_progress
from moviepy import VideoFileClip
import os
import subprocess
import platform

def download_and_cut(url):#Загружаем видео с YouTube
    yt = YouTube(url, on_progress_callback= on_progress)
    print(f'Downloading "{yt.title}"')
    yd = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
    yd.download(f'downloaded', f'{yt.title}.mp4')
    cutter(yt.title)

def cut_video(input_file, output_file, start_time, duration):
    command = [
        'ffmpeg',
        '-ss', str(start_time),
        '-i', input_file,
        '-t', str(duration),
        '-c', 'copy',
        output_file
    ]
    subprocess.run(command)
def cutter(title):
    lncut = int(input('Enter the clip length in seconds: '))
    video = VideoFileClip(f'downloaded/{title}.mp4')
    video_len = int(video.duration)
    start = 0
    end = int(lncut)
    clip_num = 1
    if os.path.isdir('clipped'): #Проверяем существует ли дирректория + создаём если ее нет
        pass
    else:
        os.mkdir('clipped')
    if os.path.isdir(f'clipped/{title}'):
        print('The video had already been cut earlier.')
        pass
    else:
        os.mkdir(f'clipped/{title}')
        while start < video_len:
            cut_video(f'downloaded/{title}.mp4', f'clipped/{title}/{title}_clip{str(clip_num)}.mp4', start, min(lncut, video_len - start))
            start += lncut
            clip_num += 1
        path = os.path.abspath('clipped')
        if platform.system() == 'Windows':
            subprocess.Popen(['explorer', path])
        elif platform.system() == 'Darwin':
            subprocess.Popen(['open', path])
        else:
            subprocess.Popen(['xdg-open', path])