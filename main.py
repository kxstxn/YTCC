from downloader import download
from cutter import cutter
import asyncio

async def main():
    url = input('Enter the link to the original video: ')
    try:
        await download(url)
    except Exception:
        print('You probably entered an incorrect link.')
    try:
        await cutter()
    except Exception:
        print('Еrror. Try Again')
asyncio.run(main())