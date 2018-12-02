from pico2d import *
import random
import game_world
import config

class Jelly:
    jelly = None
    OFF, ON = 0, 1
    def __init__(self):
        if Jelly.jelly == None:
            self.jelly = load_image('../term/cookierun_image/Item_Jelly.png')
        self.x = 850                            # 젤리 x 좌표
        self.y = 270 + random.randint(0, 200)   # 젤리 y 좌표

    def get_bb(self):
        return self.x - 10, self.y - 15, self.x + 10, self.y + 15

    def draw(self):
        self.jelly.draw(self.x, self.y)
        # 충돌체크 박스
        if config.draws_bounding_box:
            draw_rectangle(*self.get_bb())

    def update(self):
        self.x -= 10
        if self.x <= -10:
            game_world.remove_object(self)
