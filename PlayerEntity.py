__author__ = 'JacobWunder'

from kivy.uix.widget import Widget
from kivy.uix.graphics import Rectangle, Line, Ellipse
from entity import Entity


class PlayerEntity(Entity):
    def __init__(self):
        super(PlayerEntity, self).__init__()

