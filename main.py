import webbrowser
from kivy.lang import Builder
from kivymd.app import MDApp
from scraper import download_music, search_music

KV = '''
MDScreen:
    MDTextField:
        id: music_name
        hint_text: "Digite o nome da música"
        helper_text: "Post malone one right now"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .5, "center_y": .6}
        size_hint_x: .5

    MDRectangleFlatButton:
        text: "Download Music"
        pos_hint: {"center_x": 0.4, "center_y": 0.5}
        on_press: app.start_download(self)

    MDFloatingActionButton:
        text: "Stop music"
        icon: "android"
        text_color: "white"
        pos_hint: {"center_x": .6, "center_y": .5}

'''

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        return self.screen
    
    def start_download(self, instance):
        
        print("Finding music...")
        music_info = search_music(self.screen.ids.music_name.text)
        
        print("Music found, starting download...")
        music_info = download_music(music_info)

        self.screen.ids.music_name.text = ""

        print("Music downloaded successfully!")

        print("Playing music...")
        webbrowser.open(music_info['path_music'])
        
MainApp().run()