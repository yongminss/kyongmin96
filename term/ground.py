from pico2d import *

class ParallexLayer:
    def __init__(self, imageName):
        self.image = load_image(imageName)
        self.w, self.h = 800, 600
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.frame = 0

    def draw(self):
        self.image.clip_draw_to_origin(self.x1, 0, self.w1, self.h, 0, 0)
        self.image.clip_draw_to_origin(self.x2, 0, self.w2, self.h, self.w1, 0)
    
    def update(self):
        self.frame += 5
        self.x1 = self.frame % self.image.w
        self.w1 = self.image.w - self.x1
        self.x2 = 0
        self.w2 = self.cw - self.w1

class Ground:
    def __init__(self):
        self.Fground = [
            ParallexLayer('../term/cookierun_image/Ground_01.png')
            ]
        self.Sground = [
            ParallexLayer('../term/cookierun_image/Ground_02.png')
            ]

    def draw(self):
        for l in self.Fground: l.draw()

    def update(self):
        for l in self.Fground: l.update()
