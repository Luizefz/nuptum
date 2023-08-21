import webbrowser
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.fitimage import FitImage
from kivy.uix.label import Label
from scraper import download_music, search_music
from web_requests import get_top_song


class ManagerScreen(ScreenManager):
    pass


class HomeScreen(Screen):
    def search_top_songs(self):
        # response = get_top_song(self)
        # data = response["chart_items"]

        # print(response["chart_items"][0]["item"]["title"])

        # for element in data:
        #     try:
        box_layout = BoxLayout(orientation='vertical',
                                    size_hint_x=None,
                                    width="130dp",
                                    size=("130dp", "140dp"),
                                    spacing="10dp")
                
                # print(element["item"]["title"])
                # print(element["item"]["artist_names"])

        song_title = Label(text='Teste',
                                font_size="14sp",
                                color="#FFF6E0",
                                font_name="fonts/Poppins-SemiBold.ttf")

        artist_name = Label(text='Teste',
                                    font_size="16sp",
                                    color="#FFF6E0",
                                    font_name="fonts/Poppins-SemiBold.ttf")

        song_thumbnail_url = FitImage(source='https://images.genius.com/0388650ccc155fa3c34453d5011c6774.320x320x1.jpg',
                                            size_hint=(None, None),
                                            size=("130dp", "130dp"),
                                            radius=8)

        box_layout.add_widget(song_thumbnail_url)
        box_layout.add_widget(song_title)
        box_layout.add_widget(artist_name)

        self.ids.top_songs_grid.add_widget(box_layout)
        #     except Exception as e:
        #         print(e)

        # return


class SearchScreen(Screen):
    def start_download(self):
        music_name = self.ids.music_name.text
        if music_name:
            music_url = search_music(music_name)

            music_info = download_music(music_url)

            self.ids.music_name.text = ""  # Clear the text input after downloading

            try:
                print("Playing music...")
                webbrowser.open(music_info['path_music'])
            except Exception as e:
                print(e)
                return False
        else:
            return


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.material_style = "M3"
        self.title = "Nuptum Music"
        return Builder.load_file('menu.kv')


if __name__ == "__main__":
    MainApp().run()
