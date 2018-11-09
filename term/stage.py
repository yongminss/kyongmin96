from pico2d import *
import game_framework

class Stage:
    STAGE_1, STAGE_2 = range(2)

    def __init__(self):
        self.First_Stage = load_image('../term/cookierun_image/Stage_01.png')
        self.Second_Stage = load_image('../term/cookierun_image/Stage_02.png')
        self.frame = 0
        self.state = self.STAGE_1

    def draw(self):
        if self.state == self.STAGE_1:
            self.First_Stage.clip_draw(self.frame, 0, 800, 600, 400, 300)
        elif self.state == self.STAGE_2:
            self.Second_Stage.clip_draw(self.frame, 0, 800, 600, 400, 300)  

    def update(self):
        if self.state == self.STAGE_1:
            self.frame += 10
            if self.frame >= 2490:           # 일정 거리에 도착하면
                self.state = self.STAGE_2    # 스테이지 2로 교체
                self.frame = 0
        elif self.state == self.STAGE_2:
            self.frame += 10
            if self.frame >= 2490:
                game_framework.quit()
