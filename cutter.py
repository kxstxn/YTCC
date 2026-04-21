from moviepy import VideoFileClip
import os
import subprocess
import platform

def cut(url):
    video = VideoFileClip('downloaded/video.mp4')
    print('Start create clips')
    clip_num = 1 #Порядковый номер клипа
    start = 0 #Начальная точка клипа
    lncut = int(input('Enter the clip length in seconds: '))
    end = lncut #Конечная точка клипа
    video_len = int(video.duration)
    if os.path.isdir('clipped'): #Проверяем существует ли дирректория + создаём если ее нет
        pass
    else:
        os.mkdir('clipped')
    if lncut < video_len:
        while start < video_len:
            end = min(start + lncut, video_len) #Высчитываем конец клипа для некратных значений
            clip = video.subclipped(start, end)
            clip.write_videofile(f'clipped/clip{str(clip_num)}.mp4') #Сохраняем каждый клип в заданную дирректорию
            start += lncut
            clip_num += 1
        print('The clips have been successfully generated!')
        path = os.path.abspath('clipped')
        if platform.system() == 'Windows':
            subprocess.Popen(['explorer', path])
        elif platform.system() == 'Darwin':
            subprocess.Popen(['open', path])
        else:
            subprocess.Popen(['xdg-open', path])
    else:
        print('The clip is longer than the video')




