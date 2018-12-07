from pico2d import *
import game_framework

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
        self.frame += Stage.RUN_SPEED_PPS
        self.x1 = self.frame % self.image.w
        self.w1 = self.image.w - self.x1
        self.x2 = 0
        self.w2 = self.cw - self.w1

class Stage:
    RUN_SPEED_PPS = 10
    First, Second = 0, 1
    def __init__(self):
        self.Fstage = [
            ParallexLayer('../term/cookierun_image/Stage_01.png')
            ]
        self.Sstage = [
            ParallexLayer('../term/cookierun_image/Stage_02.png')
            ]
        self.state = self.First
        
    def draw(self):
        if self.state == self.First:
            for l in self.Fstage: l.draw()
        elif self.state == self.Second:
            for l in self.Sstage: l.draw()

    def update(self):
        self.RUN_SPEED_PPS += self.RUN_SPEED_PPS * game_framework.frame_time
        if self.state == self.First:
            for l in self.Fstage: l.update()
        elif self.state == self.Second:
            for l in self.Sstage: l.update()
