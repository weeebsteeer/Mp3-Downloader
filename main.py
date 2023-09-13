from pytube import *
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import os
from pathlib import Path
import threading

#To do fix progress bar add the ability to control a input box add a label so the window isnt titled tk.

def download(url,pb):
    def step(self,a,b,bytes_remaining): #progress bar and step function to display progress in %
        pb.step(bytes_remaining)
    streams = YouTube(url,on_progress_callback=step).streams
    audio_streams = streams.filter(only_audio=True).order_by("abr").desc().first().download() #Grabs the audio stream and downloads the highest kbps#
    streams.download(output_path=output_path)


def thread_download(url,pb):
    T1 = threading.Thread(target=download,args=(url,pb)).start()



#The main window displaying input button and download bar
if __name__ == "__main__":
    window = ThemedTk(theme="equilux")
    window.geometry("500x200")
    window.resizable(width=False, height=False)
    window.config(bg="gray20")
    window.title("Mp3 Downloader")
    input = ttk.Entry(width=50)
    progressbar = ttk.Progressbar(window, length=300)
    button = ttk.Button(text="Download",command=(lambda: thread_download(input.get(),progressbar)))
    button.pack()
    input.pack(padx=10,pady=10)
    progressbar.pack()
    window.mainloop()

