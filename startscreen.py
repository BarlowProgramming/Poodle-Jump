from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics import Rectangle, Ellipse, Line

class StartScreen(Widget):
    def __init__(self):
        super(StartScreen, self).__init__()
        self.layout = FloatLayout()
        self.add_widget(self.layout)
        self.startText = Label(text="Poodle Jump 2014 Edition Platinum Edition 2014",
                               center_x=Window.width / 2,
                               center_y=Window.height / 2,
                               font_size=32)
        self.layout.add_widget(self.startText)

        Clock.schedule_interval(self.update, 1.0 / 60.0)
        self.startText.bind(on_touch_move=self.on_touch_move)

    def on_touch_move(self, *args):
        self.startText.center_x = Window.mouse_pos[0]
        self.startText.center_y = Window.mouse_pos[1]

    def update(self, *args):
        self.canvas.after.clear()
        self.startText.canvas.after.clear()
        with self.startText.canvas.after:
            Rectangle(pos=(self.startText.x,
                           self.startText.y),
                      size=(self.startText.width,
                            self.startText.height))

        with self.canvas.after:
            Rectangle(pos=(Window.mouse_pos[0],
                           Window.mouse_pos[1]),
                      size=(10,
                            10))