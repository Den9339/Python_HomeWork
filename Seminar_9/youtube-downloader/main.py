from pytube import YouTube

yt = YouTube(input('Вставьте ссылку на видео: '))

path = input('Напишите адрес папки, куда скачать файл: ')
yt.streams.filter(progressive=True, file_extension='mp4')
yt.streams.order_by('resolution')
yt.streams.desc()
yt.streams.first().download(path)