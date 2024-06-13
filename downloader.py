from pytube import YouTube
import os

downloadable = []

def get_resolution(link):
    yt = YouTube(link)
    streams = yt.streams.order_by('resolution').desc()
    prog_streams = streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
    res = []

    
    #separa resoluções possiveis
    for i in range(len(prog_streams)):
        res.append(prog_streams[i].resolution)
    res = list(set(res))

    #separa melhor opção de download para cada resolução
    downloadable = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').asc()

    return(res, downloadable)


def download_video(downloadable, resolution):
    #faz o download
    #video_title = resolution+' - '+title+'.mp4'
    for i in range(len(downloadable)):
        print(downloadable[i].resolution)
        if resolution == downloadable[i].resolution:
            downloadable[i].download(output_path = 'Downloads')
        
        os.startfile('Downloads')
