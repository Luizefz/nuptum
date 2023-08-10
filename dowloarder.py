from pytube import YouTube

def download_music(url_video):
        video = YouTube(url_video)
        video_downloader = video.streams.filter(only_audio=True).first().download()
        return video_downloader