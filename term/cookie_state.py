from pico2d import *
import game_framework

class Stage:
    def __init__(self):
        self.First_Stage = load_image('../term/cookierun_image/Stage_01.png')
        self.frame = 0

    def draw(self):
        self.First_Stage.clip_draw(self.frame, 0, 800, 600, 400, 300)

    def update(self):
        self.frame += 10

class Ground:
    def __init__(self):
        self.First_Ground = load_image('../term/cookierun_image/Ground_01.png')

    def draw(self):
        self.First_Ground.draw(400, 350)

class UI:
    def __init__(self):
        self.HP = load_image('../term/cookierun_image/HP.png')
        self.HP_Count = 500

    def draw(self):
        self.HP.clip_draw(0, 0, self.HP_Count, 64, 400, 500)

    def update(self):
        self.HP_Count -= 1

class Cookie:
    RUN, JUMP, DOUBLE_JUMP, SLIDE = 0, 1, 2, 3
    
    def __init__(self):
        self.cookie = load_image('../term/cookierun_image/Cookie_Run_State.png')
        self.state = self.RUN   # 쿠키의 상태
        self.x = 250    # 쿠키 x좌표
        self.y = 215    # 쿠키 y좌표
        self.frame = 0

    def draw(self):
        if self.state == self.RUN:  # 달리기
            self.cookie.clip_draw(self.frame * 120, 382 - 135, 120, 135,
                                  self.x, self.y)
        elif self.state == self.JUMP:   # 1단 점프
            self.cookie.clip_draw(0, 382 - 135 - 165, 140, 165, self.x, self.y)
        elif self.state == self.DOUBLE_JUMP:    # 2단 점프
            self.cookie.clip_draw(self.frame * 140, 382 - 135 - 165, 140, 165,
                                  self.x, self.y)
        elif self.state == self.SLIDE:  # 슬라이딩
            self.cookie.clip_draw(self.frame * 170, 382 - 135 - 165 - 80, 170, 80,
                                  self.x, self.y)

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
        

def handle_events():
    
    events = get_events()

    for e in events:
        if e.type == SDL_QUIT:
             game_framework.quit()
        else:
            C.handle_events(e)
                    

def enter():
    global S, G, U, C

    S = Stage()
    G = Ground()
    U = UI()
    C = Cookie()


def draw():
    clear_canvas()
    S.draw()    # 스테이지
    G.draw()    # 바닥
    U.draw()    # UI
    C.draw()    # 쿠키
    update_canvas()

def update():
    S.update()
    U.update()
    C.update()
    delay(0.06)

def exit():
    pass

if __name__ == '__main__':
	import sys
	current_module = sys.modules[__name__]	
	open_canvas()
	game_framework.run(current_module)
	close_canvas()
