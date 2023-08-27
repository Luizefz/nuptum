import re
import os
import json
from unidecode import unidecode
from pytube import YouTube
from urllib.request import urlopen

filename = 'musics/music_info.json'
music_downloaded = {}

def search_music(music_name):
    print("Finding music...")

    try:
        clear_music_name = unidecode(music_name).replace(" ", "+") # Remove acentos e espaços da string
        url_request = f"https://www.youtube.com/results?search_query={clear_music_name}+audio"
        response = urlopen(url_request).read().decode() # Faz o scrape da pagina do youtube
        find_video_id = re.findall("watch\?v=(\S{11})", response) # Pesquisa regex no scrape e devolve o id do video
        music_url = f"https://www.youtube.com/watch?v={find_video_id[0]}"

        print(f"Music found! URL: {music_url}")

        return music_url

    except Exception as e:
        print("Music not found.")
        print(e)
        return False

def download_music(url_video):
    try:
        video = YouTube(url_video)
        audio_stream = video.streams.filter(only_audio=True).first().download(
            output_path='musics') # Pega o stream de audio e faz o download
        
        base_name, ext = os.path.splitext(audio_stream)
        audio_stream_mp3 = base_name + ".mp3"
        os.rename(audio_stream, audio_stream_mp3) # Renomeia o arquivo para .mp3

        music = {
            'music_title': video.title,
            'music_author': video.author,
            'music_thumbnail': video.thumbnail_url,
            'path_music': audio_stream_mp3
        }

        print("Music downloaded successfully!")
        music_downloaded[url_video[32:-1]] = music # Salva no dicionario com o id do Youtube
        
        try:
            with open(filename, "r") as json_file: # Carrega os dados existentes do arquivo
                existing_data = json.load(json_file) 

        except FileNotFoundError:
            existing_data = {}

        existing_data.update(music_downloaded) # Adiciona os novos dados aos dados existentes

        with open(filename, "w") as json_file: # Salva os dados atualizados de volta no arquivo
            json.dump(existing_data, json_file, indent=4)

        return music

    except Exception as e:
        print(e)
        return False

if __name__ == "__main__":
    music_name = input("Enter the music name: ")
    music_info = search_music(music_name)
    music_download = download_music(music_info)

    if music_info:
        print("Music was downloaded!")
    else:
        print("Music not found or could not be downloaded.")