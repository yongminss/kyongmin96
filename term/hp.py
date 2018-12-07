from pico2d import *
import game_framework

class HP:
    MAX_HP = 500
    def __init__(self):
        self.HP = load_image('../term/cookierun_image/HP.png')
        self.HP_count = self.MAX_HP
        self.x = 400
        self.y = 500
        self.fps = 0

        
    def draw(self):
        self.HP.clip_draw(0, 0, self.HP_count, 64, self.x, self.y)

    def update(self):
        self.fps += 1 * game_framework.frame_time
        if self.fps >= 0.1:
            self.HP_count -= 2
            self.fps = 0

        print(self.HP_count)
        # 체력 최대치
        if self.HP_count >= self.MAX_HP:
            self.HP_count = self.MAX_HP
        if self.HP_count <= 0:
            game_framework.quit()
                        
    def exit(self):
        pass
