from moviepy import VideoFileClip
import os
import subprocess
import platform

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

def cutter():
    lncut = int(input('Enter the clip length in seconds: '))
    video = VideoFileClip('downloaded/video.mp4')
    video_len = int(video.duration)
    start = 0
    end = int(lncut)
    clip_num = 1
    if os.path.isdir('clipped'): #Проверяем существует ли дирректория + создаём если ее нет
        pass
    else:
        os.mkdir('clipped')
    while start < video_len:
        end = min(start + lncut, video_len)
        cut_video('downloaded/video.mp4', f'clipped/clip{str(clip_num)}.mp4', start, end)
        start += lncut
        clip_num += 1
        path = os.path.abspath('clipped')
        if platform.system() == 'Windows':
            subprocess.Popen(['explorer', path])
        elif platform.system() == 'Darwin':
            subprocess.Popen(['open', path])
        else:
            subprocess.Popen(['xdg-open', path])