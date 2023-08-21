import requests
import json

url = "https://genius-song-lyrics1.p.rapidapi.com/chart/songs/"

headers = {
    "X-RapidAPI-Key": "557d5eae85mshbeea91322709584p145f0ejsn1e8d9fbf9e3b",
    "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
}

default_data = {
    "chart_items": [
        {
            "item": {
                "title": "Ops!",
                "primary_artist": {
                    "header_image_url": "https://ibb.co/b7M1wwy",
                    "artist_names": "Resquest failed",
                }
            }
        },
    ],
}


def tranding_musics():
    querystring = {"per_page": "10", "page": "1"}

    try:
        response_data = requests.get(url, headers=headers, params=querystring)
        print(f"Request Today Top Songs - {response_data.status_code}")
        return response_data.json()

    except Exception as e:
        print(e)
        return json.loads(json.dumps(default_data))


def top_month_musics():
    querystring = {"time_period": "month", "per_page": "10", "page": "1"}

    headers = {
        "X-RapidAPI-Key": "557d5eae85mshbeea91322709584p145f0ejsn1e8d9fbf9e3b",
        "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
    }

    try:
        response_data = requests.get(url, headers=headers, params=querystring)
        print(f"Request Moth Top Songs - {response_data.status_code}")
        return response_data.json()

    except Exception as e:
        print(e)
        return json.loads(json.dumps(default_data))
