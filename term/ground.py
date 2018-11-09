from pico2d import *

class Ground:
    STAGE_1, STAGE_2 = range(2)
    
    def __init__(self):
        self.First_Ground = load_image('../term/cookierun_image/Ground_01.png')
        self.Second_Ground = load_image('../term/cookierun_image/Ground_02.png')
        self.frame = 0
        self.state = self.STAGE_1

    def draw(self):
        if self.state == self.STAGE_1:
            self.First_Ground.draw(400, 350)
        elif self.state == self.STAGE_2:
            self.Second_Ground.draw(400, 350)

    def update(self):
        if self.state == self.STAGE_1:
            self.frame += 10
            if self.frame >= 2490:
                self.state = self.STAGE_2
                self.frame = 0
        elif self.state == self.STAGE_2:
            self.frame += 10
            if self.frame >= 2490:
                self.frame = 0
        
    def exit(self):
        pass
