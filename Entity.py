__author__ = 'JacobWunder'

from kivy.uix.widget import Widget
from kivy.uix.graphics import Rectangle, Line, Ellipse


class Entity(Widget):
    def __init__(self, sprite):
        super(Entity, self).__init__()
        self.sprite = sprite

        self.size = self.sprite.size

    def topLeft(self):
        return self.x, self.y + self.sprite.height

    def topRight(self):
        return self.x + self.sprite.width, self.y + self.sprite.height

    def bottomLeft(self):
        return self.x, self.y

    def bottomRight(self):
        return self.x + self.sprite.width, self.y

    def changeSprite(self, sprite):
        self.sprite = sprite

