from pico2d import *
import config

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

    def get_bb(self):
        return self.x - 100, self.y - 225, self.x + 100, self.y + 150
        
    def draw(self):
        if self.state == self.ON:
            self.image.draw(self.x, self.y)
        # 충돌체크 박스
        if config.draws_bounding_box:
            draw_rectangle(*self.get_bb())

    def update(self):
        self.frame += 10
        # 슬라이드 함정 발생 조건
        if self.frame > 250:
            self.state = self.ON
        # 슬라이드 함정 state -> ON 일 때,
        if self.state == self.ON:
            self.x -= 10
