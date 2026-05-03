from pytubefix import YouTube
from pytubefix.cli import on_progress
from moviepy import VideoFileClip
import os
import subprocess
import platform
import yt_dlp

def download_and_cut(url, lncut):#Загружаем видео с YouTube
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'downloaded/%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        title = ydl.prepare_filename(info)
        title_folder = info.get('title')

        ydl.download([url])

    cutter(title, title_folder, lncut)

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
def cutter(title, title_folder, lncut):
    video = VideoFileClip(f'{title}')
    video_len = int(video.duration)
    start = 0
    end = int(lncut)
    clip_num = 1
    if os.path.isdir('clipped'): #Проверяем существует ли дирректория + создаём если ее нет
        pass
    else:
        os.mkdir('clipped')
    if os.path.isdir(f'clipped/{title_folder}'):
        print('The video had already been cut earlier.')
        pass
    else:
        os.mkdir(f'clipped/{title_folder}')
        while start < video_len:
            cut_video(f'{title}', f'clipped/{title_folder}/{title_folder}_clip{str(clip_num)}.mp4', start, min(lncut, video_len - start))
            start += lncut
            clip_num += 1
        path = os.path.abspath('clipped')
        if platform.system() == 'Windows':
            subprocess.Popen(['explorer', path])
        elif platform.system() == 'Darwin':
            subprocess.Popen(['open', path])
        else:
            subprocess.Popen(['xdg-open', path])