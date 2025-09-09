import pyglet
from pyglet.window.key import *
bat = pyglet.graphics.Batch()
mugs = {}
class Ognestrel:
    def __init__(self, playr, phot="ognestrel.png", damag=10, mugsNum=10, mugsType="common", type=None, isP=True, bat=bat):
        self.ognTypes={}
        if not type or type not in self.ognTypes:
            self.damag = damag
            self.mugsNum = mugsNum
            self.mugsType = mugsType
            self.playr = playr
            #photo = pyglet.image.load(phot, open(phot, "br"))
            self.pist = pyglet.shapes.Line(playr.x, playr.y+6, playr.x-10, playr.y+6,2)
            #pyglet.sprite.Sprite(photo, playr.x, playr.y+3)
            self.x = playr.x
            self.y = playr.y+6
            self.x2 = playr.x-10
            self.y2 = playr.y 
            self.isP = isP
            self.bat=bat
    

    def shot(self):
        global mugs
        global bat
        if self.x > self.x2:
            mug = pyglet.shapes.Line(self.x2, self.y, self.x2 + 3, self.y, color = [200, 236, 100], batch = bat)
            mugs[mug] = (0.5, 0)
            return mug
    

    def pulaMoving(self, dt):
        for i in mugs:
            i.x += mugs[i][0]
            i.y += mugs[i][1]