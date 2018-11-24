from pico2d import *
import config

class jTrap:
    image = None
    OFF, ON = 0, 1
    def __init__(self):
        # 1단 점프 함정 초기화
        if jTrap.image == None:
            jTrap.image = load_image('../term/cookierun_image/Jump_trap_01.png')
        self.x = 900
        self.y = 225
        self.state = self.OFF
        # 그 외 변수
        self.frame = 0

    def get_bb(self):
        return self.x - 15, self.y - 25, self.x + 15, self.y + 25
        
    def draw(self):
        # 1단 점프 함정 그리기
        if self.state == self.ON:
            self.image.draw(self.x, self.y)
        # 충돌체크 박스
        if config.draws_bounding_box:
            draw_rectangle(*self.get_bb())

    def update(self):
        self.frame += 10
        # 1단 점프 함정 이벤트 발생 조건
        if self.frame > 500:
            self.state = self.ON
        # 1단 점프 함정 state -> ON 일 때,
        if self.state == self.ON:
            self.x -= 10
