import json
import webbrowser
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.fitimage import FitImage
from kivy.uix.label import Label
from scraper import download_music, search_music, filename
from web_requests import tranding_musics


class ManagerScreen(ScreenManager):
    pass


class HomeScreen(Screen):

    def show_tranding_musics(self):
        parsed_top_musics = tranding_musics()

        self.ids.top_today_grid.clear_widgets()

        for music in parsed_top_musics['chart_items']:
            chart_item = music["item"]
            music_title = chart_item["title"]
            music_author = chart_item["artist_names"]
            music_thumbnail = chart_item["header_image_url"]

            self.add_music_card('top_today_grid', music_title,
                                music_author, music_thumbnail)

    def show_recently_musics(self):
        try:
            with open(filename, "r") as json_file:  # Carrega os dados existentes do arquivo
                existing_data = json.load(json_file)

            parsed_top_musics = existing_data

            self.ids.top_month_grid.clear_widgets()

            if parsed_top_musics:
                for music_id, music in parsed_top_musics.items():
                    music_title = music['music_title']
                    music_author = music['music_author']
                    music_thumbnail = music['music_thumbnail']

                    self.add_music_card('top_month_grid', music_title,
                                        music_author, music_thumbnail, music["path_music"])

        except Exception as e:
            print(e)
            return False

    def add_music_card(self, music_carousel_id, music_title, music_author, music_thumbnail, music_url=None):

        box_layout = BoxLayout(orientation='vertical',
                               size_hint_x=None,
                               width="130dp",
                               size=("130dp", "140dp"),
                               spacing="10dp")
        song_title = Label(text=music_title[:15],
                           font_size="16sp",
                           color="#FFF6E0",
                           font_name="fonts/Poppins-SemiBold.ttf")
        artist_name = Label(text=music_author[:15],
                            font_size="14sp",
                            color="#FFF6E0",
                            font_name="fonts/Poppins-SemiBold.ttf")
        song_thumbnail_url = FitImage(source=music_thumbnail,
                                      size_hint=(None, None),
                                      size=("130dp", "130dp"),
                                      radius=8)

        box_layout.add_widget(song_thumbnail_url)
        box_layout.add_widget(song_title)
        box_layout.add_widget(artist_name)

        if music_carousel_id == 'top_today_grid':
            self.ids.top_today_grid.add_widget(box_layout)
        elif music_carousel_id == 'top_month_grid':
            self.ids.top_month_grid.add_widget(box_layout)

        box_layout.bind(on_touch_down=lambda instance, touch: self.on_music_card_touch(box_layout, touch, music_url))


class SearchScreen(Screen):
    def start_download(self):
        music_name = self.ids.music_name.text
        if music_name:
            music_url = search_music(music_name)
            music_info = download_music(music_url)

            self.ids.music_name.text = ""  # Clear the text input after downloading
            
            self.play_music(music_info['path_music'])
            # try:
            #     print("Playing music...")
            #     webbrowser.open(music_info['path_music'])
            # except Exception as e:
            #     print(e)
            #     return False
        else:
            return
        
    def play_music(self, music_path):
        try:
            print("Playing music...")
            webbrowser.open(music_path)
        except Exception as e:
            print(e)
            return False


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.material_style = "M3"
        self.title = "Nuptum Music"
        return Builder.load_file('menu.kv')


if __name__ == "__main__":
    MainApp().run()
