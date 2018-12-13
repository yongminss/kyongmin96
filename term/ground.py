from pico2d import *
import game_framework
import time

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
        # 바닥 애니메이션 처리
        self.frame += Ground.RUN_SPEED_PPS
        self.x1 = self.frame % self.image.w
        self.w1 = self.image.w - self.x1
        self.x2 = 0
        self.w2 = self.cw - self.w1


class Ground:
    RUN_SPEED_PPS = 10
    First, Second = 0, 1
    def __init__(self):
        self.Fground = [
            ParallexLayer('../term/cookierun_image/Ground_01.png')
            ]
        self.Sground = [
            ParallexLayer('../term/cookierun_image/Ground_02.png')
            ]
        self.state = Ground.First
        self.StartTime = time.time()

    def draw(self):
        if self.state == Ground.First:
            for l in self.Fground: l.draw()
        elif self.state == Ground.Second:
            for l in self.Sground: l.draw()

    def update(self):
        self.RUN_SPEED_PPS += self.RUN_SPEED_PPS * game_framework.frame_time

        StateTime = time.time() - self.StartTime

        # 바닥 변경 조건
        if StateTime >= 66.0:
            self.state = self.Second

        if self.state == Ground.First:
            for l in self.Fground: l.update()
        elif self.state == Ground.Second:
            for l in self.Sground: l.update()