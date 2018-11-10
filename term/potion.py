from pico2d import *
import config

class Potion:
    potion = None
    OFF, ON = 0, 1 
    def __init__(self):
        if Potion.potion == None:
            self.potion = load_image('../term/cookierun_image/Item_HP.png')
        self.x = 900  # 포션 x좌표
        self.y = 215  # 포션 y좌표
        self.state = self.OFF
        self.frame = 0

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def draw(self):
        if self.state == self.ON:
            self.potion.draw(self.x, self.y)
        # 충돌체크 박스
        if config.draws_bounding_box:
            draw_rectangle(*self.get_bb())
        
    def update(self):
        self.frame += 10
        if self.frame >= 2490:
                self.frame = 0
        # 포션 이벤트
        if self.frame > 100:
            self.state = self.ON
            if self.state == self.ON:
                self.x -= 10

    def exit(self):
        pass
