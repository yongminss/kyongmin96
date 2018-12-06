from pico2d import *
import game_framework
import game_world
import config

class djTrap:
    image = None
    RUN_SPEED_PPS = 500
    def __init__(self):
        # 2단 점프 함정 초기화
        if djTrap.image == None:
            djTrap.image = load_image('../term/cookierun_image/Jump_trap_02.png')
        self.x = 900
        self.y = 245

    def get_bb(self):
        return self.x - 20, self.y - 45, self.x + 20, self.y + 45

    def draw(self):
        # 2단 점프 함정 그리기
        self.image.draw(self.x, self.y)
        # 충돌체크 박스
        if config.draws_bounding_box:
            draw_rectangle(*self.get_bb())

    def update(self):
        self.x -= djTrap.RUN_SPEED_PPS * game_framework.frame_time
        if self.x <= -10:
            game_world.remove_object(self)
            
