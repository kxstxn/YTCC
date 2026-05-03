import customtkinter
from customtkinter import CTkFrame, CTkImage
from downloader_cutter import download_and_cut
import threading
import os
import subprocess
import shutil
import platform
from CTkMessagebox import CTkMessagebox
from PIL import Image
import webbrowser

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry('600x100')
        self.title('YTCC by @kxstxn')

        frame = CTkFrame(self, fg_color='transparent')
        frame.pack(pady=(10, 0), padx = 25, anchor = 'w')
        self.entry = customtkinter.CTkEntry(frame, placeholder_text='Enter link to original video', height= 30, width= 300)
        self.entry.pack(side = 'left')
        self.lenght = customtkinter.CTkEntry(frame,placeholder_text= 'Enter lenght', height= 30, width = 100)
        self.lenght.pack(side = 'left', padx = 10)
        self.cut_button = customtkinter.CTkButton(frame, text='Start cutting', fg_color='green', hover_color='darkgreen', command=self.cut_button_call)
        self.cut_button.pack(side='left')


        folder_command = CTkFrame(self, fg_color= 'transparent')
        folder_command.pack(pady = (10, 0), padx = 25, anchor = 'w')
        self.gitlogo = customtkinter.CTkImage(dark_image=Image.open('Octicons-mark-github.png'), light_image=Image.open('Octicons-mark-github.png'), size=(20,20))
        self.open_button = customtkinter.CTkButton(folder_command, text='Open work folder', command= self.open_folder)
        self.open_button.pack(side= 'left')
        self.clear_button = customtkinter.CTkButton(folder_command, text= 'Clear work folder', command = self.clear_folder)
        self.clear_button.pack(side = "left", padx = 10)
        self.git_button = customtkinter.CTkButton(folder_command, image = self.gitlogo, text = 'GitHub', width=70, fg_color='white', text_color='black', hover_color= 'gray', command= self.open_git)
        self.git_button.pack(side = 'right')

    def open_git(self):
        webbrowser.open('https://github.com/kxstxn/YTCC')

    def open_folder(self):
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

    def clear_folder(self):
        shutil.rmtree('downloaded')
        shutil.rmtree('clipped')
        os.mkdir('downloaded')
        os.mkdir('clipped')

    def cut_button_call(self):
        link = self.entry.get()
        lncut = self.lenght.get()
        if link == '' or lncut == '':
                CTkMessagebox(title= 'Error', message = 'All fields must be filled in, please try again.')
        else:
            self.cut_button.configure(state = 'disabled', text = 'Processing...')
            thread = threading.Thread(target = self.run_process, args = (link, int(lncut)), daemon = True)
            thread.start()

    def run_process(self, link, lncut):
        try:
            download_and_cut(link, lncut)
        finally:
            self.cut_button.configure(state = 'normal', text= 'Start cutting')
app = App()
app.mainloop()