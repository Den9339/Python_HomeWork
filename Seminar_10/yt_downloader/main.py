from pytube import YouTube

from tkinter import *
from tkinter import messagebox
from tkinter import ttk  
from tkinter.ttk import Progressbar


def button(enter_url, enter_path):
    yt = YouTube(enter_url)
    yt.streams.filter(progressive=True)
    yt.streams.order_by('resolution').desc().first().download(enter_path)
    messagebox.showinfo('Приложение скачивания видео с YouTube!', 'Файл успешно скачан!') 

# Окно программы
window = Tk()
window.title("Добро пожаловать в приложение скачивания видео с YouTube!")
window.geometry('550x130')

# Добавление текста для ссылки на видео
lbl = Label(window, text="Вставьте ссылку на видео:", pady=15)  
lbl.grid(column=0, row=1)  
# Поле ввода ссылки
txt_url = Entry(window,width=50)  
txt_url.grid(column=1, row=1)  
txt_url.focus()

# Добавление текста для пути скачивания
lbl = Label(window, text="Укажите путь скачивания файла:", padx=15, pady=5)  
lbl.grid(column=0, row=2) 
# Поле ввода пути скачивания
txt_path = Entry(window,width=50)  
txt_path.grid(column=1, row=2)  

# # Прогресс бар
# style = ttk.Style()  
# style.theme_use('default')  
# style.configure("black.Horizontal.TProgressbar", background='green')  
# bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')  
# bar['value'] = 50
# bar.grid(column=1, row=0, pady=10) 


# Конпка для скачивния
btn = Button(window, text="Скачать", command=lambda: button(txt_url.get(), txt_path.get()))
btn.grid(column=1, row=3)  


window.mainloop()