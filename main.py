import os
import platform
import subprocess
from downloader_cutter import download_and_cut

print (''' █████ █████ ███████████   █████████    █████████ 
░░███ ░░███ ░█░░░███░░░█  ███░░░░░███  ███░░░░░███
 ░░███ ███  ░   ░███  ░  ███     ░░░  ███     ░░░ 
  ░░█████       ░███    ░███         ░███         
   ░░███        ░███    ░███         ░███         
    ░███        ░███    ░░███     ███░░███     ███
    █████       █████    ░░█████████  ░░█████████ 
   ░░░░░       ░░░░░      ░░░░░░░░░    ░░░░░░░░░  
                                                  
                                                  
                                                  ''')
def main_menu():
    print("1) Start 🚀")
    print("2) Open folder 🗃️")
    a = int(input('\nEnter >>> '))
    if a == 2:
        try:
                path = os.path.abspath('clipped')
                if platform.system() == 'Windows':
                    subprocess.Popen(['explorer', path])
                elif platform.system() == 'Darwin':
                    subprocess.Popen(['open', path])
                else:
                    subprocess.Popen(['xdg-open', path])
        except Exception as e:
            print(f'Error: {e}')
    elif a == 1:
        main()
def main():
    url = input('Enter the link to the original video: ')
    try:
        download_and_cut(url)
    except Exception as e:
        print(f'Error: {e}')

main_menu()