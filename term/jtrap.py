from pico2d import *
import game_framework
import game_world
import config

class jTrap:
    image = None
    RUN_SPEED_PPS = 500
    def __init__(self):
        # 1단 점프 함정 초기화
        if jTrap.image == None:
            jTrap.image = load_image('../term/cookierun_image/Jump_trap_01.png')
        self.x = 900
        self.y = 225

    def get_bb(self):
        return self.x - 15, self.y - 25, self.x + 15, self.y + 25
        
    def draw(self):
        # 1단 점프 함정 그리기
        self.image.draw(self.x, self.y)
        # 충돌체크 박스
        if config.draws_bounding_box:
            draw_rectangle(*self.get_bb())

    def update(self):
        self.x -= jTrap.RUN_SPEED_PPS * game_framework.frame_time
        if self.x <= -10:
            game_world.remove_object(self)
