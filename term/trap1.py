from pico2d import *

class jTrap:
    trap01 = None   # 1단 점프 함정
    trap02 = None   # 2단 점프 함정
    OFF, ON = 0, 1
    def __init__(self):
        # 1단 점프 함정 초기화
        if jTrap.trap01 == None:
            self.trap01 = load_image('../term/cookierun_image/Jump_trap_01.png')
        self.trap01_x = 900
        self.trap01_y = 175
        self.trap01_state = self.OFF
        # 2단 점프 함정 초기화
        if jTrap.trap02 == None:
            self.trap02 = load_image('../term/cookierun_image/Jump_trap_02.png')
        self.trap02_x = 900
        self.trap02_y = 195
        self.trap02_state = self.OFF
        # 그 외 변수
        self.frame = 0

    def draw(self):
        # 1단 점프 함정 그리기
        if self.trap01_state == self.ON:
            self.trap01.draw(self.trap01_x, self.trap01_y)
        # 2단 점프 함정 그리기
        if self.trap02_state == self.ON:
            self.trap02.draw(self.trap02_x, self.trap02_y)

    def update(self):
        self.frame += 10
        # 1단 점프 함정 이벤트 발생 조건
        if self.frame > 150:
            self.trap01_state = self.ON
        # 1단 점프 함정 state -> ON 일 때,
        if self.trap01_state == self.ON:
            self.trap01_x -= 10
        # 2단 점프 함정 이벤트 발생 조건
        if self.frame > 200:
            self.trap02_state = self.ON
        # 2단 점프 함정 state -> ON 일 때,
        if self.trap02_state == self.ON:
            self.trap02_x -= 10
