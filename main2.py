from yt_dlp import YoutubeDL

def download(url):
    yt_opts = {
        'format': 'bestvideo+bestaudio/best',  # Select both best video and best audio
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',  # Merge video and audio into a single mp4 file
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Convert to mp4 format if needed
        }],
    }

    with YoutubeDL(yt_opts) as ydl:
        ydl.download([url])


url = input("Enter video url: ")
download(url)
