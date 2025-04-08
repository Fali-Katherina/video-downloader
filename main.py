from yt_dlp import YoutubeDL

def download(url):
    yt_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        
        }

    with YoutubeDL(yt_opts) as ydl:
        ydl.download([url])


url = input("Enter video url: ")
download(url)

