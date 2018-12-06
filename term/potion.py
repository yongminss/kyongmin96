from pico2d import *
import game_framework
import game_world
import config

class Potion:
    potion = None
    RUN_SPEED_PPS = 500
    def __init__(self):
        if Potion.potion == None:
            self.potion = load_image('../term/cookierun_image/Item_HP.png')
        self.x = 900  # 포션 x좌표
        self.y = 270  # 포션 y좌표

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def draw(self):
        self.potion.draw(self.x, self.y)
        # 충돌체크 박스
        if config.draws_bounding_box:
            draw_rectangle(*self.get_bb())
        
    def update(self):
        self.x -= Potion.RUN_SPEED_PPS * game_framework.frame_time
        if self.x <= -10:
            game_world.remove_object(self)

    def exit(self):
        pass
