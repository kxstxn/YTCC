import platform
import subprocess
from moviepy import VideoFileClip
from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
import subprocess
import platform

async def cut(url):
    print('Start create clips')
    clip_num = 1 #Порядковый номер клипа
    start = 0 #Начальная точка клипа
    lncut = int(input('Enter the clip length in seconds: '))
    end = lncut #Конечная тока клипа
    video_len = YouTube(url, on_progress_callback= on_progress).length #Определяем длинну исходного видеоролика
    if os.path.isdir('clipped'): #Проверяем существует ли дирректория + создаём если ее нет
        pass
    else:
        os.mkdir('clipped')
    if end < video_len:
        while end <= video_len: #Нарезаем оригинальное видео на клипы
            clip = VideoFileClip('downloaded/video.mp4').subclipped(start, end)
            clip.write_videofile(f'clipped/clip{str(clip_num)}.mp4') #Сохраняем каждый клип в заданную дирректорию
            start += lncut
            end += lncut
            clip_num += 1
        print('The clips have been successfully generated!')
        path = 'clipped'
        if platform.system() == 'Windows':
            subprocess.Popen(['explorer', path])
        elif platform.system() == 'Darwin':
            subprocess.Popen(['open', path])
        else:
            subprocess.Popen(['xdg-open', path])
    else:
        print('The clip is longer than the video')


