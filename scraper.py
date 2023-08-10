import re
from unidecode import unidecode
from pytube import YouTube
from urllib.request import urlopen

musics_info = {}

def search_music(music_name):
    clear_music_name = unidecode(music_name).replace(" ", "+") # Remove acentos e espaços da string
    url_request = f"https://www.youtube.com/results?search_query={clear_music_name}+visualizer"
    response = urlopen(url_request).read().decode() # Faz o scrape da pagina do youtube

    find_video_id = re.findall("watch\?v=(\S{11})", response) # Pesquisa regex no scrape e devolve o id do video
    return f"https://www.youtube.com/watch?v={find_video_id[0]}"

def download_music(url_video):
    video = YouTube(url_video) # Choose a stream with desired audio quality
    
    audio_stream = video.streams.filter(only_audio=True).first() # Download the audio stream
    
    audio_stream.download(output_path='musics') # Create the music info dictionary
    
    music = {
        'name': video.title,
        'path_music': f'musics/{audio_stream.default_filename}'
    } # Use slicing to get the key in musics_info
    
    musics_info[url_video[32:-1]] = music

    return music

# def download_music(url_video):
#     video = YouTube(url_video)
#     video_downloader = video.streams.filter(only_audio=True).first().download('musics')

#     music = {
#     'name' : video.streams[0].title,
#     'path_music': video_downloader.replace("\\", "/")
#     }

#     musics_info[url_video[32:-1]] = music
#     return music

if __name__ == "__main__":
    music_name = input("Enter the music name: ")
    music_info = search_music(music_name)
    
    if music_info:
        print("Music downloaded successfully!")
        print("Music Info:", music_info)
    else:
        print("Music not found or could not be downloaded.")