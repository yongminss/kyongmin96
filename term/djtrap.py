from pico2d import *
import config

class djTrap:
    image = None
    OFF, ON = 0, 1
    def __init__(self):
        # 2단 점프 함정 초기화
        if djTrap.image == None:
            djTrap.image = load_image('../term/cookierun_image/Jump_trap_02.png')
        self.x = 900
        self.y = 195
        self.state = self.OFF
        # 그 외 변수
        self.frame = 0

    def get_bb(self):
        return self.x - 20, self.y - 45, self.x + 20, self.y + 45

    def draw(self):
        # 2단 점프 함정 그리기
        if self.state == self.ON:
            self.image.draw(self.x, self.y)
        # 충돌체크 박스
        if config.draws_bounding_box:
            draw_rectangle(*self.get_bb())

    def update(self):
        self.frame += 10
        # 2단 점프 함정 이벤트 발생 조건
        if self.frame > 200:
            self.state = self.ON
        # 2단 점프 함정 state -> ON 일 때,
        if self.state == self.ON:
            self.x -= 10
