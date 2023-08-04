from urllib.request import urlopen
import re

def search_music(music_name):
    print("\nSearching for " + music_name + "...\n")
    request_url = "https://www.youtube.com/results?search_query=" + music_name.replace(" ", "+")
    response = urlopen(request_url).read().decode() # Faz o scrape da pagina do youtube
    find_video_id = re.findall("watch\?v=(\S{11})", response) # Pesquisa no scrape "watch\?v=(\S{11})" e devolve somente o id do video
    return "https://www.youtube.com/watch?v=" + find_video_id[0]