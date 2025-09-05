import pyglet
from pyglet.window.key import *
class Ognestrel:
    def __init__(self, playr, phot="ognestrel.png", damag=10, mugsNum=10, mugsType="common", type=None, isP=True):
        self.ognTypes={}
        if not type or type not in self.ognTypes:
            self.damag=damag
            self.mugsNum=mugsNum
            self.mugsType=mugsType
            self.playr=playr
            photo=pyglet.image.load(phot,open(phot,"br"))
            self.pist=pyglet.sprite.Sprite(photo, playr.x, playr.y+3)
            self.isP=isP