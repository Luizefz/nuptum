import requests

error_json = {
  "chart_items": [
    {
      "item": {
        "title": "Somenthing wrong",
        "primary_artist": {
          "header_image_url": "https://images.genius.com/0388650ccc155fa3c34453d5011c6774.320x320x1.jpg",
          "artist_names": "with Today Top Songs",
        }
      }
    },
  ]
}

def get_top_song(self):

    url = "https://genius-song-lyrics1.p.rapidapi.com/chart/songs/"

    querystring = {"per_page":"10","page":"1"}

    headers = {
        "X-RapidAPI-Key": "557d5eae85mshbeea91322709584p145f0ejsn1e8d",
        "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    
    if response.status_code == 200:
        print("Today Top Songs - Successful request")
        return(response.json())
    else:
        print("Today Top Songs - Error in request")
        return(error_json)