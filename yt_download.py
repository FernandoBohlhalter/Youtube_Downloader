from tkinter import *
import customtkinter as ctk
from center_func import center_screen
import downloader

#colors
red = '#FF0000'
black = '#0F0F0F'
dark_gray = '#272727'
gray = '#404040'

#variables
stream_res = []
placeholder = ['']

#create window
root = ctk.CTk()
root.iconbitmap('yt_icon.ico')
root.title('YouTube Downloader')
root.resizable(False, False)
center_screen(root, 500, 400)

#Gets the video resolutions
def set_res_btn():
    link = textBox.get()
    global streams
    
    stream_res, streams = downloader.get_resolution(link)
    resBox.configure(values = stream_res)

#Downloads the video on resolution of preference
def download():
    res = resBox.get()
    downloader.download_video(streams, res)

#-----------=============App body=============-----------#
mainframe = ctk.CTkFrame(root, fg_color=black, bg_color=black)
mainframe.pack(fill='both', expand=True)

text = ctk.CTkLabel(mainframe, text='YouTube Downloader', font=('Helvetica', 20, 'bold'))
text.place(relx=0.5, rely= 0.15, anchor='c')

cframe = ctk.CTkFrame(mainframe, fg_color=black, height=300, width=500)
cframe.place(relx=0.5, rely=0.63, anchor="c")
#cframe.pack(fill='x', expand=True)

label1 = ctk.CTkLabel(cframe, text_color=gray, font=('Helvetica', 11), text='Insert link:')
label1.place(relx=0.255, rely=0.03, anchor='nw')
textBox = ctk.CTkEntry(cframe, fg_color='#090909', border_width=1, border_color=dark_gray, width=173)
textBox.place(relx=0.6, rely=0.12, anchor='ne')
res_btn = ctk.CTkButton(cframe, text='Ok', fg_color=dark_gray, text_color='white', font=('Helvetica', 12, 'bold'), border_width=0, width=50, hover_color=('#CF0000'), command= set_res_btn)
res_btn.place(relx=0.65, rely=0.12, anchor='nw')

label2 = ctk.CTkLabel(cframe, text_color=gray, font=('Helvetica', 11), text='Resolution:')
label2.place(relx=0.25, rely=0.30, anchor='nw')
resBox = ctk.CTkComboBox(cframe, width=250, fg_color='#090909', font=('Helvetica', 13), dropdown_font=('Helvetica', 13), button_color=dark_gray, button_hover_color=('#CF0000'), dropdown_fg_color=dark_gray, dropdown_hover_color=gray,border_width=1, border_color=dark_gray, corner_radius=7, values=placeholder)
resBox.place(relx=0.5, rely=0.44, anchor='c')

download_btn = ctk.CTkButton(cframe, text='Download', fg_color=dark_gray, text_color='white', font=('Helvetica', 15, 'bold'), border_width=0, height=50, width=120, corner_radius=10, hover_color=('#CF0000'), command=download)
download_btn.place(relx = 0.5, rely = 0.65, anchor='c')
#-----------=============App body=============-----------#

root.mainloop()