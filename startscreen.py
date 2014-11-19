from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics import Rectangle, Ellipse, Line

NOTEXTURE = "assets/NOTEXTURE.png"


class StartScreen(Widget):
    def __init__(self):
        super(StartScreen, self).__init__()
        self.layout = FloatLayout()
        self.add_widget(self.layout)
        #Creating Widgets
        self.background = Image(
            source=NOTEXTURE,
            texture_size=Window.size,
            size=Window.size,
            allow_stretch=True,
            keep_ratio=False,
            x=0, y=0
        )
        self.logo = Image(
            source=NOTEXTURE,
            texture_size=(300, 300),
            size=(300, 300),
            center_x=Window.width / 2,
            center_y=(Window.height / 2) + 150
        )
        self.startText = Label(
            text="Poodle Jump 2014 Edition Platinum Edition #2014",
            center_x=Window.width / 2,
            center_y=Window.height / 2,
            font_size=32
        )
        self.startButton = Button(
            text="Start Game",
            width=Window.width / 2.6,
            height=Window.height / 8,
            center_x=Window.width / 2,
            center_y=Window.height / 2 - 100,
            font_size=32
        )
        self.settingsButton = Button(
            text="Settings",
            width=Window.width / 2.6,
            height=Window.height / 8,
            center_x=Window.width / 2,
            center_y=Window.height / 2 - 200,
            font_size=32
        )
        #matt did this button all by himself 11/18/14 python experiences id put a hashtag but thats meant for comments
        #dont tell me what to do jacob
        self.optionsButton = Image(
            source=NOTEXTURE,
            texture_size=(40, 40),
            size=(40, 40),
            center_x=Window.width - 40,
            center_y=Window.height - Window.height + 40
        )
        self.mouseTexture = Image(
            source="assets/CURSOR.png",
            texture_size=(20, 20),
            size=(20, 20)
        )
        #Adding Widgets
        self.layout.add_widget(self.background)
        self.layout.add_widget(self.logo)
        self.layout.add_widget(self.startText)
        self.layout.add_widget(self.startButton)
        self.layout.add_widget(self.settingsButton)
        self.layout.add_widget(self.optionsButton)
        self.layout.add_widget(self.mouseTexture)

        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def update(self, *args):
        self.mouseTexture.center_x = Window.mouse_pos[0]
        self.mouseTexture.center_y = Window.mouse_pos[1]