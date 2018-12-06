from pico2d import *
import game_framework
import game_world
import config

class sTrap:
    image = None
    RUN_SPEED_PPS = 500
    def __init__(self):
        if sTrap.image == None:
            self.image = load_image('../term/cookierun_image/Slide_trap.png')
        self.x = 900
        self.y = 500

    def get_bb(self):
        return self.x - 40, self.y - 225, self.x + 40, self.y + 150
        
    def draw(self):
        self.image.draw(self.x, self.y)
        # 충돌체크 박스
        if config.draws_bounding_box:
            draw_rectangle(*self.get_bb())

    def update(self):
        self.x -= sTrap.RUN_SPEED_PPS * game_framework.frame_time
        if self.x <= -10:
            game_world.remove_object(self)
        
