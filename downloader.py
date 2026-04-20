from pytubefix import YouTube
from pytubefix.cli import on_progress

async def download(url): #Загружаем видео с YouTube
    yt = YouTube(url, on_progress_callback= on_progress)
    print(f'Downloading "{yt.title}"')
    yd = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
    yd.download('downloaded', 'video.mp4')
