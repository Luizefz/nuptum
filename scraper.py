import re
from unidecode import unidecode
from urllib.request import urlopen

def search_music(music_name):
    clear_music_name = unidecode(music_name).replace(" ", "+") # Remove acentos e espaços da string
    url_request = f"https://www.youtube.com/results?search_query={clear_music_name}+visualizer"
    response = urlopen(url_request).read().decode() # Faz o scrape da pagina do youtube

    find_video_id = re.findall("watch\?v=(\S{11})", response) # Pesquisa regex no scrape e devolve o id do video
    return f"https://www.youtube.com/watch?v={find_video_id[0]}"