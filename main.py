import webbrowser
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from scraper import download_music, search_music

class ManagerScreen(ScreenManager):
    pass

class HomeScreen(Screen):
    pass

class SearchScreen(Screen):
    def start_download(self):
        music_name = self.ids.music_name.text
        if music_name:
            music_url = search_music(music_name)
            
            music_info = download_music(music_url)

            self.ids.music_name.text = ""  # Clear the text input after downloading
            
            print("Playing music...")
            webbrowser.open(music_info['path_music'])
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
