from pico2d import *
import game_world
import config
import time

class RunState:
    @staticmethod
    def enter(cookie):
        pass
    
    @staticmethod
    def exit(cookie):
        pass

    @staticmethod
    def update(cookie):
        pass

    @staticmethod
    def draw(cookie):
        pass


class JumpState:
    @staticmethod
    def enter(cookie):
        pass
    
    @staticmethod
    def exit(cookie):
        pass

    @staticmethod
    def update(cookie):
        pass

    @staticmethod
    def draw(cookie):
        pass

class SlideState:
    @staticmethod
    def enter(cookie):
        pass
    
    @staticmethod
    def exit(cookie):
        pass

    @staticmethod
    def update(cookie):
        pass

    @staticmethod
    def draw(cookie):
        pass


class Cookie:
    RUN, JUMP, DOUBLE_JUMP, SLIDE = 0, 1, 2, 3
    
    def __init__(self):
        self.cookie = load_image('../term/cookierun_image/Cookie_Run_State.png')
        self.state = self.RUN   # 쿠키의 상태
        self.x = 250    # 쿠키 x좌표
        self.y = 215    # 쿠키 y좌표
        self.frame = 0

    def get_bb(self):
        if self.state == self.RUN:
            return self.x - 60, self.y - 65, self.x + 60, self.y + 65
        elif self.state == self.JUMP:
            return self.x - 60, self.y - 40, self.x + 60, self.y + 70
        elif self.state == self.DOUBLE_JUMP:
            return self.x - 60, self.y - 40, self.x + 60, self.y + 70
        elif self.state == self.SLIDE:
            return self.x - 70, self.y - 30, self.x + 80, self.y + 40

    def draw(self):
        if self.state == self.RUN:              # 달리기
            self.cookie.clip_draw(self.frame * 120, 382 - 135, 120, 135,
                                  self.x, self.y)
        elif self.state == self.JUMP:           # 1단 점프
            self.cookie.clip_draw(0, 382 - 135 - 165, 140, 165, self.x, self.y)
        elif self.state == self.DOUBLE_JUMP:    # 2단 점프
            self.cookie.clip_draw(self.frame * 140, 382 - 135 - 165, 140, 165,
                                  self.x, self.y)
        elif self.state == self.SLIDE:          # 슬라이딩
            self.cookie.clip_draw(self.frame * 170, 382 - 135 - 165 - 80, 170, 80,
                                  self.x, self.y)
        # 충돌체크 박스
        if config.draws_bounding_box:
            draw_rectangle(*self.get_bb())

    def update(self):
        if self.state == self.RUN:
            self.frame = (self.frame + 1) % 3
        elif self.state == self.JUMP:
            self.frame = (self.frame + 1) % 1
        elif self.state == self.DOUBLE_JUMP:
            self.frame = (self.frame + 1) % 6
        elif self.state == self.SLIDE:
            self.frame = (self.frame + 1) % 2
        
    def handle_events(self, e):
        pass