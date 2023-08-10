from scraper import search_music
from dowloarder import download_music
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"

        # download_music(search_music("astro world"))

        return (
            MDScreen(
                

                MDRectangleFlatButton(
                    text="Hello, World",
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    onpress= (download_music(search_music("astro world")))),
                )
            )
    
MainApp().run()