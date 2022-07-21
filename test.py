import tkinter
from tkinter import filedialog

#ウィンドウで最初に立ち上げるディレクトリを指定
idir = 'C:/Users/xxxx/Desktop'
file_path = tkinter.filedialog.askopenfilename(initialdir = idir)