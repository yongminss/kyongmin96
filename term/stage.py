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
        self.frame += 10
        self.x1 = self.frame % self.image.w
        self.w1 = self.image.w - self.x1
        self.x2 = 0
        self.w2 = self.cw - self.w1

class Stage:
    def __init__(self):
        self.Fstage = [
            ParallexLayer('../term/cookierun_image/Stage_01.png')
            ]
        self.Sstage = [
            ParallexLayer('../term/cookierun_image/Stage_02.png')
            ]
        
    def draw(self):
        for l in self.Fstage: l.draw()

    def update(self):
        for l in self.Fstage: l.update()
