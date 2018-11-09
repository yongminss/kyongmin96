from pico2d import *

class sTrap:
    image = None
    OFF, ON = 0, 1
    def __init__(self):
        if sTrap.image == None:
            self.image = load_image('../term/cookierun_image/Slide_trap.png')
        self.x = 900
        self.y = 450
        self.state = self.OFF
        self.frame = 0
        
    def draw(self):
        if self.state == self.ON:
            self.image.draw(self.x, self.y)

    def update(self):
        self.frame += 10
        # 슬라이드 함정 발생 조건
        if self.frame > 250:
            self.state = self.ON
        # 슬라이드 함정 state -> ON 일 때,
        if self.state == self.ON:
            self.x -= 10
