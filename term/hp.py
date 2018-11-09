from pico2d import *

class HP:
    def __init__(self):
        self.HP = load_image('../term/cookierun_image/HP.png')
        self.HP_count = 500
        self.x = 400
        self.y = 500

    def draw(self):
        self.HP.clip_draw(0, 0, self.HP_count, 64, self.x, self.y)

    def update(self):
        self.HP_count -= 2

    def exit(self):
        pass
