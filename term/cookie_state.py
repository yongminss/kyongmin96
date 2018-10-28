from pico2d import *
import game_framework

class Stage:
    STAGE_1, STAGE_2 = 0, 1
    
    def __init__(self):
        self.First_Stage = load_image('../term/cookierun_image/Stage_01.png')
        self.Second_Stage = load_image('../term/cookierun_image/Stage_02.png')
        self.frame = 0
        self.state = self.STAGE_1

    def draw(self):
        if self.state == self.STAGE_1:
            self.First_Stage.clip_draw(self.frame, 0, 800, 600, 400, 300)
            if self.frame >= 2490:
                self.frame = 0
                self.state = self.STAGE_2
        elif self.state == self.STAGE_2:
            self.Second_Stage.clip_draw(self.frame, 0, 800, 600, 400, 300)
            if self.frame >= 2490:
                game_framework.quit()     

    def update(self):
        if self.state == self.STAGE_1:
            self.frame += 10
        elif self.state == self.STAGE_2:
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
        self.HP_Count -= 2


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


class Potion:
    potion = None
    OFF, ON = 0, 1 
    def __init__(self):
        if Potion.potion == None:
            self.potion = load_image('../term/cookierun_image/Item_HP.png')
        self.x = 900  # 포션 x좌표
        self.y = 215  # 포션 y좌표
        self.state = self.OFF
        self.frame = 0

    def draw(self):
        if self.state == self.ON:
            self.potion.draw(self.x, self.y)
        

    def update(self):
        self.frame += 10
        if self.frame >= 2490:
                self.frame = 0
        # 포션 이벤트
        if self.frame > 100:
            self.state = self.ON
            if self.state == self.ON:
                self.x -= 10


class Jelly:
    jelly = None
    OFF, ON = 0, 1
    def __init__(self):
        if Jelly.jelly == None:
            self.jelly = load_image('../term/cookierun_image/Item_Jelly.png')
        self.x = 900  # 젤리 x 좌표
        self.y = 215  # 젤리 y 좌표
        self.state = self.OFF
        self.frame = 0

    def draw(self):
        if self.state == self.ON:
            self.jelly.draw(self.x, self.y)

    def update(self):
        self.frame += 10
        if self.frame >= 2490:
                self.frame = 0
        # 젤리 이벤트
        if self.frame > 50:
            self.state = self.ON
            if self.state == self.ON:
                self.x -= 10

class Jump_Trap:
    trap01 = None   # 1단 점프 함정
    trap02 = None   # 2단 점프 함정
    OFF, ON = 0, 1
    def __init__(self):
        # 1단 점프 함정 초기화
        if Jump_Trap.trap01 == None:
            self.trap01 = load_image('../term/cookierun_image/Jump_trap_01.png')
        self.trap01_x = 900
        self.trap01_y = 175
        self.trap01_state = self.OFF
        # 2단 점프 함정 초기화
        if Jump_Trap.trap02 == None:
            self.trap02 = load_image('../term/cookierun_image/Jump_trap_02.png')
        self.trap02_x = 900
        self.trap02_y = 195
        self.trap02_state = self.OFF
        # 그 외 변수
        self.frame = 0

    def draw(self):
        # 1단 점프 함정 그리기
        if self.trap01_state == self.ON:
            self.trap01.draw(self.trap01_x, self.trap01_y)
        # 2단 점프 함정 그리기
        if self.trap02_state == self.ON:
            self.trap02.draw(self.trap02_x, self.trap02_y)

    def update(self):
        self.frame += 10
        # 1단 점프 함정 이벤트 발생 조건
        if self.frame > 150:
            self.trap01_state = self.ON
        # 1단 점프 함정 state -> ON 일 때,
        if self.trap01_state == self.ON:
            self.trap01_x -= 10
        # 2단 점프 함정 이벤트 발생 조건
        if self.frame > 200:
            self.trap02_state = self.ON
        # 2단 점프 함정 state -> ON 일 때,
        if self.trap02_state == self.ON:
            self.trap02_x -= 10
    

class Slide_Trap:
    trap = None
    OFF, ON = 0, 1
    def __init__(self):
        if Slide_Trap.trap == None:
            self.trap = load_image('../term/cookierun_image/Slide_trap.png')
        self.x = 900
        self.y = 450
        self.state = self.OFF
        self.frame = 0
        
    def draw(self):
        if self.state == self.ON:
            self.trap.draw(self.x, self.y)

    def update(self):
        self.frame += 10
        # 슬라이드 함정 발생 조건
        if self.frame > 250:
            self.state = self.ON
        # 슬라이드 함정 state -> ON 일 때,
        if self.state == self.ON:
            self.x -= 10


def handle_events():
    
    events = get_events()

    for e in events:
        if e.type == SDL_QUIT:
             game_framework.quit()
        else:
            C.handle_events(e)
                    

def enter():
    global S, G, U, C, P, J, J_T, S_T

    S = Stage()
    G = Ground()
    U = UI()
    C = Cookie()
    P = Potion()
    J = Jelly()
    J_T = Jump_Trap()
    S_T = Slide_Trap()

def draw():
    clear_canvas()
    S.draw()    # 스테이지
    G.draw()    # 바닥
    U.draw()    # UI
    C.draw()    # 쿠키
    P.draw()    # 포션
    J.draw()    # 젤리
    J_T.draw()  # 점프 함정
    S_T.draw()  # 슬라이딩 함정
    update_canvas()

def update():
    S.update()      # 스테이지
    U.update()      # UI
    C.update()      # 쿠키
    P.update()      # 포션
    J.update()      # 젤리
    J_T.update()    # 점프 함정
    S_T.update()    # 슬라이딩 함정
    delay(0.06)

def exit():
    pass

if __name__ == '__main__':
	import sys
	current_module = sys.modules[__name__]	
	open_canvas()
	game_framework.run(current_module)
	close_canvas()
