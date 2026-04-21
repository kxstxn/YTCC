from downloader import download
from cutter import cutter
import asyncio

async def main():
    url = input('Enter the link to the original video: ')
    try:
        download(url)
    except Exception:
        print('You probably entered an incorrect link.')
    try:
        cutter()
    except Exception as e:
        print(f'Еrror. Try Again {e}')
asyncio.run(main())