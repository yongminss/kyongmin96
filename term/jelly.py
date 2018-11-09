from pico2d import *

class Jelly:
    jelly = None
    OFF, ON = 0, 1
    def __init__(self):
        if Jelly.jelly == None:
            self.jelly = load_image('../term/cookierun_image/Item_Jelly.png')
        self.x = 900  # 젤리 x 좌표
        self.y = 215  # 젤리 y 좌표
        self.state = self.OFF
        self.frame = 0

    def draw(self):
        if self.state == self.ON:
            self.jelly.draw(self.x, self.y)

    def update(self):
        self.frame += 10
        if self.frame >= 2490:
                self.frame = 0
        # 젤리 이벤트
        if self.frame > 50:
            self.state = self.ON
            if self.state == self.ON:
                self.x -= 10
